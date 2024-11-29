import constantes as const, os, random, pygame, biblioteca, copy
os.system("cls")

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    '''
    Función que crea un tablero (matriz) pasando por parámetro las dimensiones.

    Args:
        cantidad_filas (int): Cantidad de filas que va a tener el tablero sudoku (9x9 o 16x16)
        cantidad_columnas (int): Cantidad de columnas que va a tener el tablero sudoku (9x9 o 16x16)
        valor_inicial (any): Valores que van a tener los valores de cada posicion del tablero. 
    
    Returns:
        list: Tablero creado con las dimensiones especificadas 
    '''
    tablero = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        tablero.append(fila)
    return tablero

def validar_numero_en_matriz(matriz:list, fila:int, columna:int, numero:int) -> bool:
    '''
    Valida que el numero que se este ingresando en la matriz sea correcto respetando las reglas del sudoku.

    Args:
        matriz (list): matriz ya creada que se usara para validar.
        fila (int): numero de fila en la que ingrese el numero a validar.
        columna (int): numero de columna en la que ingrese el numero a validar.
        numero (int): numero que se ingrese para validar.
    
    Returns:
        bool: Si el numero es correcto sera True y en caso contrario False.
    '''
    validacion = True
    for _ in range(1):
        # Verifica si el numero se encuentra en la misma fila
        if numero in matriz[fila]:
            validacion = False
            break

        # Verifica si el numero se encuentra en la misma columna
        for i in range(len(matriz)):
            if matriz[i][columna] == numero:
                validacion = False
                break
        if validacion == False:
            break

        # Verifica si el numero se encuentra en el mismo subcuadro
        subcuadro_fila = (fila // 3) * 3
        subcuadro_col = (columna // 3) * 3
        for i in range(subcuadro_fila, subcuadro_fila + 3):
            for j in range(subcuadro_col, subcuadro_col + 3):
                if matriz[i][j] == numero:
                    validacion = False
                    break
            if validacion == False:
                break

    return validacion

def llenar_matriz(tablero_vacio: list, lista_numeros:list) -> bool:
    '''
    llena matriz con numeros aleatorios respetando las reglas del Sudoku.

    Args:
        tablero_vacio (list): matriz creada para insertarle los numeros validos. 
    
    Returns:
        list: matriz creada con las dimensiones especificadas 

    Example:
        >>> llenar_matriz(tablero)
    '''
    validacion = True  
    for i in range(len(tablero_vacio)):
        for j in range(len(tablero_vacio[i])):
            if tablero_vacio[i][j] == 0:
                lista_numeros_copia = lista_numeros[:]
                random.shuffle(lista_numeros_copia)
                
                for numero in lista_numeros_copia:
                    if validar_numero_en_matriz(tablero_vacio, i, j, numero) == True:
                        tablero_vacio[i][j] = numero
                        
                        if llenar_matriz(tablero_vacio, lista_numeros) == True:
                            validacion = True
                            break
                        
                        tablero_vacio[i][j] = 0
                    else:
                        validacion = False
                break
        if validacion == False:
            break

    return validacion

def ocultar_numeros_en_matriz(matriz:list, valor_de_ocultar:any, dificultad: str) -> None:
    '''
    Funcion que oculta numeros del tablero de posiciones aleatorias dependiendo la dificultad

    Args:
        matriz (list): matriz que se le va a ocultar cierta cantidad de valores
        valor_de_ocultar (any): valor con el cual se va a reemplazar al valor a ocultar 
        dificultad (str): valor que va a ocultar cierta cantidad de elementos del tablero
    
    Returns:
        none: 

    Example:
        >>> ocultar_numeros_en_matriz(matriz, "", "intermedio")
    '''
    match dificultad:
        case "facil": dificultad = 0.20
        case "intermedio" : dificultad = 0.40
        case "dificil" : dificultad = 0.60
        case _: dificultad = None

    cantidad_numeros_tablero = len(matriz) ** 2
    cantidad_numeros_a_ocultar = int(cantidad_numeros_tablero *  dificultad)

    for _ in range(cantidad_numeros_a_ocultar):
        while True:
            fila_aleatoria = random.randint(0, len(matriz) - 1)
            columna_aleatoria = random.randint(0, len(matriz) - 1)

            if matriz[fila_aleatoria][columna_aleatoria] != 0:
                matriz[fila_aleatoria][columna_aleatoria] = valor_de_ocultar
                break

def dibujar_tablero(matriz_sudoku:list, ancho_celda: int, alto_celda:int, inicio_x_tablero:int, inicio_y_tablero:int, ventana:pygame.Surface, color_tablero:tuple, grosor_linea_gruesa:int, celda_seleccionada:tuple, celda_invalida:tuple) -> list:
    '''
    Dibuja un tablero sudoku clasico.

    Args:
        matriz_sudoku (list): Matriz ya creada para ser dibujada de forma de tablero sudoku.
        ancho_celda (int): Valor que va a tener el ancho de las celdas del tablero.
        alto_celda (int): Valor que va a tener el alto de las celdas del tablero.
        inicio_x (int): Cordenada X donde va a empezar el tablero.
        inicio_y (int): Cordena Y donde va a empezar el tablero.
        ventana (pygame.Surface): Ventana en la cual se va a dibujar el tablero.
        color_tablero (tuple): Color que va a tener las lineas del tablero.
    Returns:
        none: 
    '''
    # Creamos una matriz para guardar los rectangulos del tablero
    matriz_rectangulos = crear_matriz(9, 9, 0)

    ### DIBUJO DEL TABLERO ### 
    for i in range(len(matriz_sudoku)):
        for j in range(len(matriz_sudoku[i])):
            # Posiciones donde se van a dibujar las celdas
            x_celda = ancho_celda * j + inicio_x_tablero
            y_celda = alto_celda * i + inicio_y_tablero

            celda = pygame.Rect(x_celda, y_celda, ancho_celda, alto_celda)

            # Determinar el color de la celda
            if celda_seleccionada == (i, j):
                color_celda = const.COLOR_CELDA_SELECCIONADA  # Celeste transparente
                pygame.draw.rect(ventana, color_celda, celda)

            # Dibujar el borde de la celda
            dibujo = pygame.draw.rect(ventana, color_tablero, celda, 1)
            matriz_rectangulos[i][j] = dibujo


    ### DIBUJO DE LINEAS GRUESAS ###
    for i in range(10): 
        # grosor de la linea
        if i % 3 == 0:
            grosor = grosor_linea_gruesa
        else:
            grosor = 0

        # Lineas horizontales
        pygame.draw.line(ventana, color_tablero, (inicio_x_tablero, inicio_y_tablero + i * alto_celda), (inicio_x_tablero + 9 * ancho_celda, inicio_y_tablero + i * alto_celda), grosor)
        # Lineas verticales
        pygame.draw.line(ventana, color_tablero, (inicio_x_tablero + i * ancho_celda, inicio_y_tablero), (inicio_x_tablero + i * ancho_celda, inicio_y_tablero + 9 * alto_celda), grosor)
    
    return matriz_rectangulos

def dibujar_numeros(matriz:list, ancho_celda:int, alto_celda:int, inicio_x:int, inicio_y, color_numeros:tuple, ventana:pygame.Surface, grosor_numero:int, celda_invalida:tuple):
    '''
    Dibuja los numeros en las cordenas dichas
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            fuente = pygame.font.Font(None, grosor_numero)
            
            if celda_invalida == (i, j):
                color_actual = const.COLOR_CELDA_ERRONEA
            else:
                color_actual = color_numeros

            numero = fuente.render(str(matriz[i][j]), True, color_actual)

            # Medidas del texto
            ancho_texto, alto_texto = numero.get_size()

            # Posiciones donde se van a ubicar los numeros en el tablero
            x_numero = (ancho_celda * j) + (ancho_celda - ancho_texto) / 2 + inicio_x
            y_numero = (alto_celda * i) + (alto_celda - alto_texto) / 2 + inicio_y

            # Pinta los numeros
            ventana.blit(numero, (x_numero, y_numero))

def dibujar_opciones(ventana:pygame.Surface, ancho_celda:int, alto_celda:int, inicio_x:int, inicio_y:int, lista_numeros:list, color_numeros:tuple, color_tabla:tuple, grosor_lineas:int):
    '''
    Funcion que dibujas los rectangulos de opciones de numeros para agregar a la tabla del sudoku.
    '''
    ### DIBUJO DE LOS RECTANGULOS DE OPCIONES DE NUMERO ### 
    for i in range(3):
        for j in range(3):             
            # Posiciones donde se van a dibujar las celdas
            x_celda = ancho_celda * j + inicio_x
            y_celda = alto_celda * i + inicio_y

            # Dibujamos los rectangulos
            celda = pygame.Rect(x_celda, y_celda, ancho_celda, alto_celda)
            dibujo = pygame.draw.rect(ventana, color_tabla, celda, grosor_lineas)

    ### DIBUJO DE NUMEROS ###
    contador_opciones = 0
    tamaño_numeros = 25
    for i in range(3):
        for j in range(3):
            fuente = pygame.font.Font(None, tamaño_numeros)
            numero = fuente.render(str(lista_numeros[contador_opciones]), True, color_numeros)

            # Medidas del texto
            ancho_texto, alto_texto = numero.get_size()

            # Posiciones donde se van a ubicar los numeros en el tablero
            x_numero = (ancho_celda * j) + (ancho_celda - ancho_texto) / 2 + inicio_x
            y_numero = (alto_celda * i) + (alto_celda - alto_texto) / 2  + inicio_y

            ventana.blit(numero, (x_numero, y_numero))

            contador_opciones += 1

def obtener_celda_seleccionada(matriz_rectangulos:list, cordenadas:tuple) -> tuple|None:
    '''
    Obtiene la celda seleccionada adentro del tablero.
    '''
    verificacion = None
    for i in range(len(matriz_rectangulos)):
        for j in range(len(matriz_rectangulos[i])):
            # Valida si se interactuo sobre una celda (rectangulo)
            if matriz_rectangulos[i][j].collidepoint(cordenadas):
                verificacion =  (i, j)
                break
        if verificacion != None:
            break
    
    return verificacion

def mostrar_matriz(matriz:list):
    '''
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


### Ejecucion de la ventana ###
pygame.init()
ventana_sudoku = pygame.display.set_mode(const.DIMENSION_VENTANA, pygame.RESIZABLE)
pygame.display.set_caption(const.TITULO_JUEGO)
fps = pygame.time.Clock()

### Creamos la matriz para despues dibujarla ###
matriz = crear_matriz(9, 9, 0)
llenar_matriz(matriz, const.NUMEROS_SUDOKU)
matriz_copia = copy.deepcopy(matriz)
ocultar_numeros_en_matriz(matriz_copia, "", "intermedio")

mostrar_matriz(matriz)
print()
mostrar_matriz(matriz_copia)

# Dibujamos la tabla de opciones numericas
# dibujar_opciones(ventana_sudoku, ancho_celda_opciones, alto_celda_opciones, inicio_x_opciones, inicio_y_opciones, lista_numeros, const.NEGRO, const.NEGRO, const.GROSOR_LINEAS_OPCIONES)

celda_selec = None
celda_inv = None
corriendo = True
contador_errores = 0
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

        ## EVENTOS DE CLICK ###
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenemos las cordenadas x,y del evento click
            cordenadas_click = pygame.mouse.get_pos()
            nueva_celda = obtener_celda_seleccionada(matriz_rectangulos, cordenadas_click)

            if nueva_celda != None:
                celda_selec = nueva_celda
                celda_inv = None # Reinicia estado
            
        ## EVENTOS DE TECLA ###
        elif event.type == pygame.KEYDOWN and celda_selec:
            fila, columna = celda_selec
            # Validamos si el valor ingresado es numerico y si esta vacia la celda
            if (event.unicode.isdigit()) and (event.unicode != 0) and (matriz_copia[celda_selec[0]][celda_selec[1]] == ""):
                numero = int(event.unicode)
                # Validamos que el numero ingresado sea valido en la celda seleccionada
                if numero == matriz[celda_selec[0]][celda_selec[1]]:
                    # Ingresamos el numero en la tabla (matriz) del juego
                    matriz_copia[fila][columna] = numero 
                    celda_inv = None
                else:
                    celda_inv = celda_selec
                    matriz_copia[fila][columna] = numero
                    contador_errores += 1
                    print(contador_errores)
                    if contador_errores == 3:
                        matriz = crear_matriz(9, 9, 0)
                        llenar_matriz(matriz, const.NUMEROS_SUDOKU)
                        matriz_copia = copy.deepcopy(matriz)
                        ocultar_numeros_en_matriz(matriz_copia, "", "intermedio")
                        matriz_copia[fila][columna] = ""
                        contador_errores = 0
                        
            elif event.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                if celda_selec: 
                    if celda_inv or matriz_copia[fila][columna] != matriz[fila][columna]:
                        matriz_copia[fila][columna] = "" 
                        celda_inv = None
        
    ventana_sudoku.fill(const.BLANCO)
    # Dibujamos el tablero en la ventana
    matriz_rectangulos = dibujar_tablero(matriz_copia, const.ANCHO_CELDA_TABLERO, const.ALTO_CELDA_TABLERO, const.INICIO_X_TABLERO, const.INICIO_Y_TABLERO, ventana_sudoku, const.NEGRO, const.GROSOR_LINEA_GRUESA, celda_selec, celda_inv)
    dibujar_numeros(matriz_copia, const.ANCHO_CELDA_TABLERO, const.ALTO_CELDA_TABLERO, const.INICIO_X_TABLERO, const.INICIO_Y_TABLERO, const.NEGRO, ventana_sudoku, const.GROSOR_NUMEROS, celda_inv)

    # Actualiza la ventana
    pygame.display.flip()

    # FPS
    fps.tick(60)  

pygame.quit()



