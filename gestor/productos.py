""" administrador de productos"""
from db.conexion_oracle import connection

def listarProductos():
    """Funcion para obtener de la base de datos la lista de productos"""
    cursor=connection.cursor()
    cursor.execute("""select p.NAME as Nombre_Producto, 
                    p.PRICE as Precio,
                    b.STORE as Tienda,
                    case when b.full=1 then 'SI' else 'NO' end as Llega_gratis_hoy,
                    b.QUANTITY_AVAILABLE as Cantidad_disponibles,
                    h.PDP_SIZE as Tamaño_de_la_pantalla,
                    h.INTERNAL_MEMORY as Memoria_interna
                    from products p
                    inner join buybox b on b.id_Products_fk=p.id
                    inner join HIGHLIGHTED_SPECS h on h.id_Products_fk=p.id
    """)

    rows=cursor.fetchall()

    for row in rows:
        print(row)
        

def insertarProductos(item):
    """Funcion para insertar en la base de datos la lista de productos"""
    cursor=connection.cursor()
    id = str(item['id'])
    cursor.execute("insert into products(id,name,price) values(" + id  +",'" + item['name']  +"','" + item['price']  +"')") 
    cursor.execute("insert into buybox(id_products_fk,STORE, FULL,QUANTITY_AVAILABLE) values(" + id + ",'" + item['store'] + "',1,'" + item['quantity'] + "')")  
    cursor.execute("insert into HIGHLIGHTED_SPECS(PDP_SIZE,INTERNAL_MEMORY,id_products_fk) values('" + item['size']  +"','" + item['memory']  +"'," + id  +")")
    connection.commit()
    
    cursor.close()


    print("Productos insertados correctamente")






