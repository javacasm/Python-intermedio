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

# colores https://www.w3schools.com/colors/colors_picker.asp
color_mi_azul = pygame.Color(10,10,150)  # r, g, b
color_azul = pygame.Color('blue')
color_cuadrado = pygame.Color('red')  # nombre de color
color_rosa = pygame.Color('#e21277')  # formato HTML
color_ball = (0, 102, 0)
color_texto = pygame.Color('white')

# geometria
x_cuadrado = ancho // 2
y_cuadrado = alto // 2

ancho_cuadrado = 50
alto_cuadrado = 50

radio_ball = 20

def random_ball():
    global x_ball, y_ball, vx_ball, vy_ball
    x_ball = random.randrange(radio_ball, ancho-radio_ball)
    y_ball = random.randrange(radio_ball, alto-radio_ball)

    vx_ball = random.randrange(-10,10)
    vy_ball = random.randrange(-10,10)

 

random_ball()

miImagen = pygame.image.load('./images/python-logo.png')
print(f'image size {miImagen.get_size()}')

# sonidos de https://soundcloud.com/es o youtube
pygame.mixer.music.load('./music/Fortunate_Note.ogg')

sonido_choque = pygame.mixer.Sound('./music/ok.wav') # guardamos la referencia para usarlo

def set_volumen(volumen):
    print(f'volumen={volumen:1.2f}')
    pygame.mixer.music.set_volume(volumen)
    sonido_choque.set_volume(volumen)
    
set_volumen(0.5) # volumen entre 0 y 1.0

clock = pygame.time.Clock()

uso = ''' flechas cursor - movimiento cuadrado
    b - salto de la bola
    p - Music On
    s - Music Off
    v - volumen ++
    c - volumen --
'''

colisiones = 0

sysfont = pygame.font.get_default_font()
print(f'font: {sysfont}')
font = pygame.font.SysFont(None, 48)  

print (uso)


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
                random_ball()
            elif event.key == pygame.K_p:
                print('Music On')
                pygame.mixer.music.play() # reproduce la musica
            elif event.key == pygame.K_s:
                print('Music Off')
                pygame.mixer.music.stop()
            elif event.key == pygame.K_v:
                volumen_actual = pygame.mixer.music.get_volume()
                set_volumen(volumen_actual - 0.05)
            elif event.key == pygame.K_c:
                volumen_actual = pygame.mixer.music.get_volume()
                set_volumen(volumen_actual + 0.05)
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
        colisiones += 1
        pygame.mixer.Sound.play(sonido_choque)
        random_ball()

    # repintamos en orden inverso a la cercani
    screen.fill(color_mi_azul)  # fondo
    
    # imagen del logo de python
    screen.blit(miImagen,(10,alto - miImagen.get_size()[1]-10) )
    
    # mostramos el numero de colisiones
    
    # generamos una imagen con el texto
    # font.render(texto, suavizado, color)
    img_texto = font.render (f'Colisiones: {colisiones}',True,color_texto)
    # copiamos la imagen del  texto sobre la pantalla
    screen.blit(img_texto, (20,20))
    
    # bolita
    pygame.draw.circle(screen, color_ball, (x_ball, y_ball), radio_ball)
    
    # rectangulo
    pygame.draw.rect(screen, color_rosa, (x_cuadrado, y_cuadrado, ancho_cuadrado, alto_cuadrado) )
    
    pygame.display.flip()   # actualizacion a la pantalla del usuario

    clock.tick(60)  # medimos tiempo entre actualizaciones y aseguramos 60 fps

# terminamos

print(f'{clock.get_fps():2.0f} fps')
print('Saliendo')
pygame.quit()