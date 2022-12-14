import pygame

v = 0.1

running = True

pygame.init()  # inicializando el entorno
print('Inicializando')

ancho = 640
alto = 480

screen = pygame.display.set_mode ( (ancho, alto) )

pygame.display.set_caption('Ejemplo de uso de pygame')

# colores
color_mi_azul = pygame.Color(10,10,150)  # r, g, b
color_azul = pygame.Color('blue')
color_cuadrado = pygame.Color('red')  # nombre de color
color_rosa = pygame.Color('#e21277')  # formato HTML

# geometria
x_cuadrado = ancho // 2
y_cuadrado = alto // 2

ancho_cuadrado = 50
alto_cuadrado = 50

while running:  # bucle de eventos
    
    # leemos entrada del usuario (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('evento de salida')
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                print('Pulsada la tecla de escape')
                running = False
            elif event.key == pygame.K_UP and y_cuadrado > 0:
                print('Pulsado UP')
                y_cuadrado -= 10
            elif event.key == pygame.K_DOWN and y_cuadrado < alto - alto_cuadrado:
                print('Pulsado DOWN')
                y_cuadrado += 10               
            elif event.key == pygame.K_LEFT and x_cuadrado > 0:
                print('Pulsado LEFT')
                x_cuadrado -= 10
            elif event.key == pygame.K_RIGHT and x_cuadrado < ancho - ancho_cuadrado:
                print('Pulsado RIGHT')
                x_cuadrado += 10               
            print( (x_cuadrado, y_cuadrado) )
            
    # actualizamos
    
    
    # repintamos
    screen.fill(color_mi_azul)  # fondo
    
    pygame.draw.rect(screen, color_rosa, (x_cuadrado, y_cuadrado, ancho_cuadrado, alto_cuadrado) )
    
    pygame.display.flip()   # actualizacion a la pantalla del usuario


# terminamos
print('Saliendo')
pygame.quit()