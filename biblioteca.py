import random, os
os.system("cls")

def crear_tablero(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    '''
    Función que crea un tablero (matriz) pasando por parámetro las dimensiones.

    Args:
        cantidad_filas (int): Cantidad de filas que va a tener el tablero sudoku (9x9 o 16x16)
        cantidad_columnas (int): Cantidad de columnas que va a tener el tablero sudoku (9x9 o 16x16)
        valor_inicial (any): Valores que van a tener los valores de cada posicion del tablero. 
    
    Returns:
        list: Tablero creado con las dimensiones especificadas 

    Example:
        >>> crear_tablero(9, 9, 0)
        [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''

    tablero = []

    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        tablero.append(fila)
    return tablero

def validar_numero_en_tablero(tablero:list, fila:int, columna:int, numero:int, subcuadrado_largo:int) -> bool:
    '''
    Valida que el numero que se este ingresando en el tablero sea correcto respetando las reglas del sudoku.

    Args:
        tablero (list): tablero(matriz) ya creada que se usara para validar.
        fila (int): numero de fila en la que ingrese el numero a validar.
        columna (int): numero de columna en la que ingrese el numero a validar.
        numero (int): numero que se ingrese para validar.
        subcuadrado_largo: largo del subcuadrado que se usara para validar que el numero no se encuentre ahi.
    
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
        subcuadro_fila = (fila // subcuadrado_largo) * subcuadrado_largo
        subcuadro_col = (columna // subcuadrado_largo) * subcuadrado_largo

        for i in range(subcuadro_fila, subcuadro_fila + subcuadrado_largo):
            for j in range(subcuadro_col, subcuadro_col + subcuadrado_largo):
                if tablero[i][j] == numero:
                    validacion = False
                    break
            if validacion == False:
                break

    return validacion

def llenar_tablero(tablero_vacio: list, subcuadrado_largo: int) -> bool:
    '''
    llena tableros con numeros aleatorios respetando las reglas del Sudoku.

    Args:
        tablero_vacio (list): Tablero creado para insertarle los numeros validos. 
        subcuadrado_largo (int): Largo que va a tener los subcuadrados del tablero.
    
    Returns:
        list: Tablero creado con las dimensiones especificadas 

    Example:
        >>> llenar_tablero(tablero, 3)
    '''
    validacion = True  

    for i in range(len(tablero_vacio)):
        for j in range(len(tablero_vacio[i])):
            if tablero_vacio[i][j] == 0:
                numeros = list(range(1, len(tablero_vacio) + 1))
                random.shuffle(numeros)
                
                for numero in numeros:
                    if validar_numero_en_tablero(tablero_vacio, i, j, numero, subcuadrado_largo) == True:
                        tablero_vacio[i][j] = numero
                        
                        if llenar_tablero(tablero_vacio, subcuadrado_largo) == True:
                            validacion = True
                            break
                        
                        tablero_vacio[i][j] = 0
                    else:
                        validacion = False
                break
        if validacion == False:
            break

    return validacion

def mostrar_tablero(tablero: list, subcuadrado_largo: int) -> None:
    '''
    Muestra la simulacion de un tablero sudoku por consola.

    Args:
        tablero (list): tablero(matriz) ya generada para mostrar por consola de forma de tablero sudoku.
        subcuadrado_largo (int): Largo de los subcuadrados para mostrar dinamicamente por consola respetando las dimensiones del tablero.
    
    Returns:
        None: No retorna nada.

    Example:
        >>> mostrar_tablero(tablero, 3)
    '''
    for i in range(len(tablero)):
        # Separadores de filas cada subcuadrado
        if i % subcuadrado_largo == 0 and i != 0:
            print("---" * (len(tablero) + subcuadrado_largo - 2))

        for j in range(len(tablero[i])):
            # Separadores de columnas cada subcuadrado
            if j % subcuadrado_largo == 0 and j != 0:
                print("|", end=" ")

            print(f"{tablero[i][j]:2} ", end="")
        print()

def ocultar_numeros(tablero:list, valor_oculto:any, dificultad: str) -> None:
    '''
    Funcion que oculta numeros del tablero de posiciones aleatorias dependiendo la dificultad
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
            columna_aleatoria = random.randint(0, len(tablero[0]) - 1)

            if tablero[fila_aleatoria][columna_aleatoria] != 0:
                tablero[fila_aleatoria][columna_aleatoria] = valor_oculto
                break

# Sudoku 9x9
filas = 16
columnas = 16
valor_inicial = 0
subcuadrado_largo = 4


tablero_sudoku = crear_tablero(filas, columnas, valor_inicial)

print("Tablero vacio:\n")
mostrar_tablero(tablero_sudoku, subcuadrado_largo)

print("\nGenerando Sudoku dinamico...\n")
llenar_tablero(tablero_sudoku, subcuadrado_largo)

print("Sudoku completado:\n")
mostrar_tablero(tablero_sudoku, subcuadrado_largo)

print("\nOcultando numeros del tablero sudoku...")
ocultar_numeros(tablero_sudoku, 0, "intermedio")

print("\nTablero sudoku: \n")
mostrar_tablero(tablero_sudoku, subcuadrado_largo)

print("\nTablero sudoku...\n")
llenar_tablero(tablero_sudoku, subcuadrado_largo)
mostrar_tablero(tablero_sudoku, subcuadrado_largo)


