import os
import pygame
import random
import sys
clear = lambda: os.system('cls')


class Pelota:
    def __init__(self, radio, masa, velocidad, x, y, color):
        self.radio = radio
        self.masa = masa #todavia sin uso xd
        self.velocidad = velocidad  
        self.x = x
        self.y = y
        self.aceleracion = 2
        self.color = color

    def ShowPelota(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), self.radio)

    def actualizar(self, size):
        # vertical
        if self.y + self.radio > size[1] or self.y - self.radio < 0:
            self.velocidad[1] = -self.velocidad[1]  #se invierte la direccion

        #horizontal
        if self.x + self.radio > size[0] or self.x - self.radio < 0:
            self.velocidad[0] = -self.velocidad[0]  

        # Actualizar posición
        self.x += self.velocidad[0]
        self.y += self.velocidad[1]


def checkcollision(pelota1, pelota2):
    distx = pelota1.x - pelota2.x
    disty = pelota1.y - pelota2.y
    distancia = (distx ** 2 + disty ** 2) ** 0.5 # distancia por pitagoras

    if distancia <= pelota1.radio + pelota2.radio: 
        # se transfiere la energia de la otra pelota
        pelota1.velocidad[0], pelota2.velocidad[0] = pelota2.velocidad[0], pelota1.velocidad[0]
        pelota1.velocidad[1], pelota2.velocidad[1] = pelota2.velocidad[1], pelota1.velocidad[1]


# Main loop
def main():
    pygame.init()

    ancho, alto = 1400, 720
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Pelota con Rebote")


    pelota1 = Pelota(20, 1, [4, 4], 200,400,(255,0,0))
    pelota2 = Pelota(30, 1, [7,7], 300,500,(0,255,0))
    pelota3 = Pelota(40, 1, [3,3], 500,600,(0,0,255))



    pelotas = [pelota1,pelota2,pelota3]


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pantalla.fill((0, 0, 0))  

        for i in pelotas:
            i.ShowPelota(pantalla)





        checkcollision(pelota1,pelota2)
        checkcollision(pelota1,pelota3)
        checkcollision(pelota2,pelota3)

        # for i in pelotas:
        #     for j in pelotas:
        #         if i == j:
        #             pass
        #         else:
        #             checkcollision(i,j)
        

        for i in pelotas:
            i.actualizar((ancho,alto))




        pygame.display.flip()  
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()





