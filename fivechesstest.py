#-*-coding:utf-8-*-
import pygame
pygame.init()
from pygame.locals import *
from sys import exit
from spygame import *
from pos import *
from window import *
import os
import os.path
from music import *
from chessboard import *
from button import *
from searcher import *
pygame.init()
import win32ui
def gamestart (DEPTH):      
    b = chess()
    b.reset()
    board=b.board()
    s = searcher()
    s.board = b.board()
    paused = False 
    result=0   
    t=0
    global r
    r=1
    flag=1 #判断悔棋
    fxm=0 #防止xm，ym未赋值
    first=0# 去掉第一次悔棋后棋子上的红色标志
    reflag=0 #悔棋只能点一次有效
    while True: 
        turn=1      
        bcd('lose','lose_down')
        bcd('restart','restart_down')
        bcd('music','music_down')
        bcd('advice','advice_down')
        bcd('back2','back3')
        bcd('redo','redo_down')
        update()
        if flag%2==1:
            saveimage(screen, 'reboard1.png')
            reboard1=board
            if fxm>0:
               xm1,ym1=xm,ym
               xn1,yn1=xn,yn
        else :
            saveimage(screen, 'reboard2.png')
            reboard2=board
            xm2,ym2=xm,ym
            xn2,yn2=xn,yn
        event = pygame.event.wait()    
        if event.type == QUIT:            
                 exit()  
        if event.type == MOUSEBUTTONDOWN:
                    if buttons["lose_down"].is_over(event.pos): #认输               
                           screen.blit(wwin,(550,193))   
                           win_sound.play()
                           result=2
                    if buttons["restart_down"].is_over(event.pos): #重开
                           r=0
                           break    
                    if buttons["music_down"].is_over(event.pos): #音乐
                        if paused:
                            pygame.mixer.music.unpause()
                            paused = False
                        else:
                            pygame.mixer.music.pause()
                            paused = True  
                    if buttons["advice_down"].is_over(event.pos): #提示
                            score, xs, ys = s.search(1, DEPTH)    
                            x,y=bpos(xs,ys)       
                            if t==1:
                                bg1.blit(black,(xn,yn))     
                            bg1.blit(nblack,(x,y))
                            xn,yn=x,y
                            chess_sound.play()   
                            update()      
                            board[xs][ys]=1
                            result=b.check()
                            turn = 2
                            b.win(result)    
                    if buttons["back3"].is_over(event.pos): #认输               
                            break    
                    if buttons["redo_down"].is_over(event.pos): #悔棋 
                      if reflag==0:
                        if fxm>0:                          
                          if fxm==1:
                                r=0
                                reflag=1
                                break
                          if flag%2==1:
                              b1=image('reboard2.png')
                              screen.blit(b1, (0,0))
                              b.chboard(reboard2)
                              board[xs][ys]=0
                              board[row][col]=0
                              s.board=board
                              flag-=1
                              if fxm>0:
                                xm,ym=xm2,ym2
                                xn,yn=xn2,yn2  
                              reflag=1                           
                          else :
                              b2=image('reboard1.png')
                              screen.blit(b2, (0,0))
                              b.chboard(reboard1)
                              board[xs][ys]=0
                              board[row][col]=0
                              s.board=board
                              flag-=1
                              if fxm>1:
                                xm,ym=xm1,ym1
                                xn,yn=xn1,yn1
                              reflag=1
                                                        
        if turn==1:     
          if result==0:                                       
           if  event.type== MOUSEBUTTONDOWN:     #判断落子                            
              x,y,xs,ys=pos()#获得棋子位置和坐标
              if xs<=14 and ys <=14:
                  if board[xs][ys] == 0:   
                     if t==1 and fxm!=1 :
                       bg1.blit(black,(xn,yn))        
                     bg1.blit(nblack,(x,y)) 
                     if first==1:
                          bg1.blit(black,(xn,yn))
                     xn,yn=x,y
                     chess_sound.play()
                     update()
                     board[xs][ys]=1
                     result=b.check()
                     turn =2
                     b.win(result)
                                                                              
        if turn ==2:
            score, row, col = s.search(2, DEPTH)    
            x,y=bpos(row,col)  
            if t==1 and fxm!=1  :
                bg1.blit(white,(xm,ym))     
            bg1.blit(nwhite,(x,y))
            if first==1:
                bg1.blit(white,(xm,ym))
            xm,ym=x,y
            chess_sound.play()   
            update()      
            board[row][col]=2
            result=b.check()
            b.win(result)
            t=1  
            flag+=1
            fxm+=1
            first+=1
            reflag=0
                                                                        
def menus(DEPTH,menu):
   paused = False
   flag=0
   F=0
   while True:
       for event in pygame.event.get():     
         if event.type == QUIT:            
               exit()  
         if F==1:
               screen.blit(help_page,(0,0))
               bcd('back1','back_down')
               update()
               if event.type == MOUSEBUTTONDOWN:
                   if buttons["back_down"].is_over(event.pos):  
                       F=0
                       continue
         elif F==2:
               screen.blit(choose_page,(0,0))
               bcd('back','back_down')
               buttons["musicop"].render(screen)
               buttons["nandu"].render(screen)
               bcd('imusic','imusic_down')
               bcd('cmusic','cmusic_down')
               bcd('cbg','cbg_down')  
               if DEPTH==1:
                   buttons["csimple"].render(screen)
               else :
                  buttons["simple"].render(screen)
               if DEPTH==2:
                   buttons["cnormal"].render(screen)
               else :
                  buttons["normal"].render(screen)
               if DEPTH==3:
                   buttons["cdiff"].render(screen)
               else :
                  buttons["diff"].render(screen)
               if event.type == MOUSEBUTTONDOWN:
                   if buttons["csimple"].is_over(event.pos):                       
                              DEPTH=1
                   if buttons["cnormal"].is_over(event.pos):                              
                              DEPTH=2
                   if buttons["cdiff"].is_over(event.pos):                             
                              DEPTH=3
                   if buttons["cmusic"].is_over(event.pos): 
                          dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
                          dlg.SetOFNInitialDir('E:/Python') # 设置始显示目录
                          dlg.DoModal()
                          filename = dlg.GetPathName()
                          name=filename.split('.')
                          if filename!='' :
                             if name[1]=='mp3' or name[1]=='WAV':
                               pygame.mixer.music.load(filename)
                               pygame.mixer.music.play()
                   if buttons["imusic_down"].is_over(event.pos): #音乐
                        if paused:
                            pygame.mixer.music.unpause()
                            paused = False
                        else:
                            pygame.mixer.music.pause()
                            paused = True  
                   if buttons["cbg_down"].is_over(event.pos): 
                          dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
                          dlg.SetOFNInitialDir('E:/Python') # 设置始显示目录
                          dlg.DoModal()
                          bgfilename = dlg.GetPathName()
                          bgname=bgfilename.split('.')
                          if bgfilename!='' :
                               menu=image(bgfilename)
                   if buttons["back_down"].is_over(event.pos):  
                       F=0
                       continue
               update()                   
         else:
           mpos=[]
           mpos=pygame.mouse.get_pos()                              
           screen.blit(menu,(0,0))   
           bcd('start','start_down') 
           bcd('choose','choose_down') 
           bcd('help','help_down')    
           bcd('exit','exit_down')         
           update()
           if event.type == MOUSEBUTTONDOWN:
             if buttons["start"].is_over(event.pos):
                 chess_sound.play()  
                 flag=1  
                 break 
             if buttons["exit_down"].is_over(event.pos):
                 exit()
             if buttons["help_down"].is_over(event.pos):
                 F=1
             if buttons["choose_down"].is_over(event.pos):
                 F=2                  
       if flag==1:
               break   
   return DEPTH,menu
            
if __name__=='__main__':
    d,menu=menus(1,menu) 
    while True:   
      screen.blit(bg, (0,0))#刷新棋盘背景图  
      update()
      gamestart(d)
      if r==1:
         d,menu=menus(d,menu)
   
        
         
          
                            