from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import taller.modules.Tweets as twitter
import taller.modules.postgresql_conn as postgres
#Variables de

parametrosEmpleadosFiltrados = []



def index(request):
    opciones = ['Ver Lista de Empleados', 'Busqueda Filtrada de Tweets']
    opcionesUrls = ["/taller/listaEmpleados/", "/taller/busquedaFiltradaTweets/"]
    context = {'opciones':opciones, 'opcionesUrls': opcionesUrls}
    return render(request,'taller/templates/taller/index.html',context=context)

def listaEmpleados(request):
    global parametrosEmpleadosFiltrados
    postgres.conexion()
    empleados = []
    hayFiltros = False

    if(len(parametrosEmpleadosFiltrados) != 0):
        for i in range(0,len(parametrosEmpleadosFiltrados)):
            if(parametrosEmpleadosFiltrados[i].replace(" ","") != ""):
                hayFiltros = True

    if(hayFiltros):
        empleados = postgres.busquedaFiltradaEmpleados(parametrosEmpleadosFiltrados)
    else:
        empleados = postgres.informacionGeneneralVariosEmpleados()
    context = {'empleados' : empleados}
    return render(request,'taller/templates/taller/listaEmpleados.html',context=context)

#Actualizar Perfil
def perfilEmpleado(request, id_empleado):
    postgres.conexion()
    informacionGeneral = postgres.informacionGeneralUnEmpleado(id_empleado)

    tweetsUsuario = twitter.getUserTweets(informacionGeneral['Twitter'])

    vehiculos = postgres.informacionVehiculosEmpleado(id_empleado)

    capacitaciones = postgres.capacitacionesEmpleado(id_empleado)

    historial_salarios_puesto = postgres.historialSalarialEmpleado(id_empleado)

    acciones_disciplinarias = postgres.accionesDisciplinariasEmpleado(id_empleado)

    context = {'id_empleado':id_empleado, 'informacionGeneral': informacionGeneral, 'tweets': tweetsUsuario, 'vehiculos': vehiculos, 'capacitaciones': capacitaciones, 'historial_salario_puesto': historial_salarios_puesto, 'acciones_disciplinarias': acciones_disciplinarias}
    return render(request, 'taller/templates/taller/perfilEmpleado.html', context=context)

def actualizarEmpleadoDatosGenerales(request, id_empleado):
    postgres.conexion()
    context = postgres.informacionGeneralUnEmpleado(id_empleado)
    context['id_empleado'] = context.pop('Numero identificacion')
    context['Tipo_Empleado'] = context.pop('Tipo Empleado')
    context['Contratacion'] = context.pop('Fecha Contratacion')

    return render(request,'taller/templates/taller/actualizarEmpleadoDatosGenerales.html', context=context)

def actualizarEmpleadoDatosGeneralesACT(request, id_empleado):
    postgres.conexion()
    emp = []
    emp.append(id_empleado)
    emp.append(request.GET['nombre'])
    emp.append(request.GET['apellido'])
    emp.append(request.GET['direccion'])
    emp.append(request.GET['telefono'])
    emp.append(request.GET['correo'])
    emp.append(request.GET['fecha_contratacion'])
    emp.append(request.GET['edad'])
    emp.append(request.GET['dpi'])
    emp.append(request.GET['sexo'])
    emp.append(request.GET['puesto'])
    emp.append(request.GET['tipo_empleado'])
    emp.append(request.GET['salario'])
    emp.append(request.GET['twitter'])
    #TODO: Actualizar datos del empleado
    postgres.actualizarEmpleado(emp)

    return HttpResponseRedirect(reverse('perfilEmpleado', args=(id_empleado,)))

def agregarVehiculo(request, id_empleado):
    postgres.conexion()
    context = {'id_empleado': id_empleado}
    return render(request,'taller/templates/taller/agregarVehiculo.html', context=context)

def agregarVehiculoACT(request, id_empleado):
    postgres.conexion()
    vehiculo = []
    vehiculo.append(id_empleado)
    vehiculo.append(postgres.nuevoIdVehiculo())
    vehiculo.append(request.GET['placa'])
    vehiculo.append(request.GET['modelo'])
    vehiculo.append(request.GET['marca'])
    vehiculo.append(request.GET['anio'])
    vehiculo.append(request.GET['color'])

    postgres.crearVehiculo(vehiculo)
    postgres.asignarEmpleadoVehiculo(vehiculo)
    return HttpResponseRedirect(reverse('perfilEmpleado', args=(id_empleado,)))

def agregarCapacitacion(request, id_empleado):
    postgres.conexion()
    context = {'id_empleado' : id_empleado}
    return render(request,'taller/templates/taller/agregarCapacitacion.html', context=context)

def agregarCapacitacionACT(request, id_empleado):
    postgres.conexion()
    capa = []

    capa.append(id_empleado)
    capa.append(request.GET['fecha'])
    capa.append(request.GET['capacitacion'])
    capa.append(request.GET['calificacion'])

    postgres.crearCapacitacion(capa)
    return HttpResponseRedirect(reverse('perfilEmpleado', args=(id_empleado,)))

def agregarHistorial(request, id_empleado):
    postgres.conexion()
    context = {'id_empleado' : id_empleado}
    return render(request,'taller/templates/taller/agregarHistorial.html', context=context)

def agregarHistorialACT(request, id_empleado):
    postgres.conexion()
    entrada = []

    entrada.append(id_empleado)
    entrada.append(request.GET['id_puesto'])
    entrada.append(request.GET['fecha_puesto'])
    entrada.append(request.GET['salario'])

    postgres.crearEntradaHistorial(entrada)
    return HttpResponseRedirect(reverse('perfilEmpleado', args=(id_empleado,)))

def agregarAccion(request, id_empleado):
    postgres.conexion()
    context = {'id_empleado': id_empleado}
    return render(request,'taller/templates/taller/agregarAccion.html', context=context)

def agregarAccionACT(request, id_empleado):
    postgres.conexion()
    accion = []

    accion.append(id_empleado)
    accion.append(request.GET['fecha_accion'])
    accion.append(request.GET['accion'])
    accion.append(request.GET['observaciones'])

    postgres.crearAccionDisciplinaria(accion)
    return HttpResponseRedirect(reverse('perfilEmpleado', args=(id_empleado,)))

#Eliminar
def eliminarEmpleado(request, id_empleado):
    postgres.conexion()
    empleado = postgres.informacionGeneralUnEmpleado(id_empleado)
    twit = empleado['Twitter']
    twitter.unfollowUser(twit)
    postgres.eliminarEmpleado(id_empleado)
    return HttpResponseRedirect(reverse(listaEmpleados)) #Con dialogo de verificacion

def buscarEmpleado(request):
    postgres.conexion()
    global parametrosEmpleadosFiltrados
    parametrosEmpleadosFiltrados = []
    parametrosEmpleadosFiltrados.append(request.GET['nombre'])
    parametrosEmpleadosFiltrados.append(request.GET['apellido'])
    parametrosEmpleadosFiltrados.append(request.GET['direccion'])
    parametrosEmpleadosFiltrados.append(request.GET['telefono'])
    parametrosEmpleadosFiltrados.append(request.GET['correo'])
    parametrosEmpleadosFiltrados.append(request.GET['fecha_contratacion'])
    parametrosEmpleadosFiltrados.append(request.GET['edad'])
    parametrosEmpleadosFiltrados.append(request.GET['dpi'])
    parametrosEmpleadosFiltrados.append(request.GET['sexo'])
    parametrosEmpleadosFiltrados.append(request.GET['puesto'])
    parametrosEmpleadosFiltrados.append( request.GET['tipo_empleado'])
    parametrosEmpleadosFiltrados.append(request.GET['salario'])
    parametrosEmpleadosFiltrados.append(request.GET['twitter'])

    return HttpResponseRedirect(reverse(listaEmpleados))


#Agregar Empleado
def agregarNuevoEmpleado(request):
    postgres.conexion()
    context = {}
    return render(request, 'taller/templates/taller/agregarEmpleado.html', context=context)

def agregarEmpleado(request):
    postgres.conexion()
    emp = []
    nuevoID = postgres.nuevoIdEmpleado()
    emp.append(nuevoID)
    emp.append(request.GET['nombre'])
    emp.append(request.GET['apellido'])
    emp.append(request.GET['direccion'])
    emp.append(request.GET['telefono'])
    emp.append(request.GET['correo'])
    emp.append(request.GET['fecha_contratacion'])
    emp.append(request.GET['edad'])
    emp.append(request.GET['dpi'])
    emp.append(request.GET['sexo'])
    emp.append(request.GET['puesto'])
    emp.append(request.GET['tipo_empleado'])
    emp.append(request.GET['salario'])
    emp.append(request.GET['twitter'])

    postgres.crearEmpleado(emp)
    return HttpResponseRedirect(reverse(listaEmpleados))

#Busqueda filtrada de tweets
tweetsFiltrados = []
palabra = ""
def busquedaFiltradaTwitter(request):
    global palabra, tweetsFiltrados
    context = {'palabra': palabra, 'tweetsFiltrados': tweetsFiltrados}
    return render(request, 'taller/templates/taller/busquedaFiltradaTwitter.html', context=context)

def busquedaFiltradaTwitterACT(request):
    global palabra, tweetsFiltrados
    palabra = request.GET['palabra']

    tweetsFiltrados = twitter.getFilterTweets(palabra)
    return HttpResponseRedirect(reverse(busquedaFiltradaTwitter))