""" Funciones de ayuda """
import os
import platform

def clear():
    """ Metodo para limpiar  """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')