import pygame
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image


def create_jpg_image():
    # Window dimensions
    width = 280
    height = 280
    arrayData = np.zeros((280, 280))


    screen = pygame.display.set_mode((width, height))

    #screen = pygame.transform.scale(screen,(280, 280))
    clock = pygame.time.Clock()
    running = True
    flag = False
    for a in range(width):
        for b in range(height):
            aa = int(a)
            bb=int(b)
            screen.set_at((aa, bb), (255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = True

            if event.type == pygame.MOUSEMOTION and flag:
                x, y = pygame.mouse.get_pos()
                for p in range(30):
                    for k in range(30):
                        screen.set_at((x+p, y+k), (0, 0, 0))
                        try:
                            arrayData[(y+p, x+k)] = 255
                        except:
                            pass
                """for p in range(10):
                    for k in range(10):
                        screen.set_at((x - p, y - k), (0, 0, 0))
                for p in range(10):
                    for k in range(10):
                        screen.set_at((x + k, y - p), (0, 0, 0))
                for p in range(10):
                    for k in range(10):
                        screen.set_at((x - k, y - p), (0, 0, 0))
                for p in range(10):
                    for k in range(10):
                        screen.set_at((x - k, y + p), (0, 0, 0))"""
            if event.type == pygame.MOUSEBUTTONUP:
                flag = False
            if event.type == pygame.QUIT:
                     running = False


        pygame.display.flip()
        clock.tick(240)


    print(arrayData)
    Image.fromarray(arrayData).convert('RGB').resize((28, 28)).save('data.jpg')
    #b = Image.fromarray(arrayData).convert('RGB').resize((28, 28))

    #matplotlib.pyplot.imsave('name.png', arrayData)
    plt.imsave(fname='name2.jpg', arr=arrayData, cmap=plt.get_cmap('gray'))




