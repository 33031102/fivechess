import pygame
def image(a):
     return  pygame.image.load(a)
def set((b,c)):
     return pygame.display.set_mode((b,c),0, 32)
def title(a):
     pygame.display.set_caption(a)
def update():
     pygame.display.update()
def saveimage(a,b):
     pygame.image.save(a, b)        
    