import constantes as const, os, random, pygame, biblioteca
os.system("cls")

pygame.init()
ventana = pygame.display.set_mode(const.DIMENSION_VENTANA, pygame.RESIZABLE)
pygame.display.set_caption(const.TITULO_JUEGO)
clock = pygame.time.Clock()

def generar_tablero(porcentaje_ancho_tablero:int, porcentaje_altura_tablero:int) -> None:
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
            grosor = 5
        else:
            grosor = 1

        # Linea horizontal
        lineas_horizontales = y_tablero + alto_celda * i 
        pygame.draw.line(ventana, const.NEGRO, (x_tablero, lineas_horizontales), (ancho_tablero + x_tablero, lineas_horizontales), grosor)

        # # Linea vertical
        lineas_verticales = x_tablero + ancho_celda * i 
        pygame.draw.line(ventana, const.NEGRO, (lineas_verticales, y_tablero), (lineas_verticales, alto_tablero + y_tablero), grosor)



def agregar_numeros():
    '''
    '''

def pintar_filas():
    '''
    '''

def pintar_columnas():
    '''
    '''

corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
    
    ventana.fill(const.BLANCO)

    generar_tablero(50, 90)

    # Actualiza la ventana
    pygame.display.flip()

    # FPS
    clock.tick(60)  


pygame.quit()

