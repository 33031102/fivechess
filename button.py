#-*-coding:utf-8-*-
import pygame
from window import *
class Button(object):
    def __init__(self, image_filename, position):
        self.position = position
        self.image = pygame.image.load(image_filename)

    def render(self, surface):     
        x, y = self.position
        w, h = self.image.get_size()
        x -= w / 2
        y -= h / 2
        surface.blit(self.image, (x, y))

    def is_over(self, point):  
        point_x, point_y = point
        x, y = self.position
        w, h = self.image.get_size()
        x -= w /2
        y -= h / 2
        in_x = point_x >= x and point_x < x + w
        in_y = point_y >= y and point_y < y + h
        return in_x and in_y       
def bcd(x,y) :
        mpos=[]
        mpos=pygame.mouse.get_pos()      
        if buttons[x].is_over(mpos):              
               buttons[y].render(screen)
        else:
               buttons[x].render(screen)
buttons={}  
buttons["advice"] = Button("image/board/advice.png", (570,60))
buttons["advice_down"] = Button("image/board/advice_down.png", (570,60))
buttons["music"] = Button("image/board/music.png", (570,105))
buttons["music_down"] = Button("image/board/music_down.png", (570,105))   
buttons["lose"] = Button("image/board/lose.png", (570,440))
buttons["lose_down"] = Button("image/board/lose_down.png", (570,440))
buttons["restart"] = Button("image/board/restart.png", (570,485))
buttons["restart_down"] = Button("image/board/restart_down.png", (570,485)) 
buttons["back2"] = Button("image/board/back.png", (635,440))
buttons["back3"] = Button("image/board/back_down.png", (635,440))
buttons["redo"] = Button("image/board/redo.png", (635,105))
buttons["redo_down"] = Button("image/board/redo_down.png", (635,105))

   

         
buttons["start"] = Button("image/menu/start.png", (350,240))
buttons["start_down"] = Button("image/menu/start_down.png", (350,240))
buttons["choose"] = Button("image/menu/choose.png", (350,290))
buttons["choose_down"] = Button("image/menu/choose_down.png", (345,288)) 
buttons["help"] = Button("image/menu/help.png", (350,340))
buttons["help_down"] = Button("image/menu/help_down.png", (350,340))
buttons["exit"] = Button("image/menu/exit.png", (350,390))
buttons["exit_down"] = Button("image/menu/exit_down.png", (350,390))

buttons["simple"] = Button("image/menu/option/simple.jpg", (310,270))
buttons["csimple"] = Button("image/menu/option/csimple.jpg", (310,270))
buttons["normal"] = Button("image/menu/option/normal.jpg", (308,320))
buttons["cnormal"] = Button("image/menu/option/cnormal.jpg", (310,320))
buttons["diff"] = Button("image/menu/option/diff.jpg", (312,370))
buttons["cdiff"] = Button("image/menu/option/cdiff.jpg", (312,370))
buttons["cmusic"] = Button("image/menu/option/cmusic.jpg", (310,200))
buttons["cmusic_down"] = Button("image/menu/option/cmusic_down.png", (308,201))
buttons["imusic"] = Button("image/menu/option/music.jpg", (500,201))
buttons["imusic_down"] = Button("image/menu/option/music_down.png", (497,199)) 
buttons["musicop"] = Button("image/menu/option/musicop.jpg", (132,199)) 
buttons["back"] = Button("image/menu/option/back.jpg", (310,450)) 
buttons["back_down"] = Button("image/menu/option/back_down.png", (315,451)) 
buttons["cbg"] = Button("image/menu/option/blue.jpg", (131,120)) 
buttons["cbg_down"] = Button("image/menu/option/cbg_down.png", (131,119)) 
buttons["nandu"] = Button("image/menu/option/nandu.jpg", (130,319)) 
buttons["back1"] = Button("image/menu/option/back.png", (310,450))


