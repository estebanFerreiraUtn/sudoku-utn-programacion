import pygame, constantes as const

pygame.init()

def correr_juego(dimension_ventana:tuple) -> None:
    """
    Muestra la ventana del menu principal del juego.
    """

    pantalla = pygame.display.set_mode(dimension_ventana)

    juego_corriendo = True
    while juego_corriendo == True:
        pygame.display.set_caption(const.TITULO_JUEGO)
        fondo_menu_principal = pygame.image.load(const.FONDO_MENU_PRINCIPAL)
        pantalla.blit(fondo_menu_principal, (0, 0))
        texto_menu = pygame.font.Font(const.LETRA_MENU_PRINCIPAL, (30)).render("MENU PRINCIPAL", True, "#0000b3")
        rectangulo_menu = texto_menu.get_rect(center=(400, 70))
        borde_rectangulo_menu = pygame.draw.rect(pantalla, "#0000b3", rectangulo_menu, 4)
        texto_boton_jugar = pygame.font.Font(const.LETRA_MENU_PRINCIPAL, (30)).render("JUGAR", True, "#0000b3")
        rectangulo_boton_jugar = texto_boton_jugar.get_rect(center=(250, 191))
        
        print(rectangulo_menu)
        pantalla.blit(texto_menu, rectangulo_menu)
        pantalla.blit(texto_boton_jugar, rectangulo_boton_jugar)
        posicion_mouse = pygame.mouse.get_pos()
        print(posicion_mouse)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            
            #Si recibe parámetros, actualiza solo esa parte. Sin parámetros actualiza todo
        pygame.display.flip() #actualiza todo
    
def mostrar_opciones():
    #pantalla.fill(const.GRIS)
    pass
    
correr_juego(const.DIMENSION_VENTANA)
