import pygame, constantes as const 
from funciones import menu_principal
from puntajes import *

def correr_juego(dimension_ventana:tuple)->None:
    """
    Corre el juego
    Recibe: dimension_ventana (tuple) con el tamaño de la ventana principal
    """
    pygame.init()
    pygame.mixer.init()
    caption = pygame.image.load(const.CAPTION)
    pygame.display.set_icon(caption)
    pantalla = pygame.display.set_mode(dimension_ventana)

    juego_corriendo = True
    pantalla_menu = True
    pantalla_jugar = False
    pantalla_puntajes = False
    pantalla_actual = ""

    while juego_corriendo == True:
        posicion_mouse = pygame.mouse.get_pos()
        lista_eventos = pygame.event.get()
        boton_mouse_presionado = pygame.mouse.get_pressed()

        if pantalla_menu == True:
            pantalla.fill(const.NEGRO)
            menu_principal.iniciar_musica(const.MUSICA_MENU_PRINCIPAL)
            pygame.display.set_caption(const.TITULO_MENU)
            menu_principal.dibujar_fondo(pantalla, const.FONDO_MENU_PRINCIPAL)
            titulo = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "MENU PRINCIPAL", const.AZUL_MENU, 400, 80, 20, 20, 4)
            boton_jugar = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "JUGAR", const.AZUL_MENU, 400, 200, 15, 15, 3, const.AZUL_CLARO)
            boton_puntajes = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "PUNTAJES", const.AZUL_MENU, 400, 300, 15, 15, 3, const.AZUL_CLARO)
            boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 400, 400, 15, 15, 3, const.AZUL_CLARO)
            pantalla_menu = False
            pantalla_actual = "menu"
        
        if pantalla_jugar == True:
            pantalla.fill(const.GRIS_CLARO)
            menu_principal.iniciar_musica(const.MUSICA_JUGAR)
            pygame.display.set_caption(const.TITULO_JUGAR)
            menu_principal.dibujar_fondo(pantalla, const.FONDO_JUGAR)
            
            boton_volver = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "VOLVER", const.AZUL_MENU, 690, 450, 15, 15, 3, const.AZUL_CLARO)
            boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 700, 550, 15, 15, 3, const.AZUL_CLARO)
            
            pantalla_jugar = False
            pantalla_actual = "jugar"
        
        if pantalla_puntajes == True:
            pantalla.fill(const.GRIS_CLARO)
            menu_principal.iniciar_musica(const.MUSICA_PUNTAJE)
            pygame.display.set_caption(const.TITULO_PUNTAJE)
            menu_principal.dibujar_fondo(pantalla, const.FONDO_PUNTAJES)

            boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 600, 550, 15, 15, 3, const.AZUL_CLARO)
            boton_volver = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "VOLVER", const.AZUL_MENU, 200, 550, 15, 15, 3, const.AZUL_CLARO)
            mostrar_puntajes(lista_jugadores, pantalla)

            pantalla_puntajes = False
            pantalla_actual = "puntajes"
        
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and boton_mouse_presionado[0] == True:
                if boton_salir.collidepoint(posicion_mouse):
                    juego_corriendo = False
                
                if boton_jugar.collidepoint(posicion_mouse):
                    pantalla_menu = False
                    pantalla_jugar = True
                
                if boton_puntajes.collidepoint(posicion_mouse):
                    pantalla_menu = False
                    pantalla_puntajes = True
                
                if pantalla_actual == "jugar":
                    if boton_volver.collidepoint(posicion_mouse):
                        pantalla_menu = True
                        pantalla_jugar = False
                
                if pantalla_actual == "puntajes":
                    if boton_volver.collidepoint(posicion_mouse):
                        pantalla_menu = True
                        pantalla_puntajes = False
                
            
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            
            
        pygame.display.flip()

correr_juego(const.DIMENSION_VENTANA)
