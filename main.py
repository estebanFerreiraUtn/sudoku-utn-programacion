import pygame, constantes as const

pygame.init()

def correr_juego(dimension_ventana:tuple)->None:
    """
    Corre el juego
    """

    pantalla = pygame.display.set_mode(dimension_ventana)

    juego_corriendo = True
    while juego_corriendo == True:
        pygame.display.set_caption(const.TITULO_MENU)
        caption = pygame.image.load(const.CAPTION)
        pygame.display.set_icon(caption)
        fondo_menu_principal = pygame.image.load(const.FONDO_MENU_PRINCIPAL)
        pantalla.blit(fondo_menu_principal, (0, 0))
        
        texto_menu = pygame.font.Font(const.LETRA_MENU_PRINCIPAL, (30)).render("MENU PRINCIPAL", True, "#0000b3")
        rectangulo_menu = texto_menu.get_rect(center=(400, 70))
        borde_rectangulo_menu = pygame.Rect.copy(rectangulo_menu)
        borde_rectangulo_menu = pygame.Rect.inflate(borde_rectangulo_menu, 20, 20)
        borde_rectangulo_menu = pygame.draw.rect(pantalla, "#0000b3", borde_rectangulo_menu, 4)
        
        texto_boton_jugar = pygame.font.Font(const.LETRA_MENU_PRINCIPAL, (30)).render("JUGAR", True, "#0000b3", "#fef5e7")
        rectangulo_boton_jugar = texto_boton_jugar.get_rect(center=(400, 200))
        borde_boton_jugar = pygame.Rect.copy(rectangulo_boton_jugar)
        borde_boton_jugar = pygame.Rect.inflate(rectangulo_boton_jugar, 15, 15)
        borde_boton_jugar = pygame.draw.rect(pantalla, "#0000b3", borde_boton_jugar, 3)
        
        texto_boton_puntajes = pygame.font.Font(const.LETRA_MENU_PRINCIPAL, (30)).render("PUNTAJES", True, "#0000b3", "#fef5e7")
        rectangulo_boton_puntajes = texto_boton_puntajes.get_rect(center=(400, 300))
        borde_boton_puntajes = pygame.Rect.copy(rectangulo_boton_puntajes)
        borde_boton_puntajes = pygame.Rect.inflate(rectangulo_boton_puntajes, 15, 15)
        borde_boton_puntajes = pygame.draw.rect(pantalla, "#0000b3", borde_boton_puntajes, 3)

        texto_boton_salir = pygame.font.Font(const.LETRA_MENU_PRINCIPAL, (30)).render("SALIR", True, "#0000b3", "#fef5e7")
        rectangulo_boton_salir = texto_boton_salir.get_rect(center=(400, 400))
        borde_boton_salir = pygame.Rect.copy(rectangulo_boton_salir)
        borde_boton_salir = pygame.Rect.inflate(rectangulo_boton_salir, 15, 15)
        borde_boton_salir = pygame.draw.rect(pantalla, "#0000b3", borde_boton_salir, 3)

        pantalla.blit(texto_menu, rectangulo_menu)
        pantalla.blit(texto_boton_jugar, rectangulo_boton_jugar)
        pantalla.blit(texto_boton_puntajes, rectangulo_boton_puntajes)
        pantalla.blit(texto_boton_salir, rectangulo_boton_salir)
        posicion_mouse = pygame.mouse.get_pos()
        #print(posicion_mouse)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            
            #Si recibe parámetros, actualiza solo esa parte. Sin parámetros actualiza todo
        pygame.display.flip() #actualiza todo
    
def pantalla_juego():
    #pantalla.fill(const.NEGRO)
    pass

def menu_opciones():
    #pantalla.fill(const.GRIS)
    pass
    
correr_juego(const.DIMENSION_VENTANA)