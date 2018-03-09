def concatenar(tabla, *datos):
    lista = list(str(datos))
    text = "INSERT INTO " + tabla + " VALUES "
    for i in lista:
        text += i
    return text
        

def insert(conn, tabla, *datos):
    conn.execute(concatenar(tabla, *datos))
