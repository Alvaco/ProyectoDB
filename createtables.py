import psycopg2
from terminaltables import AsciiTable

##CONEXION

def conexion():
    global con
    global conn
    global cur
    
    con = None
    conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    print ("CONEXION EXITOSA")

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
        PRIMARY KEY (empleadoID)
        );
        ''')
    print ("TABLA empleados CREADA")


    cur. execute('''
        CREATE TABLE IF NOT EXISTS vehiculos (
        vehiculoID INT NOT NULL,
        placa VARCHAR(50),
        modelo VARCHAR(50),
        marca VARCHAR(50),
        aÃ±o VARCHAR(50),
        color VARCHAR(50),
        PRIMARY KEY (vehiculoID)
        );
        ''')
    print ("TABLA vehiculos CREADA")


    cur.execute('''
        CREATE TABLE  IF NOT EXISTS vehiculos_asignados (
        vehiculoID INT,
        empleadoID INT,
        dia_semana VARCHAR(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID),
        FOREIGN KEY (vehiculoID) REFERENCES vehiculos(vehiculoID)
        );
        ''')
    print ("TABLA vehiculos_asignados CREADA")


    cur.execute('''
        CREATE TABLE IF NOT EXISTS historial (
        empleadoID INT,
        puestoID INT NOT NULL,
        fecha_puesto DATE,
        salario FLOAT(50),
        PRIMARY KEY (puestoID),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print ("TABLA historial CREADA")


    cur.execute('''
        CREATE TABLE IF NOT EXISTS capacitaciones (
        empleadoID INT,
        fecha_capacitacion DATE,
        capacitacion VARCHAR(50),
        calificacion FLOAT(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print ("TABLA capacitaciones CREADA")


    cur.execute('''
        CREATE TABLE IF NOT EXISTS acciones (
        empleadoID INT,
        fecha_accion DATE,
        accion_otorgada VARCHAR(50),
        explicacion VARCHAR(100),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print ("TABLA acciones CREADA")


    cur.execute('''
        CREATE TABLE IF NOT EXISTS administrativos (
        empleadoID INT,
        oficina VARCHAR(50),
        tel_oficina VARCHAR(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print ("TABLA administrativos CREADA")


    cur.execute('''
        CREATE TABLE IF NOT EXISTS operativos (
        empleadoID INT,
        tipo_licencia VARCHAR(10),
        uso_lentes VARCHAR(50),
        FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
        );
        ''')
    print ("TABLA operativos CREADA")

##ELIMINAR TABLAS

def eliminarTablas():
    cur.execute('''
        DROP TABLE IF EXISTS empleados CASCADE;
        ''')
    conn.commit()
    print ("TABLAS ELIMINADAS")

    
##CREACION TUPLAS
    
def crearEmpleado():
    
    emp=[]
    emp.append(input("INGRESE EMPLEADO ID "))
    emp.append(input("INGRESE NOMBRE "))
    emp.append(input("INGRESE APELLIDO "))
    emp.append(input("INGRESE DIRECCION "))
    emp.append(input("INGRESE TELEFONO "))
    emp.append(input("INGRESE CORREO "))
    emp.append(input("INGRESE FECHA DE CONTRATACION "))
    emp.append(input("INGRESE EDAD "))
    emp.append(input("INGRESE DPI "))
    emp.append(input("INGRESE SEXO "))
    emp.append(input("INGRESE PUESTO "))
    emp.append(input("INGRESE TIPO DE EMPLEADO "))
    emp.append(input("INGRESE SALARIO "))


    query =  "INSERT INTO empleados (empleadoID, nombre, apellido, direccion, telefono, correo, fecha_contratacion, edad, dpi, sexo, puesto, tipo_empleado, salario) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10], emp[11], emp[12])
    cur.execute(query, data)
    conn.commit()


##MOSTRAR TABLAS
    
def mostrarTabla():\
    
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'empleados'")
    colnames = cur.fetchall()

    cur.execute("SELECT * FROM empleados") 
    row = cur.fetchall()
    
    table_data=[colnames, row[0]]
    table = AsciiTable(table_data)
    print (table.table)

def infGen():
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'empleados'")

    cur.execute("SELECT * FROM empleados") 
    row = cur.fetchall()
    informacionGeneral={}
    r=row[0]
    nom=['empleadoID', 'Nombre', 'Apellido', 'Dirreccion', 'Telefono', 'Correro', 'Fecha Contratacion', 'Edad', 'DPI', 'Sexo', 'Puesto', 'Tipo Empleado', 'Salario', 'Twitter']
    for i in range(0, len(nom)):
        informacionGeneral.update({nom[i]:r[i]})


def vehiculos():
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'vehiculos'")

    cur.execute("SELECT * FROM vehiculos") 
    row = cur.fetchall()
    nom=['vehiculoID', 'Placas', 'Modelo', 'Anio', 'Marca', 'Color']
    vehiculos=[]
    for j in range(0, len(row)):
        vehiculo={}
        r=row[j]
        for i in range(0, len(nom)):
            vehiculo.update({nom[i]:r[i]})
        vehiculos.append(vehiculo)


def capacitaciones():
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'capacitaciones'")

    cur.execute("SELECT * FROM capacitaciones") 
    row = cur.fetchall()
    nom=['empleadoID', 'Capacitacion', 'Fecha Capacitacion', 'Calificacion']
    capacitaciones=[]
    for j in range(0, len(row)):
        capacitacion={}
        r=row[j]
        for i in range(0, len(nom)):
            capacitacion.update({nom[i]:r[i]})
        capacitaciones.append(capacitacion)


def histSal():
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'historial'")

    cur.execute("SELECT * FROM historial") 
    row = cur.fetchall()
    nom=['empleadoID', 'Fecha Asignacion', 'Puesto', 'Salario']
    historial_salarios_puesto=[]
    for j in range(0, len(row)):
        hist={}
        r=row[j]
        for i in range(0, len(nom)):
            hist.update({nom[i]:r[i]})
        historial_salarios_puesto.append(hist)


def accD():
    cur.execute("SELECT column_name \
                FROM   information_schema.columns \
                WHERE  table_name = 'acciones'")

    cur.execute("SELECT * FROM acciones") 
    row = cur.fetchall()
    nom=['empleadoID', 'Fecha', 'Accion Otorgada', 'Observaciones']
    acciones_disciplinarias=[]
    for j in range(0, len(row)):
        accion={}
        r=row[j]
        for i in range(0, len(nom)):
            accion.update({nom[i]:r[i]})
        acciones_disciplinarias.append(accion)

        
##ACTUALIZAR DATOS

def actualizarEmpleado():
    emp=[]
    emp.append(input("INGRESE EMPLEADO ID "))
    emp.append(input("INGRESE NOMBRE "))
    emp.append(input("INGRESE APELLIDO "))
    emp.append(input("INGRESE DIRECCION "))
    emp.append(input("INGRESE TELEFONO "))
    emp.append(input("INGRESE CORREO "))
    emp.append(input("INGRESE FECHA DE CONTRATACION "))
    emp.append(input("INGRESE EDAD "))
    emp.append(input("INGRESE DPI "))
    emp.append(input("INGRESE SEXO "))
    emp.append(input("INGRESE PUESTO "))
    emp.append(input("INGRESE TIPO DE EMPLEADO "))
    emp.append(input("INGRESE SALARIO "))

    
    query = """ UPDATE empleados
                SET (nombre, apellido, direccion, telefono, correo, fecha_contratacion, edad, dpi, sexo, puesto, tipo_empleado, salario)=(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                WHERE empleadoID = %s
                """
    data = (emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10], emp[11], emp[12], emp[0])
    
    cur.execute(query, data)
    conn.commit()
