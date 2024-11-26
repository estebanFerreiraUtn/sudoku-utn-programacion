import constantes as const, os, random, pygame, biblioteca
os.system("cls")

def crear_matriz_tablero(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
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

def validar_numero_en_tablero(tablero:list, fila:int, columna:int, numero:int) -> bool:
    '''
    Valida que el numero que se este ingresando en el tablero sea correcto respetando las reglas del sudoku.

    Args:
        tablero (list): tablero(matriz) ya creada que se usara para validar.
        fila (int): numero de fila en la que ingrese el numero a validar.
        columna (int): numero de columna en la que ingrese el numero a validar.
        numero (int): numero que se ingrese para validar.
    
    Returns:
        bool: Si el numero es correcto sera True y en caso contrario False.
    '''
    validacion = True
    for _ in range(1):
        # Verifica si el numero se encuentra en la misma fila
        if numero in tablero[fila]:
            validacion = False
            break

        # Verifica si el numero se encuentra en la misma columna
        for i in range(len(tablero)):
            if tablero[i][columna] == numero:
                validacion = False
                break
        if validacion == False:
            break

        # Verifica si el numero se encuentra en el mismo subcuadro
        subcuadro_fila = (fila // 3) * 3
        subcuadro_col = (columna // 3) * 3
        for i in range(subcuadro_fila, subcuadro_fila + 3):
            for j in range(subcuadro_col, subcuadro_col + 3):
                if tablero[i][j] == numero:
                    validacion = False
                    break
            if validacion == False:
                break

    return validacion

def llenar_tablero(tablero_vacio: list, lista_numeros:list) -> bool:
    '''
    llena tableros con numeros aleatorios respetando las reglas del Sudoku.

    Args:
        tablero_vacio (list): Tablero creado para insertarle los numeros validos. 
    
    Returns:
        list: Tablero creado con las dimensiones especificadas 

    Example:
        >>> llenar_tablero(tablero)
    '''
    validacion = True  
    for i in range(len(tablero_vacio)):
        for j in range(len(tablero_vacio[i])):
            if tablero_vacio[i][j] == 0:
                lista_numeros_copia = lista_numeros[:]
                random.shuffle(lista_numeros_copia)
                
                for numero in lista_numeros_copia:
                    if validar_numero_en_tablero(tablero_vacio, i, j, numero) == True:
                        tablero_vacio[i][j] = numero
                        
                        if llenar_tablero(tablero_vacio, lista_numeros) == True:
                            validacion = True
                            break
                        
                        tablero_vacio[i][j] = 0
                    else:
                        validacion = False
                break
        if validacion == False:
            break

    return validacion

def ocultar_numeros(tablero:list, valor_de_ocultar:any, dificultad: str) -> None:
    '''
    Funcion que oculta numeros del tablero de posiciones aleatorias dependiendo la dificultad

    Args:
        tablero (list): Tablero (matriz) que se le va a ocultar cierta cantidad de valores
        valor_de_ocultar (any): valor con el cual se va a reemplazar al valor a ocultar 
        dificultad (str): valor que va a ocultar cierta cantidad de elementos del tablero
    
    Returns:
        none: 

    Example:
        >>> ocultar_numeros(matriz, "", "intermedio")
    '''
    match dificultad:
        case "facil": dificultad = 0.20
        case "intermedio" : dificultad = 0.40
        case "dificil" : dificultad = 0.60
        case _: dificultad = None

    cantidad_numeros_tablero = len(tablero) ** 2
    cantidad_numeros_a_ocultar = int(cantidad_numeros_tablero *  dificultad)

    for _ in range(cantidad_numeros_a_ocultar):
        while True:
            fila_aleatoria = random.randint(0, len(tablero) - 1)
            columna_aleatoria = random.randint(0, len(tablero) - 1)

            if tablero[fila_aleatoria][columna_aleatoria] != 0:
                tablero[fila_aleatoria][columna_aleatoria] = valor_de_ocultar
                break

def generar_tablero(matriz_sudoku:list, ancho_celda: int, alto_celda:int, inicio_x:int, inicio_y:int, ventana:pygame.Surface, tamaño_numeros:int, color_numeros:tuple) -> None:
    '''
    Dibuja un tablero sudoku clasico.

    Args:
        matriz_sudoku (list): Matriz ya creada para ser dibujada de forma de tablero sudoku.
        ancho_celda (int): Valor que va a tener el ancho de las celdas del tablero.
        alto_celda (int): Valor que va a tener el alto de las celdas del tablero.
        inicio_x (int): Cordenada X donde va a empezar el tablero.
        inicio_y (int): Cordena Y donde va a empezar el tablero.
        ventana (pygame.Surface): Ventana en la cual se va a dibujar el tablero.
        tamaño_numeros (int): Tamaño que van a tener los numeros en el tablero.
        color_numeros (tuple): Color que van a tener los numeros en el tablero.
        
    Returns:
        none: 
    '''
    ### DIBUJO DEL TABLERO ### 
    matriz_rectangulos = crear_matriz_tablero(9, 9, 0)

    for i in range(len(matriz_sudoku)):
        for j in range(len(matriz_sudoku[i])):
            if (i + j) % 2 == 0:
                color = const.NEGRO
            else:
                color = const.AZUL

            # Posiciones donde se van a dibujar las celdas
            x_celda = ancho_celda * j + inicio_x
            y_celda = alto_celda * i + inicio_y

            # Dibujamos los rectangulos
            celda = pygame.Rect(x_celda, y_celda, ancho_celda, alto_celda)
            dibujo = pygame.draw.rect(ventana, color, celda)

            matriz_rectangulos[i][j] = dibujo

            matriz_rectangulos

    ### DIBUJO DE NUMEROS ###
    for i in range(len(matriz_sudoku)):
        for j in range(len(matriz_sudoku[i])):
            fuente = pygame.font.Font(None, tamano_numero)
            numero = fuente.render(str(matriz_sudoku[i][j]), True, color_numeros)

            # Medidas del texto
            ancho_texto, alto_texto = numero.get_size()

            # Posiciones donde se van a ubicar los numeros en el tablero
            x_numero = (ancho_celda * j) + (ancho_celda - ancho_texto) / 2 + inicio_x
            y_numero = (alto_celda * i) + (alto_celda - alto_texto) / 2 + inicio_y

            ventana.blit(numero, (x_numero, y_numero))

def dibujar_opciones(ventana:pygame.Surface, ancho_celda:int, alto_celda:int, inicio_x:int, inicio_y:int, lista_numeros:list, color_numeros:tuple):
    '''
    Funcion que dibujas los rectangulos de opciones de numeros para agregar a la tabla del sudoku.
    '''
    ### DIBUJO DE LOS RECTANGULOS DE OPCIONES DE NUMERO ### 
    for i in range(3):
        for j in range(3): 
            if (i + j) % 2 == 0:
                color = const.NEGRO
            else:
                color = const.AZUL
            
            # Posiciones donde se van a dibujar las celdas
            x_celda = ancho_celda * j + inicio_x
            y_celda = alto_celda * i + inicio_y

            # Dibujamos los rectangulos
            celda = pygame.Rect(x_celda, y_celda, ancho_celda, alto_celda)
            dibujo = pygame.draw.rect(ventana, color, celda)

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

        
### EJECUCION DE LA VENTANA ###
pygame.init()
ventana_sudoku = pygame.display.set_mode(const.DIMENSION_VENTANA, pygame.RESIZABLE)
pygame.display.set_caption(const.TITULO_JUEGO)
fps = pygame.time.Clock()

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

### VARIABLES TABLERO ###
ancho_celda_tablero = 50
alto_celda_tablero = 50
inicio_x_tablero = 10
inicio_y_tablero = 70

### VARIABLES TABLA OPCIONES NUMERICAS ###
ancho_celda_opciones = 80
alto_celda_opciones = 50
inicio_x_opciones = 500
inicio_y_opciones = 370
tamano_numero = 25

### Creamos la matriz para despues dibujarla ###
matriz = crear_matriz_tablero(9, 9, 0)
llenar_tablero(matriz, lista_numeros)
matriz_copia = matriz[:]
ocultar_numeros(matriz_copia, "", "intermedio")

corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtenemos las cordenadas x,y del evento click
            eje_x, eje_y = event.pos
            # Mostramos x,y 
            print(f"X: {eje_x}, Y: {eje_y}")

    # Fondo de la ventana
    ventana_sudoku.fill(const.BLANCO)

    # Dibujamos el tablero en la ventana
    generar_tablero(matriz, ancho_celda_tablero, alto_celda_tablero, inicio_x_tablero, inicio_y_tablero, ventana_sudoku, tamano_numero, const.BLANCO)
    # Dibujamos la tabla de opciones numericas
    dibujar_opciones(ventana_sudoku, ancho_celda_opciones, alto_celda_opciones, inicio_x_opciones, inicio_y_opciones, lista_numeros, const.BLANCO)

    # Actualiza la ventana
    pygame.display.flip()

    # FPS
    fps.tick(60)  

pygame.quit()

