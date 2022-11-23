import pygame

v = 0.1

running = True

pygame.init()  # inicializando el entorno
print('Inicializando')

ancho = 640
alto = 480

screen = pygame.display.set_mode ( (ancho,alto) )

color_mi_azul = pygame.Color(10,10,150)
color_azul = pygame.Color('blue')
color_cuadrado = pygame.Color('red')

x_cuadrado = ancho // 2
y_cuadrado = alto // 2

ancho_cuadrado = 20
alto_cuadrado = 20

while running:
    
    # leemos entrada del usuario (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('evento de salida')
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                print('Pulsada la tecla de escape')
                running = False
            elif event.key == pygame.K_UP:
                print('Pulsado UP')
                y_cuadrado -= 10
            elif event.key == pygame.K_DOWN:
                print('Pulsado DOWN')
                y_cuadrado += 10               
            elif event.key == pygame.K_LEFT:
                print('Pulsado LEFT')
                x_cuadrado -= 10
            elif event.key == pygame.K_RIGHT:
                print('Pulsado RIGHT')
                x_cuadrado += 10               
            print( (x_cuadrado, y_cuadrado) )
    # actualizamos
    
    
    # repintamos
    screen.fill(color_mi_azul)  # fondo
    
    pygame.draw.rect(screen, color_cuadrado, (x_cuadrado, y_cuadrado, ancho_cuadrado, alto_cuadrado) )
    
    pygame.display.flip()   # actualizacion a la pantalla del usuario


# terminamos
print('Saliendo')
pygame.quit()