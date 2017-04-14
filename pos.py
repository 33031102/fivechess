import pygame
def pos():
      po=pygame.mouse.get_pos()
      x=po[0]
      y=po[1]
      xm=(x-18)%35
      ym=(y-18)%35
      xs=(x-18)/35
      ys=(y-18)/35        
      if xm>17.5 and ym>17.5:  
         xs=xs+1
         ys=ys+1  
      if xm<17.5 and ym<17.5:   
        pass                  
      if xm>17.5and ym<17.5:
         xs=xs+1                                         
      if xm<17.5 and ym>17.5: 
         ys=ys+1
      x= 35*xs
      y= 35*ys
         
      return x,y,xs,ys
def bpos(a,b):
    x=35*a
    y=35*b
    return x,y