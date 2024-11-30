# FORMA DE IMPRIMIR LOS PUNTAJES EN PANTALLA:
import pygame
from constantes import *
import json


def parsear_json(nombre_archivo:str)->list[dict]:
    """
    Esta función se encarga de generar una lista de diccionarios a partir de un archivo json.
    Recibe como parametros:
        nombre_archivo (str): un string que representa la ruta en que se encuentra el archivo json.
    Retorna:
        lista_elementos (list[dict]): una lista que representa la lista de diccionarios.
    """
    try:
        with open(nombre_archivo, "r") as archivo:
            lista_elementos = json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        lista_elementos = []  # Retornar una lista vacía en caso de error
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' no contiene un JSON válido.")
        lista_elementos = []  # Retornar una lista vacía en caso de error
    
    return lista_elementos

def ordenar_lista_puntajes(lista_puntajes:list[dict])->list:
    """
    Esta función se encarga de ordenar de forma descendente los puntajes de una lista de diccionarios.
    Recibe:
        lista_puntajes (list[dict]): es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
    Retorna:
    """
    bandera = False
    for i in range(len(lista_puntajes) - 1):
        for j in range(i + 1, len(lista_puntajes)):
            if lista_puntajes[i]["puntaje"] < lista_puntajes[j]["puntaje"]:
                aux = lista_puntajes[i]
                lista_puntajes[i] = lista_puntajes[j]
                lista_puntajes[j] = aux
                bandera = True
    return bandera

def obtener_top_cinco(lista_puntajes:list[dict])->list[dict]:
    """
    Esta función se encarga de recortar la lista de puntajes para obtener los cinco puntajes más altos.
    Recibe:
        lista_puntajes (list[dict]): es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
    Retorna:
        lista_top_cinco (list[dict]): es una lista de diccionarios con los jugadores con los cinco mejores puntajes ordenados de mayor a menor
    """
    return lista_puntajes[:5]


lista_jugadores = parsear_json("puntajes_sudoku.json") # Obtengo los datos de los jugadores a partir del archivo json

print(lista_jugadores)

ordenar_lista_puntajes(lista_jugadores) # Ordeno la lista de jugadores descendentemente de acuerdo a su puntaje

lista_jugadores_top_cinco = obtener_top_cinco(lista_jugadores) # Me quedo con los cinco jugadores con mejor puntaje



# Función para dibujar el texto sin usar enumerate
def mostrar_puntajes(jugadores:list, ventana:pygame.Surface):
    """
    Esta función se encarga de mostrar la lista de jugadores con sus respectivos puntajes.
    Esta función recibe:

    """
    fuente = pygame.font.SysFont("Rockwell", 32)  # Fuente y tamaño
    # Dibujar el fondo
    # ventana.blit(fondo, (0, 0))
    
    # Mostramos los datos de los jugadores
    cabecera = "Top 10 mejores puntajes sudoku"
    cabecera_renderizada = fuente.render(cabecera, True, AZUL)
    ventana.blit(cabecera_renderizada, (170, 50))

    # Donde va a empezar la posicion x, y
    posicion_x = 50 
    posicion_y = 90  

    for i in range(len(jugadores)):
        texto = f"{i + 1} _ {jugadores[i]['nombre']}: {jugadores[i]['puntaje']}"
        texto_renderizado = fuente.render(texto, True, AZUL) 
        ventana.blit(texto_renderizado, (250, posicion_y))  # Dibuja el texto en la posicion (50, posicion_y)
        
        # Actualiza la posicion en el eje Y para el siguiente jugador
        posicion_y += 40  # Aumenta la posicion en 40 píxeles


