import mysql.connector

try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user='root',
        password='p@ssword',
        database='db_kasolution',
        auth_plugin='mysql_native_password'
    )

    print('comunicação feita com sucesso!!!')

except mysql.connector.Error as erro:
    print(erro)


#CRUD = (CREATE, READ, UPDATE e DELETE)

