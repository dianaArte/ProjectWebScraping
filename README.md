Extracción de Datos de la Web


En este repositorio van a poder encontrar el código de  Web Scraping de mercado libre

CONTENIDO
conexion_oracle : logica para realizar la conexion a la base de datos oracle
productos : Se encuentra la logica para insertar los productos extraidos de la web de mercado libre
menu : se encuentran la lista de menu de la operacion a realizar (listar, insertar y salir)
scrapingMercadoLibre: Se enceuntra la logica para realizar el webScraping y enviar los parametros a insertar


Se debe ejecutar el comando:  python .\gestor\core.py



Desafío Teórico

Consigna
Procesos, hilos y corrutinas
- Un caso en el que usarías procesos para resolver un problema y por qué.

    

- Un caso en el que usarías threads para resolver un problema y por qué.

    Cuando se debe consultar mucha informacion y evitar recursos de memoria por ejemplo al realizar el conteo
    de mucha informacion, se debe crear una funcion donde se creen varios hilos
    que deben iniciarsen ya que al momento de ejecutarse tengamos acceso a la informacion mas rapido y en procesos separados

- Un caso en el que usarías corrutinas para resolver un problema y por qué.

    Se deben insertar millones de datos y para evitar que la BD se vuelva mas len
    ta la solucion es programar tareas 
    para que realice la ejecuion en determinado tiempo donde la db no tenga peticiones

Optimización de recursos del sistema operativo

Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos
información en una API HTTP. ¿Cómo lo harías? Explicar.

Construir un  servicio implementando paginacion, enviar el objeto con la clave de la paginación el cual debe retornar
la cantidad de registros que encontro, cual es la siguiente pg y cual es la anterior.
Adicionalmente usaria la mayor cantidad de threads posibles para poder realizar la mayor cantidad de peticiones
