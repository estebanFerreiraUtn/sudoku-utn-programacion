# FORMA DE IMPRIMIR LOS PUNTAJES EN PANTALLA:
import pygame
from constantes import *
import json

# Funciones para asignarle al archivo json el puntaje correspondiente

def cargar_archivo_json(ruta:str)-> list[dict]:
    """
    Esta función se encarga leer un archivo json y retornar su contenido.
    Recibe:
        ruta (str): representa a la dirección en la que se encuentra el archivo json a ser leido.
    Retorna:
        datos(list[dict]): son los datos que del archivo en forma de una lista de diccionarios.
    """
    with open(ruta, "r") as mi_archivo:
        datos = json.load(mi_archivo)
    
    return datos

def agregar_jugador_a_lista(nombre_jugador: str, puntaje: int, lista_jugadores: list[dict]) -> list[dict]:
    """
    Agrega un nuevo jugador o actualiza el puntaje máximo de un jugador existente.
    Si el nombre ya existe y el nuevo puntaje es mayor, actualiza el puntaje.
    """

    jugador_existe = False

    for jugador in lista_jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador_existe = True

            # Actualizar puntaje solo si el nuevo es mayor
            if puntaje > jugador["puntaje"]:
                jugador["puntaje"] = puntaje
            break

    # Si no se encuentra el jugador, se agrega como nuevo
    if jugador_existe == False:
        lista_jugadores.append({"nombre": nombre_jugador, "puntaje": puntaje})
    
    return lista_jugadores


def guardar_archivo_json(lista:list[dict], ruta:str)->None:
    """
    Esta función se encarga de escribirle una lista de diccionario a un archivo json. Si el archivo json no existe lo crea.
    Recibe:
        lista (list[dict]): es una lista de diccionarios que representa a la lista con los datos a guardarse en el archivo json.
        ruta (str): representa a la dirección en la que se encuentra el archivo json al cual se le escribirá la lista.
    No retorna nada.
    """
    with open(ruta, "w") as mi_archivo:
        json.dump(lista, mi_archivo, indent = 4)


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

def ordenar_lista_puntajes(lista_puntajes:list[dict])->None:
    """
    Esta función se encarga de ordenar de forma descendente los puntajes de una lista de diccionarios.
    Recibe:
        lista_puntajes (list[dict]): es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
    Retorna:
    """
    
    for i in range(len(lista_puntajes) - 1):
        for j in range(i + 1, len(lista_puntajes)):
            if lista_puntajes[i]["puntaje"] < lista_puntajes[j]["puntaje"]:
                aux = lista_puntajes[i]
                lista_puntajes[i] = lista_puntajes[j]
                lista_puntajes[j] = aux


def obtener_top_cinco(lista_puntajes:list[dict])->list[dict]:
    """
    Esta función se encarga de recortar la lista de puntajes para obtener los cinco puntajes más altos.
    Recibe:
        lista_puntajes (list[dict]): es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
    Retorna:
        lista_top_cinco (list[dict]): es una lista de diccionarios con los jugadores con los cinco mejores puntajes ordenados de mayor a menor
    """
    return lista_puntajes[:5]

# Función para dibujar el texto
def mostrar_puntajes(jugadores:list, ventana:pygame.Surface)->None:
    """
    Esta función se encarga de mostrar la lista de jugadores con sus respectivos puntajes.
    Esta función recibe:

    """
    fuente = pygame.font.SysFont("Rockwell", 32)  # Fuente y tamaño
    
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