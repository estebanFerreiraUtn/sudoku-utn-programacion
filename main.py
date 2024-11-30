import copy
import pygame, constantes as const
from funciones import menu_principal
from puntajes import *
from funciones_sudoku import *

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

    evento_ticks_1 = pygame.USEREVENT + 1 # Creo evento personalizado para el timer
    tiempo_milisegundos = 1000
    pygame.time.set_timer(evento_ticks_1, tiempo_milisegundos)
    tiempo_transcurrido = 0
    contador_errores = 0

    juego_corriendo = True
    pantalla_menu = True
    sonido_ejecutandose = True
    pantalla_jugar = False
    pantalla_puntajes = False
    pantalla_configuraciones = False # Nuevo menu para elegir dificultad del juego
    dificultad = "facil" # Inicializo la dificultad en fácil

    pantalla_actual = ""
    
    # pygame.image.load(const.FONDO_SUDOKU)
    celda_selec = None
    celda_inv = None

    lista_celdas_invalidas = []
    lista_celdas_validas = []

    matriz = crear_matriz(9, 9, 0)
    llenar_matriz(matriz, const.NUMEROS_SUDOKU)
    matriz_copia = copy.deepcopy(matriz)
    ocultar_numeros_en_matriz(matriz_copia, "", dificultad)

    # mostrar_matriz(matriz)
    # print()
    # mostrar_matriz(matriz_copia)
    
    while juego_corriendo == True:
        # Obtenemos los eventos utilizados
        posicion_mouse = pygame.mouse.get_pos()
        lista_eventos = pygame.event.get()
        boton_mouse_presionado = pygame.mouse.get_pressed()


        if pantalla_menu == True:
            # pantalla.fill(const.NEGRO)

            # Musica del menu principal
            menu_principal.iniciar_musica(const.MUSICA_MENU_PRINCIPAL)
            # Titulo de la ventana menu
            pygame.display.set_caption(const.TITULO_MENU)

            # Agregamos el fondo de la ventana y dibujamos los botones con sus selecciones
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
            menu_principal.iniciar_musica(const.MUSICA_JUGAR)
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
            # pantalla.fill(const.GRIS_CLARO)

            # titulo de la ventana configuraciones
            pygame.display.set_caption(const.TITULO_CONFIGURACIONES)
            # Fondo de la ventana
            menu_principal.dibujar_fondo(pantalla, const.FONDO_CONFIGURACIONES, 0, 0)
            
            titulo_configuraciones = menu_principal.dibujar_boton(pantalla, const.LETRA, 30, "CONFIGURACIONES", const.AZUL_MENU, 400, 80, 20, 20, 4)
            
            # Dibujamos los botones con sus selecciones
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
                
                # Validamos que este la ventana de jugar si solo va sumando el tiempo cuando se este en la ventana de jugar
                if pantalla_actual == "jugar":
                    if evento.type == evento_ticks_1:
                        tiempo_transcurrido += 1000  
                
                # Titulo de la ventana jugar
                pygame.display.set_caption(const.TITULO_JUGAR)
                
                # Dibujamos el fondo y los botones de seleccion
                menu_principal.dibujar_fondo(pantalla, const.FONDO_SUDOKU, 0, 0) # Despues agregar una imagen de fondo a la ventana!!!!!
                boton_sonido = menu_principal.dibujar_boton(pantalla, const.LETRA, 20, "SONIDO ON/OFF", const.NEGRO, 620, 400, 15, 15, 3, const.CREMA)
                boton_reiniciar = menu_principal.dibujar_boton(pantalla, const.LETRA, 20, "REINICIAR", const.NEGRO, 660, 450, 15, 15, 3, const.CREMA) # Nuevo botón para reiniciar el la partida
                boton_volver = menu_principal.dibujar_boton(pantalla, const.LETRA, 20, "VOLVER", const.NEGRO, 690, 500, 15, 15, 3, const.CREMA)
                boton_salir = menu_principal.dibujar_boton(pantalla, const.LETRA, 20, "SALIR", const.NEGRO, 700, 550, 15, 15, 3, const.CREMA)
                
                # Dibujamos el tablero y los numeros del sudoku
                matriz_rectangulos = dibujar_tablero(matriz_copia, const.ANCHO_CELDA_TABLERO, const.ALTO_CELDA_TABLERO, const.INICIO_X_TABLERO, const.INICIO_Y_TABLERO, pantalla, const.NEGRO, const.GROSOR_LINEA_GRUESA, celda_selec, celda_inv)
                dibujar_numeros(matriz_copia, const.ANCHO_CELDA_TABLERO, const.ALTO_CELDA_TABLERO, const.INICIO_X_TABLERO, const.INICIO_Y_TABLERO, const.NEGRO, pantalla, const.GROSOR_NUMEROS, lista_celdas_invalidas, lista_celdas_validas)
                
                # Hacemos la formula para que nos de el tiempo en minutos y segundos
                minutos = tiempo_transcurrido // 60000  
                segundos = (tiempo_transcurrido // 1000) % 60  

                # Dibujamos el cronometro en la ventana
                recuadro_cronometro = menu_principal.dibujar_boton(pantalla, None, 30, f"Tiempo: {minutos:02}:{segundos:02}", const.NEGRO, 705, 50, 15, 15, 3, const.CREMA)
                puntaje_actual = menu_principal.calcular_puntaje(minutos, contador_errores, dificultad)
                recuadro_puntaje = menu_principal.dibujar_boton(pantalla, None, 30, f"Puntaje: {puntaje_actual:4}", const.NEGRO, 550, 50, 15, 15, 3, const.CREMA)

                # Dibujamos el rectangulo de errores
                recuadro_errores = menu_principal.dibujar_boton(pantalla, None, 30, f"Errores: {contador_errores}", const.NEGRO, 620, 90, 15, 15, 3, const.CREMA)

            # EVENTOS DE CLICKS ###
            if evento.type == pygame.MOUSEBUTTONDOWN and pantalla_actual ==  "jugar":

                # Obtenemos las cordenadas x, y del evento click
                cordenadas_click = pygame.mouse.get_pos()
                # Guardamos la celda seleccionada si se toco en el tablero con la funcion obtener_celda_seleccionada
                nueva_celda = obtener_celda_seleccionada(matriz_rectangulos, cordenadas_click)

                # Valida si se selcciono una celda adentro del tablero. si se selecciona se pinta y si se toca afuera del tablero se despinta
                if nueva_celda != None:
                    celda_selec = nueva_celda  
                else:
                    celda_selec = None  
                
            ## EVENTOS DE TECLA ###
            if evento.type == pygame.KEYDOWN and celda_selec and pantalla_actual == "jugar":
                # Obtenemos la fila y columna de la celda seleccionada (x, y)
                fila, columna = celda_selec
                print(celda_selec)
                
                # Validamos si el valor ingresado es numerico y si esta vacia la celda
                if (evento.unicode.isdigit()) and (evento.unicode != 0) and (matriz_copia[celda_selec[0]][celda_selec[1]] == ""):
                    
                    numero = int(evento.unicode)

                    # Validamos que el numero ingresado sea valido en la celda seleccionada
                    if numero == matriz[celda_selec[0]][celda_selec[1]]:
                        # Ingresamos el numero en el tablero (matriz copia) del juego
                        matriz_copia[fila][columna] = numero 
                        lista_celdas_validas.append(celda_selec)
                        print("Celda correcta")
                    else:
                        # Agregamos a una variable la celda invalida para luego usarla y poder pintar el numero de rojo
                        # celda_inv = celda_selec
                        lista_celdas_invalidas.append(celda_selec)
                        matriz_copia[fila][columna] = numero
                        contador_errores += 1
                        print(contador_errores)

                        # Si se llego a los 3 errores se reinicia la partida
                        if contador_errores == 3:
                            matriz = crear_matriz(9, 9, 0)
                            llenar_matriz(matriz, const.NUMEROS_SUDOKU)
                            matriz_copia = copy.deepcopy(matriz)
                            ocultar_numeros_en_matriz(matriz_copia, "", "intermedio")
                            matriz_copia[fila][columna] = ""
                            contador_errores = 0
                            lista_celdas_invalidas.clear()
                            celda_selec = None

                        lista_celdas_invalidas.append(celda_inv)

                if evento.key in (pygame.K_BACKSPACE, pygame.K_DELETE) and pantalla_actual == "jugar":
                    # Borra las celdas invalidas si se presiono la tecla de borrar o la de suprimir
                    if celda_selec != None: 
                        if (celda_selec in lista_celdas_invalidas) or (matriz_copia[fila][columna] != matriz[fila][columna]):
                            matriz_copia[fila][columna] = "" 
                            lista_celdas_invalidas.remove(celda_selec)

            if evento.type == pygame.MOUSEBUTTONDOWN and boton_mouse_presionado[0] == True:
                if boton_salir.collidepoint(posicion_mouse):
                    pantalla_menu = False
                
                ### PANTALLA MENU ###
                if pantalla_actual == "menu":
                    if boton_jugar.collidepoint(posicion_mouse):
                        pantalla_jugar = True
                    
                    if boton_puntajes.collidepoint(posicion_mouse):
                        pantalla_puntajes = True
                    
                    if boton_configuraciones.collidepoint(posicion_mouse):
                        pantalla_configuraciones = True
                
                ### PANTALLA JUGAR ###
                if pantalla_actual == "jugar":
                    if boton_reiniciar.collidepoint(posicion_mouse):
                        pantalla_jugar = True
                        tiempo_transcurrido = 0

                        # Reincia el contador de errores y genera una nueva matriz para el tablero de juego
                        contador_errores = 0
                        matriz = crear_matriz(9, 9, 0)
                        llenar_matriz(matriz, const.NUMEROS_SUDOKU)
                        matriz_copia = copy.deepcopy(matriz)
                        ocultar_numeros_en_matriz(matriz_copia, "", dificultad)
                        lista_celdas_invalidas.clear()
                        lista_celdas_validas.clear()
                        celda_selec = None

                    
                    if boton_volver.collidepoint(posicion_mouse):
                        pantalla_menu = True
                    
                    if boton_sonido.collidepoint(posicion_mouse):
                        if sonido_ejecutandose == True:
                            pygame.mixer.music.stop()
                            sonido_ejecutandose = False
                        else:
                            pygame.mixer.music.play(-1)
                            sonido_ejecutandose = True
                
                ### PANTALLA PUNTAJES ###
                if pantalla_actual == "puntajes":
                    if boton_volver.collidepoint(posicion_mouse):
                        pantalla_menu = True
                
                ### MENU CONFIGURACIONES ###
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

                    # Reinicia la matriz para un nuevo tablero cuando se modifique la dificultad
                    if boton_dificultad_facil.collidepoint(posicion_mouse) or boton_dificultad_intermedio.collidepoint(posicion_mouse) or boton_dificultad_dificil.collidepoint(posicion_mouse):
                        matriz = crear_matriz(9, 9, 0)
                        llenar_matriz(matriz, const.NUMEROS_SUDOKU)
                        matriz_copia = copy.deepcopy(matriz)
                        ocultar_numeros_en_matriz(matriz_copia, "", dificultad)
                        celda_selec = None
                        lista_celdas_validas.clear()
                        lista_celdas_invalidas.clear()

            if evento.type == pygame.QUIT:
                juego_corriendo = False
        
        pygame.display.flip()

correr_juego(const.DIMENSION_VENTANA)
