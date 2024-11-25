import pygame
from constantes import *
import json

pygame.init()

fondo_puntuaciones = pygame.image.load("imagenes/fondo_puntuaciones.png")

boton_volver = {"superficie":pygame.image.load("Botón_desde_opciones_a_menu.png"),"rectangulo":pygame.Rect(0,0,0,0)}

fuente = pygame.font.SysFont("Times New Roman",30)
fuente_boton = pygame.font.SysFont("Arial",23)

def parsear_json(nombre_archivo: str)->list:
    """
    Esta función se encarga de generar una lista de diccionarios a partir de un archivo json.
    Recibe como parametros:
        nombre_archivo: un string que representa la ruta en que se encuentra el archivo json.
    Retorna:
        lista_elementos: una lista que representa la lista de diccionarios.
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


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def ordenar_lista_puntajes(lista_puntajes:list)->list:
    """
    Esta función se encarga de ordenar de forma descendente los puntajes de una lista de diccionarios.
    Recibe:
        lista_puntajes: es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
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
        lista_puntajes: es una lista de diccionarios que representa a los jugadores del sudoku con sus respectivos puntajes.
    Retorna:
        lista_top_cinco: es una lista de diccionarios con los jugadores con los cinco mejores puntajes ordenados de mayor a menor
    """
    return lista_puntajes[:5]


def mostrar_puntuaciones(pantalla:pygame.Surface,eventos):

    retorno = "puntuaciones"
    
    # for evento in eventos:
    #     if evento.type == pygame.MOUSEBUTTONDOWN:
    #         if boton_volver['rectangulo'].collidepoint(evento.pos):
    #             # click_sonido.play()
    #             retorno = "menu"
    #     elif evento.type == pygame.QUIT:
    #         retorno = "salir"
            
    pantalla.blit(fondo_puntuaciones,(0,0))

    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(5,5))
      
    lista_ordenada = lista_jugadores
    contador = 0
    posicionY = 0
    for lista in lista_ordenada:
         contador += 1
         posicionY += 45
         blit_text(pantalla,f"{contador} {lista["nombre"]} - {lista["puntaje"]} puntos",(10,posicionY),fuente,AZUL) 
    
    # return retorno




# Código para probar el menu puntajes:

# lista_jugadores = parsear_json("puntajes_sudoku.json")
# print(lista_jugadores)

# print(ordenar_lista_puntajes(lista_jugadores))

# print(lista_jugadores)

# print(obtener_top_cinco(lista_jugadores))
    

# PANTALLA = (800,600)
# pygame.init()
# pantalla = pygame.display.set_mode(PANTALLA) #Se crea una ventana
# pygame.display.set_caption("Preguntados")

# corriendo = True

# while corriendo == True:
#     mostrar_puntuaciones(pantalla,pygame.event.get())

#     pygame.display.flip()

# pygame.quit()