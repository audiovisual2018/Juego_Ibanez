import pygame
from pygame.locals import*
import random
from random import randint
import os
import sys

#Defino colores en RGB

negro= (0,0,0)
blanco= (255,255,255)
verde=(0,255,0)
rojo=(255,0,0)

pygame.init()

#defino el tamaño de la pantalla
tamaño= 700,500
pantalla=pygame.display.set_mode(tamaño)

#constantes
IMG_DIR = "imagenes"
piso=500
espaciomedio=randint(150,250)

#Clases y funciones


def intro_juego():
    intro= True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_c:
                    juego()
        pantalla.fill(blanco)
        letras=pygame.font.SysFont(None,50) #50 es el tamaño de las letras
        texto=letras.render("Presione 'c' para comenzar", True, negro) # Aparece en pantalla el texto Game Over
        pantalla.blit(texto,[115,250])      #defino la ubicación donde va a aparecer el texto
        pygame.display.update()
        
def gameover():
    over= True
    while over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_c:
                    juego()
        pantalla.fill(blanco)
        letras=pygame.font.SysFont(None,70) #25 es el tamaño de las letras
        texto=letras.render("Game Over", True, rojo) #Aaperecera en pantalla el texto Game Over
        pantalla.blit(texto,[215,250])      #defino la ubicación donde va a aparecer el texto
        pygame.display.update()

        
def juego():
    
    #Nombre del juego
    pygame.display.set_caption("Flappy planes")

    final=False

    #Cuadros por segundo
    reloj=pygame.time.Clock()

    #Fondo de pantalla
    fondo=pygame.image.load("fondo.png").convert()
    pantalla.blit(fondo, (0,0))
    pygame.display.flip() 

    ##Otras imagenes
    avi=pygame.image.load("avi.png").convert_alpha()
    nube=pygame.image.load("nube.png").convert_alpha()
    nubs=pygame.image.load("nubs.png").convert_alpha()
    
    def avion(x,y):
        pantalla.blit(avi,(x,y))
        
    def nubes1(xloc1, yloc1):
        pantalla.blit(nube,(xloc1,yloc1))

    def nubes2(xloc2, yloc2):
        pantalla.blit(nube,(xloc2,yloc2))

    def nubes3(xloc3, yloc3):
        pantalla.blit(nube,(xloc3,yloc3))
        
    def nubes4(xloc4, yloc4):
        pantalla.blit(nubs,(xloc4,yloc4))
    

    def puntaje(puntos):
        letras=pygame.font.SysFont(None,40) #25 es el tamaño de las letras
        texto=letras.render("Puntos: "+ str(puntos), True, negro)
        pantalla.blit(texto,[0,0])
##        puntos=0
##        if xloc==100:
##            puntos+=1 
                                                     
## valores definidos    
    x=150
    y=250
    x_velocidad=0
    y_velocidad=0
    puntos=0
    
    #nubes 1
    xloc1=700
    yloc1=randint(10,250)
    velnubes1=2.5

    #nubes 2
    xloc2=790
    yloc2=randint(250,420)
    velnubes2=3.6

    #nubes 3
    xloc3=1890
    yloc3=randint(-10,450)
    velnubes3=4.5

    #nubes 4
    xloc4=740
    yloc4=randint(-10,450)
    velnubes4=1.5


    while not final:
        for event in pygame.event.get():    # obtiene todos los eventos en pygame
            if event.type== pygame.QUIT:    # si se da el evento quit el juego termina
                final=True
            if event.type==pygame.KEYDOWN:      # al dejar de apretar la tecla la velocidad baja en 10    
                if event.key==pygame.K_UP:
                    y_velocidad=-5             
            if event.type== pygame.KEYUP:       # al presionar la tacla la velocidaad aumenta en 3
                if event.key==pygame.K_UP:
                    y_velocidad=3

        #nubes1
        if xloc1<-180:
            xloc1=700
            yloc1=randint(-5,250)
        #nubes2
        if xloc2<-290:
            xloc2=750
            yloc2=randint(90,420)
        #nubes3
        if xloc3<-400:
            xloc3=790
            yloc3=randint(-5,440)
        #nubes4
        if xloc4<-170:
            xloc4=790
            yloc4=randint(-5,440)
    
        if y>piso:      #si toca el piso pierde
            gameover()
        if y<=-50:       #si va para arriba de la pantalla pierde
            gameover()
            
        if xloc1<x+40<xloc1+190 and yloc1<y+5<yloc1+50:
            velnubes1=0
            y_velocidad=0
            gameover()
        if xloc2<x+40<xloc2+190 and yloc2<y+5<yloc2+50:
            velnubes2=0
            y_velocidad=0
            gameover()
        if xloc3<x+40<xloc3+190 and yloc3<y+5<yloc3+50:
            velnubes3=0
            y_velocidad=0
            gameover()
        if xloc4<x+40<xloc4+190 and yloc4<y+5<yloc4+56:
            velnubes4=0
            y_velocidad=0
            gameover()

            
        if xloc1==50:
            puntos= puntos +1
        if xloc2==50:
            puntos= puntos +1
        if xloc3==50:
            puntos= puntos +1
        if xloc4==50:             
            puntos= puntos +1
            
        pantalla.blit(avi,(x,y))
        pantalla.blit(nube,(xloc1,yloc1))
        pantalla.blit(nube,(xloc2,yloc2))
        pantalla.blit(nube,(xloc3,yloc3))
        pantalla.blit(nubs,(xloc4,yloc4))
        pantalla.blit(fondo, (0,0))

        avion(x,y)
        y+=y_velocidad

        #nubes1
        nubes1(xloc1, yloc1)
        xloc1-=velnubes1
        #nubes2
        nubes2(xloc2, yloc2)
        xloc2-=velnubes2
        #nubes3
        nubes3(xloc3, yloc3)
        xloc3-=velnubes3
        #nubes4
        nubes4(xloc4, yloc4)
        xloc4-=velnubes4
        
        puntaje(puntos)
        pygame.display.update()
        reloj.tick(60)              #rapidez del juego

    pygame.quit()
intro_juego()
juego()
