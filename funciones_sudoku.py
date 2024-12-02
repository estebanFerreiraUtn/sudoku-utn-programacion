import constantes as const, os, random, pygame
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
        tablero_vacio (list): Matriz creada para insertarle los numeros validos.
        lista_numeros (list): Lista de numeros con la cual se va a llenar la matriz 
    
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

def dibujar_tablero(matriz:list, ancho_celda: int, alto_celda:int, inicio_x_tablero:int, inicio_y_tablero:int, ventana:pygame.Surface, color_tablero:tuple, grosor_linea_gruesa:int, celda_seleccionada:tuple) -> list:
    '''
    Dibuja un tablero sudoku clasico.

    Args:
        matriz (list): Matriz ya creada para ser dibujada de forma de tablero sudoku.
        ancho_celda (int): Valor que va a tener el ancho de las celdas del tablero.
        alto_celda (int): Valor que va a tener el alto de las celdas del tablero.
        inicio_x (int): Cordenada X donde va a empezar el tablero.
        inicio_y (int): Cordena Y donde va a empezar el tablero.
        ventana (pygame.Surface): Ventana en la cual se va a dibujar el tablero.
        color_tablero (tuple): Color que va a tener las lineas del tablero.
        grosor_linea_gruesa (int): Grosor de las lineas que dividen las submatrices.
        celda_seleccionada (tuple): Valor de x, y de la celda seleccionada.


    Returns:
        matriz_rectangulos (list): 
    '''
    # Creamos una matriz para guardar los rectangulos del tablero
    matriz_rectangulos = crear_matriz(9, 9, 0)

    ### DIBUJO DEL TABLERO ### 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
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

def dibujar_numeros(matriz:list, ancho_celda:int, alto_celda:int, inicio_x:int, inicio_y, color_numeros_principales:tuple, ventana:pygame.Surface, grosor_numero:int, lista_celdas_invalidas:tuple, lista_celdas_validas:tuple) -> None:
    '''
    Dibuja los numeros en el tablero y las pinta de un color en especifico segun su valor.

    Args:
        matriz (list): Matriz del tablero el cual se va a dibujar los numeros que tiene en si misma en la ventana.
        ancho_celda (int): Pasamos el ancho que tiene la celda para dibujar los numeros de forma centrada con una formula.
        alto_celda (int): Pasamos el alto que tiene la celda para dibujar los numeros de forma centrada con una formula.
        inicio_x (int): Donde se van a comenzar a dibujar los numeros en el tablero en el eje x.
        inicio_y (int): Donde se van a comenzar a dibujar los numeros en el tablero en el eje y.
        color_numeros_principales (tuple): color que van a tener los numeros principales del tablero.
        ventana (pygame.Surfe): Ventana donde se van a dibujar los numeros.
        grosor_numero (int): Grosor que van a tener los numeros al dibujarse.
        lista_celdas_invalidas (list): Lista que va a contener todas las celdas con los numeros ingresados invalidos para pintarlos de rojo.
        lista_celdas_validas (list): Lista que va a contener todas las celdas con los numeros ingresados validos para pintarlos de verde.

    Returns:
        None: No retorna nada, solo dibuja los numeros en la ventana
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            fuente = pygame.font.Font(None, grosor_numero)

            if (i, j) in lista_celdas_validas:
                color_actual = const.VERDE
            elif (i, j) in lista_celdas_invalidas:
                color_actual = const.COLOR_CELDA_ERRONEA
            else:
                color_actual = color_numeros_principales

            numero = fuente.render(str(matriz[i][j]), True, color_actual)

            # Medidas del texto
            ancho_texto, alto_texto = numero.get_size()

            # Posiciones donde se van a ubicar los numeros en el tablero
            x_numero = (ancho_celda * j) + (ancho_celda - ancho_texto) / 2 + inicio_x
            y_numero = (alto_celda * i) + (alto_celda - alto_texto) / 2 + inicio_y

            # Pinta los numeros
            ventana.blit(numero, (x_numero, y_numero))

def obtener_celda_seleccionada(matriz_rectangulos:list, cordenadas:tuple) -> tuple|None:
    '''
    Obtiene la celda (x, y) seleccionada adentro del tablero.

    Args:
        matriz_rectangulos (list): Lista de una matriz que contiene los rectangulos (celdas) del tablero.
        cordenadas (tuple): Cordenas donde se clickeo en la ventana para validar si coincide con algun rectangulo (celda) del tablero.
    
    Returns:
        tuple: Si el click coincide con algun rectangulo (celda) del tablero entonces devuelve la celda seleccionada (x, y)
        None: En caso contrario no devuelve nada 
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

def mostrar_matriz(matriz:list) -> None:
    '''
    Funcion que muesta una matriz por consola.

    Args:
        matriz (list): lista ya creada para mostrar por consola en forma de matriz.

    Returns:
        None: No retorna nada ya que solamente se encarga de mostrar por consola la lista en forma de matriz

    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
