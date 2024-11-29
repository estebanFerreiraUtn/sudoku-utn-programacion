import pygame

def dibujar_boton(pantalla: pygame.Surface, tipografia: str|None, tamanio_letra: int, texto_boton: str, color_principal: tuple, eje_x: int, eje_y: int, incremento_x: int, incremento_y: int, grosor_borde: int, color_fondo: tuple|None = None)->None:
    """
    Dibuja un botón en pantalla\n
    Recibe:\n
        pantalla (pygame:Surface) en la que se dibujará el botón\n
        tipografia (str|None) con la ubicación o None para el default de Pygame\n
        tamanio_letra (int) a imprimir\n
        texto_boton (str) descriptivo de la función del botón\n
        color_principal (tuple) del texto y borde en RGB\n
        eje_x (int) ubicación del botón en el eje x de la pantalla\n
        eje_y (int) ubicación del botón en el eje y de la pantalla\n
        incremento_x (int) respecto al texto, para el borde\n
        incremento_y (int) respecto al texto, para el borde\n
        grosor_borde (int) del recuadro del botón\n
        color_de_fondo (tuple|None) por default None (sin color)\n
    Retorna:\n
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

def iniciar_musica(ubicacion_archivo: str, volumen_inicial: float = 0.1)->None:
    """
    Inicia la música de una pantalla\n
        Recibe: ubicacion_archivo(str) de música\n
                volumen_inicial (float) entre 0 - 1, 0.1 por default
    """
    pygame.mixer.music.load(ubicacion_archivo)
    pygame.mixer.music.set_volume(volumen_inicial)
    pygame.mixer.music.play(-1)

def dibujar_fondo(pantalla: pygame.Surface, ubicacion_imagen: str, eje_x: int, eje_y: int)->None:
    """
    Dibuja el fondo de pantalla\n
    Recibe: pantalla (pygame.Surface) en la cual dibujar\n
            ubicacion_imagen (str) a dibujar\n
            eje_x (int) ubicación del fondo en el eje x de la pantalla\n
            eje_y (int) ubicación del fondo en el eje y de la pantalla
    """
    fondo = pygame.image.load(ubicacion_imagen)
    pantalla.blit(fondo, (eje_x, eje_y))

def determinar_coeficiente_segun_dificultad(dificultad:str)->int:
    """
    Esta función se encarga de asignar un coeficiente para el puntaje del jugador de acuerdo al nivel de dificultad del juego.
    Recibe:
        dificultad(str): es un string que representa al nivel de dificultad del juego.
    Retorna:
        coeficiente_segun_dificultad (int): es un número entero que representa a un coeficiente con el que se multiplicará el puntaje del jugador teniendo en cuenta la dificultad elegida para el sudoku (1 para fácil, 1,5 para intermedio, 2 para díficil).
    """
    match dificultad:
        case "facil":
            coeficiente_segun_dificultad = 1
        case "intermedio":
            coeficiente_segun_dificultad = 1.5
        case "dificil":
            coeficiente_segun_dificultad = 2
    
    return coeficiente_segun_dificultad

def calcular_puntaje(minutos_transcurridos:int, cantidad_errores:int,  dificultad_sudoku:str="facil", puntaje_base:int=1000, penalizacion_por_error:int=50, penalizacion_por_minuto:int=10)->int:
    """
    Esta función se encarga de calcular el puntaje de un jugador al terminar la partida del sudoku.
    Recibe:
        minutos_transcurridos (int): es un número entero que representa la cantidad de minutos transcurridos desde que se inicio el juego.
        cantidad_errores (int): es un número entero que representa la cantidad de errores cometidos por el jugador.
        puntaje_base (int): es un número entero que representa el puntaje que tiene el jugador al iniciar el juego.
        penalizacion_por_error (int): es un número entero que representa el puntaje que se resta al jugador por cada error cometido.
        penalizacion_por_minuto (int): es un número entero que representa el puntaje que se resta al jugador por cada minuto transcurrido luego de haber iniciado el juego.
        dificultad(str): es un string que representa al nivel de dificultad del juego.
    Retorna:
        resultado (int): es un número entero que representa el puntaje final del jugador al terminar el juego.
    """
    resultado = (puntaje_base - (cantidad_errores * penalizacion_por_error) - (minutos_transcurridos * penalizacion_por_minuto)) * determinar_coeficiente_segun_dificultad(dificultad_sudoku)

    return resultado