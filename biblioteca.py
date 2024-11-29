import pygame
import constantes as const, os, random
import json
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

# Funciones para calcular el puntaje de un jugador:

def determinar_coeficiente_segun_dificultad(dificultad:str)->int:
    """
    Esta función se encarga de asignar un coeficiente para el puntaje del jugador de acuerdo al nivel de dificultad del juego.
    Recibe:
        dificultad(str): es un string que representa al nivel de dificultad del juego.
    Retorna:
        coeficiente_segun_dificultad (int): es un número entero que representa a un coeficiente con el que se multiplicará el puntaje del jugador teniendo en cuenta la dificultad elegida para el sudoku (1 para fácil, 1,5 para intermedio, 2 para díficil).
    """
    match dificultad:
        case "facil":
            coeficiente_segun_dificultad = 1
        case "intermedio":
            coeficiente_segun_dificultad = 1.5
        case "dificil":
            coeficiente_segun_dificultad = 2
    
    return coeficiente_segun_dificultad

def calcular_puntaje(minutos_transcurridos:int, cantidad_errores:int,  dificultad_sudoku:str="facil", puntaje_base:int=1000, penalizacion_por_error:int=50, penalizacion_por_minuto:int=10)->int:
    """
    Esta función se encarga de calcular el puntaje de un jugador al terminar la partida del sudoku.
    Recibe:
        minutos_transcurridos (int): es un número entero que representa la cantidad de minutos transcurridos desde que se inicio el juego.
        cantidad_errores (int): es un número entero que representa la cantidad de errores cometidos por el jugador.
        puntaje_base (int): es un número entero que representa el puntaje que tiene el jugador al iniciar el juego.
        penalizacion_por_error (int): es un número entero que representa el puntaje que se resta al jugador por cada error cometido.
        penalizacion_por_minuto (int): es un número entero que representa el puntaje que se resta al jugador por cada minuto transcurrido luego de haber iniciado el juego.
        dificultad(str): es un string que representa al nivel de dificultad del juego.
    Retorna:
        resultado (int): es un número entero que representa el puntaje final del jugador al terminar el juego.
    """
    resultado = (puntaje_base - (cantidad_errores * penalizacion_por_error) - (minutos_transcurridos * penalizacion_por_minuto)) * determinar_coeficiente_segun_dificultad(dificultad_sudoku)

    return resultado

# Función para determinar qué porcentaje del tablero del sudoku debe ser ocultado:

def asignar_porcentaje_casilleros_ocultos(dificultad:str="facil")->float:
    """
    Esta función se encarga de asignar un porcentaje de casilleros a ocultar en un tablero de sudoku de acuerdo al nivel de dificultad del juego.
    Recibe:
        dificultad(str): es un string que representa al nivel de dificultad del juego.
    Retorna:

    """
    match dificultad:
        case "facil":
            porcentaje_casilleros_ocultos = 0.20
        case "intermedio":
            porcentaje_casilleros_ocultos = 0.60
        case "dificil":
            porcentaje_casilleros_ocultos = 0.40

    return porcentaje_casilleros_ocultos




# Función para validar el ingreso de un nombre en el sudoku:

def validar_nombre_ingresado(nombre_jugador:str)-> bool:
    """
    Esta función se encarga de validar el nombre de un usuario viendo que tenga entre 3 y 15 caracteres y que sea alfanúmerico.
    Recibe:
        nombre_ingresado (str): es un string que representa el nombre del usuario a validar.
    Devuelve:
        retorno_validación (bool): es un booleano que tiene el valor True si el nombre del usuario es válido, False en caso contrario.
    """
    retorno_validacion = False
    if len(nombre_jugador) > 2 and len(nombre_jugador) < 15 and nombre_jugador.isalnum():
        retorno_validacion = True
    return retorno_validacion

# Funciones utiles para manejar el archivo json para los puntajes:

def guardar_archivo_json(lista:list[dict], ruta:str)->None:
    """
    Esta función se encarga de escribirle una lista de diccionario a un archivo json. Si el archivo json no existe lo crea.
    Recibe:
        lista (list[dict]): es una lista de diccionarios que representa a la lista con los datos a guardarse en el archivo json.
        ruta (str): representa a la dirección en la que se encuentra el archivo json al cual se le escribirá la lista.
    No retorna nada.
    """
    with open(ruta, "w") as mi_archivo:
        json.dump(lista, mi_archivo, indent = 4)


# Importar datos del archivo json al programa

def cargar_archivo_json(ruta:str)-> list[dict]:
    """
    Esta función se encarga leer un archivo json y retornar su contenido.
    Recibe:
        ruta (str): representa a la dirección en la que se encuentra el archivo json a ser leido.
    Retorna:
        datos(list[dict]): son los datos que del archivo en forma de una lista de diccionarios.
    """
    with open(ruta, "r") as mi_archivo:
        datos = json.load(mi_archivo)
    
    return datos

def agregar_jugador_a_lista(nombre_jugador:str,puntaje:float,lista_jugadores:list[dict])->list[dict]:
    """
    Esta función se encarga de agregar un nuevo jugador (son su id, su nombre y puntaje) a la lista de personas que ya jugaron al juego.
    Recibe:
        nombre_jugador (str): es un string que representa al nombre del jugador.
        puntaje (float): es un entero que representa al nombre del jugador
        lista_jugadores(list[dict]): es una lista de diccionarios que representa a la lista de jugadores qye ya han jugado al juego.
    Devuelve:
        lista_jugadores (list[dict]): es la lista de jugadores con el último jugador que jugo el juego ya cargado a la misma.
    """
    id = len(lista_jugadores)
    nuevo_jugador = {"id": id, "nombre": nombre_jugador, "puntaje": puntaje}
    lista_jugadores.append(nuevo_jugador)

    return lista_jugadores

