import mysql.connector
from mysql.connector import Error
import pandas as pandas

#--Conectar ao MySql Server--#
def create_server_connection(host, user, psw, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            passwd = psw,
            database = db
        )
        print("Conectado com sucesso!! yeyy \o/")
    except Error as err:
        print(f"Erro: '{err}'")
    return connection

#--Executando a conexão--#
connection = create_server_connection("localhost", "root", "toor", "")




#--Executar Query--#
def execute_query(connection, query):
    cursor = connection.cursor
    try:
        cursor.execute_query(query)
        connection.commit()
        print('Query executada!')
    except Error as err:
        print(f"Erro: '{err}'")

#--Executar Query--#
#   query = """
#   multiplas linhas
#   """
#   execute_query(connection, query)

#-Query Leitura-#
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#-Apresentar leitura-#
#q1 = """
#SELECT *
#FROM teacher;
#"""
#connection = create_db_connection("localhost", "root", pw, db)
#results = read_query(connection, q1)
#for result in results:
#  print(result)




#-Usando Listas-#
# sql = '''
#    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
#    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#    ''' 
#val = [
#    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
#    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
#]
