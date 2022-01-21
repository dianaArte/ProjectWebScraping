import cx_Oracle


try:
    #se realiza conexion a la base de datos.
    connection=cx_Oracle.connect(
        user='mercadoLibre',
        password='mercadoLibre',
        dsn='localhost:1521/ORCLCDB.localdomain'
    #  ,encoding='UTF-8'
    )

    print(connection.version)

    # cursor=connection.cursor()
    # cursor.execute("select * from products")
    # rows=cursor.fetchall()

except Exception as ex:
    print(ex)



