import random, os
os.system("cls")

def crear_tablero(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    '''
    Funcion que crea un tablero (matriz) pasando por paramtro las dimensiones.
    '''
    tablero = []

    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        tablero += [fila]
    return tablero

def validar_numero_en_tablero(tablero:list, fila:int, columna:int, numero:int) -> bool:
    '''
    Verifica si el numero puesto es valido en la fila y columna del tablero
    '''
    # Verifica si el numero esta en la fila
    if numero in tablero[fila]:
        return False

    # Verifica si el numero esta en la columna
    for i in range(len(tablero)):
        if tablero[i][columna] == numero:
            return False

    # Verifica si el numero esta en el cuadrado 3x3
    subcuadro_fila = (fila // 3) * 3
    subcuadro_col = (columna // 3) * 3

    for i in range(subcuadro_fila, subcuadro_fila + 3):

        for j in range(subcuadro_col, subcuadro_col + 3):

            # Asegurarse de no comparar con la propia celda si ya está colocada
            if tablero[i][j] == numero:
                return False

    # Si pasa todas las verificaciones el numero es valido.
    return True

def llenar_tablero(tablero_vacio:list, desde:int, hasta:int) -> None:
    '''
    Llena el tablero de forma aleatoria respetando las reglas del sudoku
    '''
    for i in range(len(tablero_vacio)):
        for j in range(len(tablero_vacio[i])):
            while True:
                numero = random.randint(desde, hasta)
                if validar_numero_en_tablero(tablero_vacio, i, j, numero):
                    tablero_vacio[i][j] = numero
                    break

def mostrar_tablero(tablero:list) -> None:
    '''
    Muestra la simulacion de un tablero en consola
    '''
    for i in range(len(tablero)):

        # separadores de filas
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(len(tablero[i])):

            # separadores de columnas
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            # Muestra el numero
            print(f"{tablero[i][j]} ", end="")

        # salto en linea por cada fila
        print()

tablero = crear_tablero(9, 9, 0)
llenar_tablero(tablero, 1, 9)
mostrar_tablero(tablero)
