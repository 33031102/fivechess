import pygame  
pygame.mixer.pre_init(44100, 16, 2, 1024*4)
pygame.mixer.music.load("music/water.wav")
pygame.mixer.music.play()
chess_sound = pygame.mixer.Sound("music/chess.wav")
win_sound=pygame.mixer.Sound("music/win.wav")