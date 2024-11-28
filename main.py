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

    evento_ticks_1 = pygame.USEREVENT + 1 #Creo evento personalizado para el timer
    tiempo_milisegundos = 1000
    pygame.time.set_timer(evento_ticks_1, tiempo_milisegundos)
    tiempo_transcurrido = 0

    juego_corriendo = True
    pantalla_menu = True
    pantalla_jugar = False
    pantalla_puntajes = False
    pantalla_configuraciones = False # Nuevo menu para elegir dificultad del juego
    dificultad = "facil" # Inicializo la dificultad en fácil

    pantalla_actual = ""
    
    while juego_corriendo == True:
        posicion_mouse = pygame.mouse.get_pos()
        lista_eventos = pygame.event.get()
        boton_mouse_presionado = pygame.mouse.get_pressed()

        if pantalla_menu == True:
            pantalla.fill(const.NEGRO)
            menu_principal.iniciar_musica(const.MUSICA_MENU_PRINCIPAL)
            pygame.display.set_caption(const.TITULO_MENU)
            menu_principal.dibujar_fondo(pantalla, const.FONDO_MENU_PRINCIPAL, 0, 0)
            titulo = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "MENU PRINCIPAL", const.AZUL_MENU, 400, 80, 20, 20, 4)
            boton_jugar = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "JUGAR", const.AZUL_MENU, 400, 200, 15, 15, 3, const.AZUL_CLARO)
            boton_puntajes = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "PUNTAJES", const.AZUL_MENU, 400, 300, 15, 15, 3, const.AZUL_CLARO)
            boton_configuraciones = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "CONFIGURACIONES", const.AZUL_MENU, 400, 400, 15, 15, 3, const.AZUL_CLARO)
            boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 400, 500, 15, 15, 3, const.AZUL_CLARO) # Botón salir con la posición cambiada hacia abajo
            # boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 400, 400, 15, 15, 3, const.AZUL_CLARO) # Botón salir original
            pantalla_menu = False
            pantalla_actual = "menu"
        
        if pantalla_jugar == True:
            pantalla.fill(const.GRIS_CLARO)
            menu_principal.iniciar_musica(const.MUSICA_JUGAR)
            pygame.display.set_caption(const.TITULO_JUGAR)
            menu_principal.dibujar_fondo(pantalla, const.FONDO_JUGAR, 0, 0)
            
            boton_reiniciar_partida = menu_principal.dibujar_boton(pantalla, const.LETRA, 15, "REINICIAR PARTIDA", const.AZUL_MENU, 650, 350, 15, 15, 3, const.GRIS_CLARO) # Nuevo botón para reiniciar el la partida
            boton_volver = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "VOLVER", const.AZUL_MENU, 690, 450, 15, 15, 3, const.AZUL_CLARO)
            boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 700, 550, 15, 15, 3, const.AZUL_CLARO)

            pantalla_jugar = False
            pantalla_actual = "jugar"
        
        if pantalla_puntajes == True:
            pantalla.fill(const.GRIS_CLARO)
            menu_principal.iniciar_musica(const.MUSICA_PUNTAJE)
            pygame.display.set_caption(const.TITULO_PUNTAJE)
            menu_principal.dibujar_fondo(pantalla, const.FONDO_PUNTAJES, 0, 0)

            boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 600, 550, 15, 15, 3, const.AZUL_CLARO)
            boton_volver = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "VOLVER", const.AZUL_MENU, 200, 550, 15, 15, 3, const.AZUL_CLARO)
            mostrar_puntajes(lista_jugadores_top_cinco, pantalla)

            pantalla_puntajes = False
            pantalla_actual = "puntajes"
        
        if pantalla_configuraciones == True: # Nuevo menu configuraciones
            pantalla.fill(const.GRIS_CLARO)
            # Faltaría música
            pygame.display.set_caption(const.TITULO_CONFIGURACIONES)
            menu_principal.dibujar_fondo(pantalla, const.FONDO_CONFIGURACIONES, 0, 0) # Cambiar fondo
            titulo_configuraciones = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "CONFIGURACIONES", const.AZUL_MENU, 400, 80, 20, 20, 4)
            
            cabecera_elegir_dificultad = menu_principal.dibujar_boton(pantalla, const.LETRA, 20, "Elija el nivel de dificultad", const.AZUL_MENU, 400, 170, 20, 20, 4, const.AZUL_CLARO)
            boton_dificultad_facil = menu_principal.dibujar_boton(pantalla, const.LETRA, 15, "Fácil", const.AZUL_MENU, 400, 220, 20, 20, 4, const.GRIS_CLARO)
            boton_dificultad_intermedio = menu_principal.dibujar_boton(pantalla, const.LETRA, 15, "Intermedio", const.AZUL_MENU, 400, 260, 20, 20, 4, const.GRIS_CLARO)
            boton_dificultad_dificil = menu_principal.dibujar_boton(pantalla, const.LETRA, 15, "Díficil", const.AZUL_MENU, 400, 300, 20, 20, 4, const.GRIS_CLARO)

            boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "SALIR", const.AZUL_MENU, 600, 550, 15, 15, 3, const.AZUL_CLARO)
            boton_volver = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "VOLVER", const.AZUL_MENU, 200, 550, 15, 15, 3, const.AZUL_CLARO)

            pantalla_configuraciones = False
            pantalla_actual = "configuraciones"
            
        
        for evento in lista_eventos:
            if pantalla_actual == "jugar":
                if evento.type == evento_ticks_1:
                    tiempo_transcurrido += 1000
                    minutos = tiempo_transcurrido // 60000  # Convertir milisegundos a minutos
                    segundos = (tiempo_transcurrido // 1000) % 60  # Convertir milisegundos a segundos
                    texto_cronometro = pygame.font.Font(None, 30).render(f"{minutos:02}:{segundos:02}", True, (0, 0, 0))  # Texto en negro
                    cuadrado_texto_cronometro = texto_cronometro.get_rect(topleft=(600,50))
                    pantalla.fill((255, 255 ,255), cuadrado_texto_cronometro)
                    pantalla.blit(texto_cronometro, (600, 50))

            if evento.type == pygame.MOUSEBUTTONDOWN and boton_mouse_presionado[0] == True:
                if boton_salir.collidepoint(posicion_mouse):
                    juego_corriendo = False
                
                if pantalla_actual == "menu":

                    if boton_jugar.collidepoint(posicion_mouse):
                        pantalla_jugar = True
                    
                    if boton_puntajes.collidepoint(posicion_mouse):
                        pantalla_puntajes = True
                    
                    if boton_configuraciones.collidepoint(posicion_mouse):
                        pantalla_configuraciones = True
                
                if pantalla_actual == "jugar":
                    if boton_reiniciar_partida.collidepoint(posicion_mouse):
                        pantalla_jugar = True
                        tiempo_transcurrido = 0
                    
                    if boton_volver.collidepoint(posicion_mouse):
                        pantalla_menu = True
                
                if pantalla_actual == "puntajes":
                    if boton_volver.collidepoint(posicion_mouse):
                        pantalla_menu = True
                
                if pantalla_actual == "configuraciones": # Nuevo menu configuraciones
                    if boton_volver.collidepoint(posicion_mouse):
                        pantalla_menu = True
                    
                    if boton_dificultad_facil.collidepoint(posicion_mouse):
                        dificultad = "facil"
                        print(dificultad) # Solo para verificar
                    
                    if boton_dificultad_intermedio.collidepoint(posicion_mouse):
                        dificultad = "intermedio"
                        print(dificultad) # Solo para verificar
                    
                    if boton_dificultad_dificil.collidepoint(posicion_mouse):
                        dificultad = "dificil"
                        print(dificultad) # Solo para verificar

            if evento.type == pygame.QUIT:
                juego_corriendo = False


        pygame.display.flip()

correr_juego(const.DIMENSION_VENTANA)
