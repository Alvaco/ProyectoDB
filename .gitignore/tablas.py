%%sql 


# TABLA EMPLEADOS
CREATE TABLE empleados (
    empleadoID INT NOT NULL,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    direccion VARCHAR(50),
    telefono VARCHAR(50),
    correo VARCHAR(50),
    fecha_contratacion DATE,
    edad INT(50),
    dpi INT(50),
    sexo CHAR(10),
    puesto VARCHAR(50),
    tipo_empleado VARCHAR(50),
    salario FLOAT(50),
    PRIMARY KEY (empleadoID),
);


# VEHICULOS
CREATE TABLE vehiculos (
    vehiculoID INT NOT NULL,
    placa VARCHAR(50),
    modelo VARCHAR(50),
    marca VARCHAR(50),
    año VARCHAR(50),
    color VARCHAR(50),
    PRIMARY KEY (vehiculoID),
);


# VEHICULOS ASIGNADOS
CREATE TABLE vehiculos_asignados (
    vehiculoID INT,
    empleadoID INT,
    dia_semana VARCHAR(50),
    FOREIGN KEY (empleadoID) REFERENCES epleados(empleadoID),
    FOREIGN KEY (vehiculoID) REFERENCES vehiculos(vehiculoID),
);


# HISTORIAL
CREATE TABLE historial (
    empleadoID INT,
    puestoID INT NOT NULL,
    fecha_puesto DATE,
    salario FLOAT(50),
    PRIMARY KEY (puestoID),
    FOREIGN KEY (empleadoID) REFERENCES epleados(empleadoID),
);


# CAPACITACIONES
CREATE TABLE capacitaciones (
    empleadoID INT,
    fecha_capacitacion DATE,
    capacitacion VARCHAR(50),
    calificacion FLOAT(50),
    FOREIGN KEY (empleadoID) REFERENCES epleados(empleadoID),
);


# ACCIONES DISCIPLINARIAS
CREATE TABLE acciones (
    empleadoID INT,
    fecha_accion DATE,
    accion_otorgada VARCHAR(50),
    explicacion VARCHAR(100),
    FOREIGN KEY (empleadoID) REFERENCES epleados(empleadoID),
);


# ADMINISTRATIVOS
CREATE TABLE administrativos (
    empleadoID INT,
    oficina VARCHAR(50),
    tel_oficina VARCHAR(50),
    FOREIGN KEY (empleadoID) REFERENCES epleados(empleadoID),
);


# OPERATIVOS
CREATE TABLE operativos (
    empleadoID INT,
    tipo_licencia VARCHAR(10),
    uso_lentes VARCHAR(50),
    FOREIGN KEY (empleadoID) REFERENCES epleados(empleadoID),
);
