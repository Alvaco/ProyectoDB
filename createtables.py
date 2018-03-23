import psycopg2
import config
import sys

con = None

conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")
print ("CONEXION EXITOSA")


c = conn.cursor()

c.execute('''

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


c. execute('''
    CREATE TABLE IF NOT EXISTS vehiculos (
    vehiculoID INT NOT NULL,
    placa VARCHAR(50),
    modelo VARCHAR(50),
    marca VARCHAR(50),
    año VARCHAR(50),
    color VARCHAR(50),
    PRIMARY KEY (vehiculoID)
    );
    ''')
print ("TABLA vehiculos CREADA")


c.execute('''
    CREATE TABLE  IF NOT EXISTS vehiculos_asignados (
    vehiculoID INT,
    empleadoID INT,
    dia_semana VARCHAR(50),
    FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID),
    FOREIGN KEY (vehiculoID) REFERENCES vehiculos(vehiculoID)
    );
    ''')
print ("TABLA vehiculos_asignados CREADA")


c.execute('''
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


c.execute('''
    CREATE TABLE IF NOT EXISTS capacitaciones (
    empleadoID INT,
    fecha_capacitacion DATE,
    capacitacion VARCHAR(50),
    calificacion FLOAT(50),
    FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
    );
    ''')
print ("TABLA capacitaciones CREADA")


c.execute('''
    CREATE TABLE IF NOT EXISTS acciones (
    empleadoID INT,
    fecha_accion DATE,
    accion_otorgada VARCHAR(50),
    explicacion VARCHAR(100),
    FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
    );
    ''')
print ("TABLA acciones CREADA")


c.execute('''
    CREATE TABLE IF NOT EXISTS administrativos (
    empleadoID INT,
    oficina VARCHAR(50),
    tel_oficina VARCHAR(50),
    FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
    );
    ''')
print ("TABLA administrativos CREADA")


c.execute('''
    CREATE TABLE IF NOT EXISTS operativos (
    empleadoID INT,
    tipo_licencia VARCHAR(10),
    uso_lentes VARCHAR(50),
    FOREIGN KEY (empleadoID) REFERENCES empleados(empleadoID)
    );
    ''')
print ("TABLA operativos CREADA")
