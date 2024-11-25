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


matriz = crear_matriz_tablero(9, 9, 0)
llenar_tablero(matriz, 3)

def generar_tablero(porcentaje_ancho_tablero:int, porcentaje_altura_tablero:int, matriz:list) -> None:
    '''

    '''
    # Ancho y altura de la ventana actualizada
    ancho_ventana, alto_ventana = ventana.get_size()

    ### separacion de tablero y ventana ###
    x_tablero = ancho_ventana * 0.02
    y_tablero = alto_ventana * 0.04

    ### Dimensiones del tablero sudoku ###
    ancho_tablero = ancho_ventana * (porcentaje_ancho_tablero * 0.01)
    alto_tablero = alto_ventana * (porcentaje_altura_tablero * 0.01)

    ### Medida de las celdas ###
    ancho_celda = ancho_tablero / 9 
    alto_celda = alto_tablero / 9 

    ### Dibujo del tablero sudoku ###
    for i in range(10):
        if i % 3 == 0:
            grosor = 4
        else:
            grosor = 1

        # Lineas horizontales
        lineas_horizontales = y_tablero + (alto_celda * i) 
        pygame.draw.line(ventana, const.NEGRO, (x_tablero, lineas_horizontales), (ancho_tablero + x_tablero, lineas_horizontales), grosor)

        # # Lineas verticales
        lineas_verticales = x_tablero + (ancho_celda * i) 
        pygame.draw.line(ventana, const.NEGRO, (lineas_verticales, y_tablero), (lineas_verticales, alto_tablero + y_tablero), grosor)


    tamaño_numeros = 30
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            fuente = pygame.font.Font(None, tamaño_numeros)
            numero = fuente.render(str(matriz[i][j]), True, const.NEGRO)

            # Dimensiones del texto
            ancho_texto, alto_texto = numero.get_size()

            # Posiciones de los numeros en cada celda centrada
            x_numero = x_tablero + (ancho_celda * j) + (ancho_celda - ancho_texto) / 2
            y_numero = y_tablero + (alto_celda * i) + (alto_celda - alto_texto) / 2

            ventana.blit(numero, (x_numero, y_numero))


def dibujar_numeros_tablero():
    '''
    '''
    # Ancho y altura de la ventana actualizada
    ancho_ventana, alto_ventana = ventana.get_size()




def pintar_filas():
    '''
    '''

def pintar_columnas():
    '''
    '''

pygame.init()
ventana = pygame.display.set_mode(const.DIMENSION_VENTANA, pygame.RESIZABLE)
pygame.display.set_caption(const.TITULO_JUEGO)
clock = pygame.time.Clock()

### PORCENTAJE QUE OCUPA EL TABLERO EN RELACION A LA VENTANA ###
porcentaje_ancho_tablero = 50
porcentaje_alto_tablero = 90

corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
    
    # Fondo de la ventana
    ventana.fill(const.BLANCO)

    generar_tablero(porcentaje_ancho_tablero, porcentaje_alto_tablero, matriz)
    # dibujar_numeros_tablero()

    # Actualiza la ventana
    pygame.display.flip()

    # FPS
    clock.tick(60)  

pygame.quit()

