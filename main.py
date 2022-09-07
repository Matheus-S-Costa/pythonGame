import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 500

velocidade = 10
x_controle = velocidade
y_controle = 0


pontos = 0
fonte = pygame.font.SysFont('comicsCarToon', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
    clock.tick(120)
    tela.fill((0,0,0))

    pygame.display.update()