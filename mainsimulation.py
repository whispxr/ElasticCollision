import os
import pygame
clear = lambda: os.system('cls')

import pygame
import sys

class Pelota:
    def __init__(self, radio, masa, velocidad, x, y, color):
        self.radio = radio
        self.masa = masa
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
            self.radio -= 1
            self.velocidad[1] = -self.velocidad[1]  #se invierte la direccion

        #horizontal
        if self.x + self.radio > size[0] or self.x - self.radio < 0:
            self.radio -= 1
            self.velocidad[0] = -self.velocidad[0]  

        # Actualizar posición
        self.x += self.velocidad[0]
        self.y += self.velocidad[1]



    def checkcollision(self):
        pass

# Main loop
def main():
    pygame.init()

    ancho, alto = 800, 720
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Pelota con Rebote")


    pelota = Pelota(20, 1, [4, 4], 400, 300,(255,0,0))
    pelota2 = Pelota(40, 1, [5,5], 400, 300,(0,255,0))


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pantalla.fill((0, 0, 0))  

        pelota.ShowPelota(pantalla)  
        pelota2.ShowPelota(pantalla)


        pelota.checkcollision()
        pelota2.checkcollision()

        pelota.actualizar((ancho, alto))
        pelota2.actualizar((ancho,alto))





        pygame.display.flip()  
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()





