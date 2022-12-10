import pygame
import random

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
color_ball = (0, 102, 0)


# geometria
x_cuadrado = ancho // 2
y_cuadrado = alto // 2

ancho_cuadrado = 50
alto_cuadrado = 50

x_ball = random.randrange(0,ancho)
y_ball = random.randrange(0,alto)

vx_ball = random.randrange(5,10)
vy_ball = random.randrange(5,10)

miImagen_orig = pygame.image.load('./images/python-logo.png')

miImagen = pygame.transform.scale(miImagen_orig,(50,50))

radio_ball = 20

clock = pygame.time.Clock()

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
            elif event.key == pygame.K_b:    
                x_ball = random.randrange(0,ancho)
                y_ball = random.randrange(0,alto)

                vx_ball = random.randrange(-10,10)
                vy_ball = random.randrange(-10,10)
                
            print( (x_cuadrado, y_cuadrado) )
            
    # actualizamos
    
    x_ball = x_ball + vx_ball
    y_ball = y_ball + vy_ball
    
    if x_ball > ancho - radio_ball or x_ball < radio_ball:
        vx_ball = -vx_ball

    if y_ball > alto - radio_ball or y_ball < radio_ball:
        vy_ball = -vy_ball
        
    ## deteccion de colisones
        
    if  x_cuadrado < x_ball < x_cuadrado+ancho_cuadrado and y_cuadrado < y_ball < y_cuadrado+ alto_cuadrado:
        print('Hay colision')

    # repintamos en orden inverso a la cercani
    screen.fill(color_mi_azul)  # fondo
    
    screen.blit(miImagen,(20,alto - 400) )
    
    pygame.draw.circle(screen, color_ball, (x_ball, y_ball), radio_ball)
    
    pygame.draw.rect(screen, color_rosa, (x_cuadrado, y_cuadrado, ancho_cuadrado, alto_cuadrado) )
    
    pygame.display.flip()   # actualizacion a la pantalla del usuario

    clock.tick(60)  # medimos tiempo entre actualizaciones

# terminamos
print('Saliendo')
print(f'{clock.get_fps()} fps')
pygame.quit()