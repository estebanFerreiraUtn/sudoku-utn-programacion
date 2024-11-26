import pygame

def dibujar_boton(pantalla: pygame.Surface, tipografia: str, tamanio_letra: int, texto_boton: str, color_principal: tuple, eje_x: int, eje_y: int, incremento_x: int, incremento_y: int, grosor_borde: int, color_fondo: tuple|None = None)->None:
    """
    Dibuja un botón en pantalla
    Recibe:
        pantalla (pygame:Surface) en la que se dibujará el botón
        tipografia (str) del texto
        tamanio_letra (int) a imprimir
        texto_boton (str) descriptivo de la función del botón
        color_principal (tuple) del texto y borde en RGB
        eje_x (int) ubicación del botón en el eje x de la pantalla
        eje_y (int) ubicación del botón en el eje y de la pantalla
        incremento_x (int) respecto al texto, para el borde
        incremento_y (int) respecto al texto, para el borde
        grosor_borde (int) del recuadro del botón
        color_de_fondo (tuple|None) por default None (sin color)
    Retorna:
        borde (pygame.rect.Rect) para interactuar en eventos
    """

    #Crea el texto
    fuente = pygame.font.Font(tipografia, (tamanio_letra))
    texto = fuente.render(texto_boton, True, color_principal, color_fondo)
    rectangulo_texto = texto.get_rect(center=(eje_x, eje_y))

    #Crea el rectángulo del botón
    borde = rectangulo_texto.inflate(incremento_x, incremento_y)

    #Agrega el fondo
    if color_fondo != None:
        pygame.draw.rect(pantalla, color_fondo, borde)
    
    #Dibuja el borde
    pygame.draw.rect(pantalla, color_principal, borde, grosor_borde)
    pantalla.blit(texto, rectangulo_texto.topleft)

    return borde

def iniciar_musica(ubicacion_archivo: str, volumen_inicial: float = 0.1):
    """
    Inicia la música de una pantalla
        Recibe: ubicacion_archivo(str) de música
                volumen_inicial (float) entre 0 - 1, 0.1 por default
    """
    pygame.mixer.music.load(ubicacion_archivo)
    pygame.mixer.music.set_volume(volumen_inicial)
    pygame.mixer.music.play(-1)

def dibujar_fondo(pantalla: pygame.Surface, ubicacion_imagen: str):
    """
    Dibuja el fondo de pantalla
        Recibe: pantalla (pygame.Surface) en la cual dibujar
        ubicacion_imagen (str) a dibujar
    """
    fondo = pygame.image.load(ubicacion_imagen)
    pantalla.blit(fondo, (0, 0))