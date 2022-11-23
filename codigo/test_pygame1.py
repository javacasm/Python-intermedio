import pygame


running = True

pygame.init()  # inicializando el entorno
print('Inicializando')

ancho = 640
alto = 480

screen = pygame.display.set_mode ( (ancho,alto) )

color_mi_azul = pygame.Color(10,10,150)
color_azul = pygame.Color('blue')

while running:
    
    # leemos entrada del usuario (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('evento de salida')
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                print('Pulsada la tecla de escape')
                running = False
    
    # actualizamos
    
    screen.fill(color_mi_azul)  # fondo
    
    pygame.display.flip()   # actualizacion a la pantalla del usuario
    # repintamos


# terminamos
print('Saliendo')
pygame.quit()