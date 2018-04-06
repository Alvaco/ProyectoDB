from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listaEmpleados/', views.listaEmpleados, name='listaEmpleados'),

    #Agregar Empleado
    path('listaEmpleados/agregarNuevoEmpleado/', views.agregarNuevoEmpleado, name='agregarNuevoEmpleado'),
    path('listaEmpleados/agregarNuevoEmpleado/agregarEmpleado/', views.agregarEmpleado, name='agregarEmpleado'),

    #Actualizar Perfil
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/actualizarEmpleadoDatosGenerales/', views.actualizarEmpleadoDatosGenerales, name='actualizarEmpleadoDatosGenerales'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/actualizarEmpleadoDatosGenerales/actualizarEmpleadoDatosGeneralesACT', views.actualizarEmpleadoDatosGeneralesACT, name='actualizarEmpleadoDatosGeneralesACT'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarVehiculo', views.agregarVehiculo, name='agregarVehiculo'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarVehiculoACT', views.agregarVehiculoACT, name='agregarVehiculoACT'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarCapacitacion', views.agregarCapacitacion, name='agregarCapacitacion'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarCapacitacionACT/', views.agregarCapacitacionACT, name='agregarCapacitacionACT'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarHistorial', views.agregarHistorial, name='agregarHistorial'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarHistorialACT/', views.agregarHistorialACT, name='agregarHistorialACT'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarAccion', views.agregarAccion, name='agregarAccion'),
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/agregarAccionACT/', views.agregarAccionACT, name='agregarAccionACT'),

    #Eliminar
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/eliminarEmpleado/', views.eliminarEmpleado, name='eliminarEmpleado'),

    #Perfil
    path('listaEmpleados/perfilEmpleado/<int:id_empleado>/',views.perfilEmpleado, name='perfilEmpleado'),

    #Buscar Filtros
    path('buscar/', views.buscarEmpleado,name='buscar'),

    #Bscar Filtros Tweets
    path('busquedaFiltradaTweets/', views.busquedaFiltradaTwitter,name='busquedaFiltradaTwitter'),
    path('busquedaFiltradaTweets/buscar/', views.busquedaFiltradaTwitterACT,name='busquedaFiltradaTwitterACT'),
]