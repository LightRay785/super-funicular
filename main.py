import pygame
import os
import random
from sys import exit
pygame.init()

# Screen Setup
width, height = 600, 1100
screen = pygame.display.set_mode((width, height))
fps = 60
pygame.display.set_caption('Flappy Bird')
bird = pygame.image.load('flappy-bird.png')

#class Bird(pygame.sprite.Sprite):

clock = pygame.time.Clock()
while True:
    screen.fill(255,255,255)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(fps)

#WIP
