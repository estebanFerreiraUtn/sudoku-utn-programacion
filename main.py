import pygame, constantes as const

pygame.init()

pantalla = pygame.display.set_mode(const.DIMENSION_VENTANA)
pygame.display.set_caption(const.TITULO_JUEGO)
fondo_menu_principal = pygame.image.load("imagenes/menu_principal.png")

def menu_principal(pantalla:pygame.Surface)->None:
    """
    """
    juego_corriendo = True
    while juego_corriendo == True:
        
        pantalla.blit(fondo_menu_principal, (0, 0))
        lista_eventos = pygame.event.get()
        posicion_mouse = pygame.mouse.get_pos()
        texto_menu = pygame.font.Font("imagenes/fuente.ttf", (30)).render("MENU PRINCIPAL", True, "#0000b3")
        rectangulo_menu = texto_menu.get_rect(center=(400, 70))
        pantalla.blit(texto_menu, rectangulo_menu)

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
        
        #Si recibe parámetros, actualiza solo esa parte. Sin parámetros actualiza todo
        pygame.display.flip() #actualiza todo
    
def pantalla_juego():
    pantalla.fill(const.NEGRO)
    

def menu_opciones():
    pantalla.fill(const.GRIS)
    

menu_principal(pantalla)