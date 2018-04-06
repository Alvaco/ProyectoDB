import taller.modules.postgresql_conn as p
import datetime

p.conexion()
#p.eliminarTablas()
#p.crearTablas()

#emp = [0, "Juan", "Lopez", "Calle A", "14782", "kdsfl", "10/10/2010", "21", "15418542", "M", "Mecanico", "Operativo", "3000", "_joseMart"]
#p.crearEmpleado(emp)

#ve = [0, 1, "355SDF", "picanto", "KIA", "2014", "Negro"]
#p.crearVehiculo(ve)

#p.asignarEmpleadoVehiculo(ve)

#p.mostrarTabla()

#capa = [0, "10/10/2015", "Expresion Oral", "95"]
#p.crearCapacitacion(capa)

#p.mostrarTabla()

#print(p.capacitacionesEmpleado(0))

#entrada = [0, 0, "22/07/2015", "3000"]

#p.crearEntradaHistorial(entrada)

#p.mostrarTabla()

#print(p.historialSalarialEmpleado(0))

#accion = [0, "14/02/2017", "Llegada tarde", "Llego 20 minutos tarde"]
#p.crearAccionDisciplinaria(accion)

#p.mostrarTabla()

p.eliminarEmpleado(2)