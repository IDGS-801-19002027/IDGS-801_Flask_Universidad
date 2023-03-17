from db import get_connection

# MAESTROS
def insertarMaestro(nombres, apellidos, email):

    # INSERT
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL agregarMaestro(%s, %s, %s)',(nombres, apellidos, email))
        connection.commit()
        connection.close()
    
    except Exception as ex:
        print('error')

def modificarMaestro(id, nombres, apellidos, email):
    # UPDATE
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL modificarMaestro(%s, %s, %s, %s)',(id, nombres, apellidos, email))
        connection.commit()
        connection.close()
    
    except Exception as ex:
        print('error')

def consultarMaestros():
    # GETALL
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL consultaMaestros()')
            resultset=curso.fetchall()

        #for row in resultset:
            #print(row)
        connection.close()
        
    except Exception as ex:
        print('error')
    
    listaMaestros = list(resultset)
    #print(listaMaestros)
    return listaMaestros

def eliminarMaestro(id):
    # DELETE
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL eliminarMaestro(%s)',(id))
        connection.commit()
        connection.close()
    
    except Exception as ex:
        print('error')

def consultarMaestro(id):
    # GETALLBYID
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL consultaMaestro(%s)',(id))
            row = curso.fetchone()
        #resultset=curso.fetchall()
        #for row in resultset:
            #print(row[1])
        connection.close()
    
    except Exception as ex:
        print('error')

    maestro = list(row)
    #print(maestro)
    return maestro

# ALUMNOS
def insertarAlumno(nombres, apellidos, email):

    # INSERT
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL agregarAlumno(%s, %s, %s)',(nombres, apellidos, email))
        connection.commit()
        connection.close()
    
    except Exception as ex:
        print('error')

def modificarAlumno(id, nombres, apellidos, email):
    # UPDATE
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL actualizarAlumno(%s, %s, %s, %s)',(id, nombres, apellidos, email))
        connection.commit()
        connection.close()
    
    except Exception as ex:
        print('error')

def consultarAlumnos():
    # GETALL
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL consultarAlumnos()')
            resultset=curso.fetchall()

        #for row in resultset:
            #print(row)
        connection.close()
        
    except Exception as ex:
        print('error')
    
    listaAlumnos = list(resultset)
    #print(listaMaestros)
    return listaAlumnos

def eliminarAlumno(id):
    # DELETE
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL eliminarAlumno(%s)',(id))
        connection.commit()
        connection.close()
    
    except Exception as ex:
        print('error')

def consultarAlumno(id):
    # GETALLBYID
    try:
        connection=get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL consultaAlumno(%s)',(id))
            row = curso.fetchone()
        #resultset=curso.fetchall()
        #for row in resultset:
            #print(row[1])
        connection.close()
    
    except Exception as ex:
        print('error')

    alumno = list(row)
    #print(alumno)
    return alumno
