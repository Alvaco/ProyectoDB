import psycopg2
from terminaltables import AsciiTable
import datetime

##CONEXION

def conexion():
    global con
    global conn
    global cur

    con = None
    conn = psycopg2.connect(database="postgres", user="postgres", password="Guatemala101296", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    print("CONEXION EXITOSA")


##CREACION TABLAS

def crearTablas():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
        empleadoID INT NOT NULL,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        direccion VARCHAR(50),
        telefono VARCHAR(50),
        correo VARCHAR(50),
        fecha_contratacion DATE,
        edad INT,
        dpi VARCHAR(50),
        sexo VARCHAR(10),
        puesto VARCHAR(50),
        tipo_empleado VARCHAR(50),
        salario FLOAT,
        twitter VARCHAR(50),
        PRIMARY KEY (empleadoID)
        );
        ''')
    print("TABLA empleados CREADA")

    cur.execute('''
        CREATE TABLE IF NOT EXISTS vehiculos (
        vehiculoID INT NOT NULL,
        placa VARCHAR(50),
        modelo VARCHAR(50),
        marca VARCHAR(50),
        anio VARCHAR(50),
        color VARCHAR(50),
        PRIMARY KEY (vehiculoID)
        );
        ''')
    print("TABLA vehiculos CREADA")

    cur.execute('''
        CREATE TABLE  IF NOT EXISTS vehiculos_asignados (
        vehiculoID INT,
        empleadoID INT,
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID),
        FOREIGN KEY (vehiculoID) REFERENCES vehiculos(vehiculoID)
        );
        ''')
    print("TABLA vehiculos_asignados CREADA")

    cur.execute('''
        CREATE TABLE IF NOT EXISTS historial (
        empleadoID INT,
        puestoID INT NOT NULL,
        fecha_puesto DATE,
        salario FLOAT(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print("TABLA historial CREADA")

    cur.execute('''
        CREATE TABLE IF NOT EXISTS capacitaciones (
        empleadoID INT,
        fecha_capacitacion DATE,
        capacitacion VARCHAR(50),
        calificacion FLOAT(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print("TABLA capacitaciones CREADA")

    cur.execute('''
        CREATE TABLE IF NOT EXISTS acciones (
        empleadoID INT,
        fecha_accion DATE,
        accion_otorgada VARCHAR(50),
        explicacion VARCHAR(100),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print("TABLA acciones CREADA")

    cur.execute('''
        CREATE TABLE IF NOT EXISTS administrativos (
        empleadoID INT,
        oficina VARCHAR(50),
        tel_oficina VARCHAR(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print("TABLA administrativos CREADA")

    cur.execute('''
        CREATE TABLE IF NOT EXISTS operativos (
        empleadoID INT,
        tipo_licencia VARCHAR(10),
        uso_lentes VARCHAR(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print("TABLA operativos CREADA")


##ELIMINAR TABLAS

def eliminarTablas():
    cur.execute('''
        DROP TABLE IF EXISTS historial CASCADE;
        ''')
    conn.commit()
    print("TABLAS ELIMINADAS")


##CREACION TUPLAS

def crearEmpleado(emp):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'empleados'")

    query = "INSERT INTO empleados (empleadoID, nombre, apellido, direccion, telefono, correo, fecha_contratacion, edad, dpi, sexo, puesto, tipo_empleado, salario, twitter) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10], emp[11], emp[12], emp[13])
    cur.execute(query, data)
    conn.commit()

def nuevoIdEmpleado():
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'empleados'")

    cur.execute("SELECT MAX(empleadoID) FROM empleados ")
    row = cur.fetchall()

    return row[0][0] + 1

def crearVehiculo(ve):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'vehiculos'")

    query = "INSERT INTO vehiculos (vehiculoID, placa, modelo, marca, anio, color) \
                VALUES (%s, %s, %s, %s, %s, %s)"
    data = (
         ve[1], ve[2], ve[3], ve[4], ve[5], ve[6])
    cur.execute(query, data)
    conn.commit()

def nuevoIdVehiculo():
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'vehiculos'")

    cur.execute("SELECT MAX(vehiculoID) FROM vehiculos ")
    row = cur.fetchall()

    return row[0][0] + 1

def asignarEmpleadoVehiculo(ve):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'vehiculos_asignados'")

    query = "INSERT INTO vehiculos_asignados (vehiculoID, empleadoID) \
                VALUES (%s, %s)"
    data = (
         ve[1], ve[0])
    cur.execute(query, data)
    conn.commit()


def crearCapacitacion(capa):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'capacitaciones'")

    query = "INSERT INTO capacitaciones (empleadoID, fecha_capacitacion, capacitacion, calificacion) \
                    VALUES (%s, %s, %s, %s)"
    data = (
       capa[0], capa[1], capa[2], capa[3])
    cur.execute(query, data)
    conn.commit()

def crearEntradaHistorial(entrada):
    cur.execute("SELECT column_name \
                    FROM   information_schema.columns \
                    WHERE  table_name = 'historial'")

    query = "INSERT INTO historial (empleadoID, puestoID, fecha_puesto, salario) \
                        VALUES (%s, %s, %s, %s)"
    data = (
        entrada[0], entrada[1], entrada[2], entrada[3])
    cur.execute(query, data)
    conn.commit()

def crearAccionDisciplinaria(accion):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'acciones'")

    query = "INSERT INTO acciones (empleadoID, fecha_accion, accion_otorgada, explicacion) \
                            VALUES (%s, %s, %s, %s)"
    data = (
        accion[0], accion[1], accion[2], accion[3])
    cur.execute(query, data)
    conn.commit()


##MOSTRAR TABLAS

def mostrarTabla():

    cur.execute("SELECT column_name \
            FROM   information_schema.columns \
            WHERE  table_name = 'acciones'")


    colnames = cur.fetchall()

    cur.execute("SELECT * FROM acciones")
    row = cur.fetchall()

    table_data = [colnames, row[0]]
    table = AsciiTable(table_data)
    print(table.table)

#Informacion General Empleado
def informacionGeneneralVariosEmpleados():
    informacionGeneralVariosEmpleados = []
    informacionGeneralUnEmpleado = {}

    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'empleados'")

    cur.execute("SELECT * FROM empleados")
    row = cur.fetchall()

    nom = ['id_empleado', 'Nombre', 'Apellido', 'Dirreccion', 'Telefono', 'Correro', 'Fecha Contratacion', 'Edad', 'DPI',
           'Sexo', 'Puesto', 'Tipo Empleado', 'Salario', 'Twitter']

    for i in range(0, len(row)):
        r = row[i]
        for j in range(0, len(nom)):
            llave = nom[j]
            valor = r[j]
            if(llave == 'Fecha Contratacion'):
                valor = valor.strftime('%m/%d/%Y')

            informacionGeneralUnEmpleado.update({llave: valor})

        informacionGeneralVariosEmpleados.append(informacionGeneralUnEmpleado.copy())
        print(informacionGeneralUnEmpleado)
        informacionGeneralUnEmpleado.clear()

    return informacionGeneralVariosEmpleados #Devuelve una lista con todos los empleados

def informacionGeneralUnEmpleado(id_empleado):
    informacionGeneralUnEmpleado = {}
    cur.execute("SELECT column_name \
                    FROM   information_schema.columns \
                    WHERE  table_name = 'empleados'")

    cur.execute("SELECT * FROM empleados WHERE empleadoID = " + str(id_empleado))
    row = cur.fetchall()
    r = row[0]
    nom = ['Numero identificacion', 'Nombre', 'Apellido', 'Direccion', 'Telefono', 'Correo', 'Fecha Contratacion', 'Edad',
           'DPI',
           'Sexo', 'Puesto', 'Tipo Empleado', 'Salario', 'Twitter']

    for j in range(0, len(nom)):
        llave = nom[j]
        valor = r[j]
        if (llave == 'Fecha Contratacion'):
            valor = valor.strftime('%m/%d/%Y')

        informacionGeneralUnEmpleado.update({llave: valor})

    return informacionGeneralUnEmpleado  # Devuelve una lista con todos los empleados

def busquedaFiltradaEmpleados(filtros):
    llaves = ["nombre", "apellido", "direccion", "telefono", "correo", "fecha_contratacion", "edad", "dpi", "sexo", "puesto", "tipo_empleado", "salario", "twitter"]

    strWhere = " WHERE "

    for i in range(0,len(llaves)):
        if(filtros[i] != ""):
            if(llaves[i] == "fecha_contratacion" or llaves[i] == "edad" or llaves == "salario"):
                try:
                    if (llaves[i] == "fecha_contratacion"):
                        filtros[i] = datetime.datetime.strptime(filtros[i], "%d/%m/%Y").strftime("%d/%m/%y")
                    elif (llaves[i] == "edad"):
                        filtros[i] = str(int(filtros[i]))
                    else:
                        filtros[i]= str(float(filtros[i]))
                except ValueError:
                    if (llaves[i] == "fecha_contratacion"):
                        filtros[i] = datetime.datetime.strptime("10/10/2010", "%d/%m/%Y").strftime("%d/%m/%y")
                    elif (llaves[i] == "edad"):
                        filtros[i] = 18
                    else:
                        filtros[i] = 1000

            strWhere = strWhere + llaves[i] + " = " + "'" + filtros[i] + "'" + " AND "

    strWhere = strWhere[:len(strWhere)-5]

    informacionGeneralVariosEmpleados = []
    informacionGeneralUnEmpleado = {}

    cur.execute("SELECT column_name \
                    FROM   information_schema.columns \
                    WHERE  table_name = 'empleados'")

    cur.execute("SELECT * FROM empleados" + strWhere)
    row = cur.fetchall()

    nom = ['id_empleado', 'Nombre', 'Apellido', 'Dirreccion', 'Telefono', 'Correro', 'Fecha Contratacion', 'Edad',
           'DPI',
           'Sexo', 'Puesto', 'Tipo Empleado', 'Salario', 'Twitter']

    for i in range(0, len(row)):
        r = row[i]
        for j in range(0, len(nom)):
            llave = nom[j]
            valor = r[j]
            if (llave == 'Fecha Contratacion'):
                valor = valor.strftime('%m/%d/%Y')

            informacionGeneralUnEmpleado.update({llave: valor})

        informacionGeneralVariosEmpleados.append(informacionGeneralUnEmpleado.copy())
        print(informacionGeneralUnEmpleado)
        informacionGeneralUnEmpleado.clear()

    return informacionGeneralVariosEmpleados  # Devuelve una lista con todos los empleados filtrados

#Informacion Vehiculos Empleado
def informacionVehiculosEmpleado(id_empleado):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'vehiculos'")

    cur.execute("SELECT * FROM vehiculos WHERE vehiculoID IN (SELECT vehiculoID FROM vehiculos_asignados WHERE empleadoID = " + str(id_empleado) + ")")
    row = cur.fetchall()
    nom = ['vehiculoID', 'Placa', 'Modelo', 'Anio', 'Marca', 'Color']
    vehiculos = []
    for j in range(0, len(row)):
        vehiculo = {}
        r = row[j]
        for i in range(1, len(nom)):
            vehiculo.update({nom[i]: r[i]})
        vehiculos.append(vehiculo.copy())
        vehiculo.clear()

    return vehiculos

#Informacion Capacitaciones Empleado
def capacitacionesEmpleado(id_empleado):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'capacitaciones'")

    cur.execute("SELECT * FROM capacitaciones WHERE empleadoID = " + str(id_empleado))
    row = cur.fetchall()
    nom = ['empleadoID', 'Fecha Capacitacion', 'Capacitacion', 'Calificacion']
    capacitaciones = []
    for j in range(0, len(row)):
        capacitacion = {}
        r = row[j]
        for i in range(1, len(nom)):
            llave = nom[i]
            valor = r[i]
            if (llave == 'Fecha Capacitacion'):
                valor = valor.strftime('%m/%d/%Y')
            capacitacion.update({llave: valor})
        capacitaciones.append(capacitacion.copy())
        capacitacion.clear()

    return capacitaciones


def historialSalarialEmpleado(id_empleado):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'historial'")

    cur.execute("SELECT * FROM historial WHERE empleadoID = " + str(id_empleado))
    row = cur.fetchall()
    nom = ['empleadoID', 'Puesto ID', 'Fecha Asignacion', 'Salario']
    historial_salarios_puesto = []
    for j in range(0, len(row)):
        entrada = {}
        r = row[j]
        for i in range(1, len(nom)):
            llave = nom[i]
            valor = r[i]
            if (llave == 'Fecha Asignacion'):
                valor = valor.strftime('%m/%d/%Y')
            entrada.update({llave: valor})
        historial_salarios_puesto.append(entrada.copy())
        entrada.clear()

    return historial_salarios_puesto


def accionesDisciplinariasEmpleado(id_empleado):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'acciones'")

    cur.execute("SELECT * FROM acciones WHERE empleadoID = " + str(id_empleado))
    row = cur.fetchall()
    nom = ['empleadoID', 'Fecha', 'Accion Otorgada', 'Observaciones']
    acciones_disciplinarias = []
    for j in range(0, len(row)):
        accion = {}
        r = row[j]
        for i in range(1, len(nom)):
            llave = nom[i]
            valor = r[i]
            if (llave == 'Fecha'):
                valor = valor.strftime('%m/%d/%Y')
            accion.update({llave: valor})
        acciones_disciplinarias.append(accion.copy())
        accion.clear()

    return acciones_disciplinarias


##ACTUALIZAR DATOS

def actualizarEmpleado(emp):
    cur.execute("SELECT column_name \
                        FROM   information_schema.columns \
                        WHERE  table_name = 'empleados'")

    query = """ UPDATE empleados
                SET (nombre, apellido, direccion, telefono, correo, fecha_contratacion, edad, dpi, sexo, puesto, tipo_empleado, salario, twitter)=(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                WHERE empleadoID = %s
                """
    data = (emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10], emp[11], emp[12], emp[13], emp[0])

    cur.execute(query, data)
    conn.commit()

#Eliminar Empleado
def eliminarEmpleado(id_empleado):
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'empleados'")

    cur.execute("DELETE FROM empleados WHERE empleadoID = " + str(id_empleado))
    conn.commit()