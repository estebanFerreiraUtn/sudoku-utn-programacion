# FORMA DE IMPRIMIR LOS PUNTAJES EN PANTALLA:
import pygame
from constantes import *
import json

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Puntajes Sudoku')

# Cargar la imagen de fondo
fondo_puntuaciones = pygame.image.load("imagenes/fondo_seccion_puntuaciones.jpg")
fondo_puntuaciones = pygame.transform.scale(fondo_puntuaciones, (ANCHO, ALTO))  # Asegurarse de que se ajusta al tamaño de la ventana

# Configurar la fuente para mostrar el texto
fuente = pygame.font.SysFont("Rockwell", 32)  # Fuente y tamaño


def parsear_json(nombre_archivo:str)->list:
    """
    Esta función se encarga de generar una lista de diccionarios a partir de un archivo json.
    Recibe como parametros:
        nombre_archivo (str): un string que representa la ruta en que se encuentra el archivo json.
    Retorna:
        lista_elementos (str): una lista que representa la lista de diccionarios.
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

def ordenar_lista_puntajes(lista_puntajes:list)->list:
    """
    Esta función se encarga de ordenar de forma descendente los puntajes de una lista de diccionarios.
    Recibe:
        lista_puntajes (list): es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
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

def obtener_top_cinco(lista_puntajes:list)->list:
    """
    Esta función se encarga de recortar la lista de puntajes para obtener los cinco puntajes más altos.
    Recibe:
        lista_puntajes (list): es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
    Retorna:
        lista_top_cinco (list): es una lista de diccionarios con los jugadores con los cinco mejores puntajes ordenados de mayor a menor
    """
    return lista_puntajes[:5]


lista_jugadores = parsear_json("puntajes_sudoku.json") # Obtengo los datos de los jugadores a partir del archivo json

print(lista_jugadores)

ordenar_lista_puntajes(lista_jugadores) # Ordeno la lista de jugadores descendentemente de acuerdo a su puntaje

obtener_top_cinco(lista_jugadores) # Me quedo con los cinco jugadores con mejor puntaje



# Función para dibujar el texto sin usar enumerate
def mostrar_puntajes(jugadores:list, fondo:pygame.Surface):
    """
    Esta función se encarga de mostrar la lista de jugadores con sus respectivos puntajes.
    Esta función recibe:

    """
    # Dibujar el fondo
    ventana.blit(fondo, (0, 0))
    
    # Inicializar el contador para las posiciones
    posicion_y = 50  # Comienza en 50 píxeles en el eje Y

    # Mostrar los datos de los jugadores
    cabecera = "Top 10 mejores puntajes sudoku"
    cabecera_renderizada = fuente.render(cabecera, True, AZUL)
    ventana.blit(cabecera_renderizada, (170, 50))

    # Inicializar el contador para las posiciones
    posicion_y = 90  # Comienza en 90 píxeles en el eje Y

    
    for i in range(len(jugadores)):
        texto = f"{i + 1} _ {jugadores[i]['nombre']}: {jugadores[i]['puntaje']}"
        texto_renderizado = fuente.render(texto, True, AZUL)  # Color azul
        ventana.blit(texto_renderizado, (250, posicion_y))  # Dibujar el texto en la posición (50, posicion_y)
        
        # Actualizar la posición en el eje Y para el siguiente jugador
        posicion_y += 40  # Aumentar la posición Y en 40 píxeles

    # Actualizar la pantalla
    pygame.display.flip()

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Llamar a la función para mostrar los puntajes
    mostrar_puntajes(lista_jugadores, fondo_puntuaciones)

    # Limitar los FPS (opcional)
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()


##################################### TIMER EN PYGAME
# import pygame

# # Inicializar pygame
# pygame.init()

# # Definir dimensiones de la ventana
# ANCHO = 800
# ALTO = 600
# pantalla = pygame.display.set_mode((ANCHO, ALTO))
# pygame.display.set_caption("Cronómetro en Pygame")

# # Definir fuente para el cronómetro usando SysFont
# fuente = pygame.font.SysFont('Arial', 40)

# # Definir el reloj para controlar los FPS
# reloj = pygame.time.Clock()

# # Variable para controlar el tiempo
# inicio_tiempo = pygame.time.get_ticks()

# # Bucle principal del juego
# ejecutando = True
# while ejecutando:
#     # Manejo de eventos
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             ejecutando = False

#     # Calcular el tiempo transcurrido
#     tiempo_transcurrido = pygame.time.get_ticks() - inicio_tiempo  # en milisegundos
#     minutos = tiempo_transcurrido // 60000  # Convertir milisegundos a minutos
#     segundos = (tiempo_transcurrido // 1000) % 60  # Convertir milisegundos a segundos

#     # Crear el texto para mostrar el cronómetro
#     texto_cronometro = fuente.render(f"{minutos:02}:{segundos:02}", True, (0, 0, 0))  # Texto en negro

#     # Limpiar la pantalla con fondo blanco
#     pantalla.fill((255, 255, 255))  # Rellenar toda la pantalla de blanco

#     # Dibujar el cronómetro en la esquina superior derecha de la pantalla
#     pantalla.blit(texto_cronometro, (ANCHO - 190 - texto_cronometro.get_width(), 450))

#     # Actualizar la pantalla
#     pygame.display.flip()

#     # Controlar los FPS
#     reloj.tick(60)

# # Salir de pygame
# pygame.quit()