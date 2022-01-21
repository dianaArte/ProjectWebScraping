""" Menú del programa """

import os
import helpers
import productos
from scrapy import cmdline

def loop():
    while True:

        helpers.clear()

        print("=================================================")
        print("  BIENVENIDO AL WEBSCRAPING DE MERCADO LIBRE     ")
        print("=================================================")
        print("[1] Insertar datos Web Scraping                  ")
        print("[2] Listar productos                             ")
        print("[3] Salir                                        ")
        print("=================================================")

        option = input("> ")

        helpers.clear() #limpiar

        if option == '1':
            print("Insertando datos...\n")
            cmdline.execute(['scrapy',  'runspider', '.\gestor\scrapingMercadoLibre.py'])
        if option == '2':
            print("Mostrando productos...\n")
            productos.listarProductos()
        if option == '3':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")

