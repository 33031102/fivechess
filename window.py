#-*-coding:utf-8-*-
from spygame import *
from pygame.locals import *
bg=image('image/board/board1.png')#背景图的对象
menu=image('image/background/red.jpg')#主菜单
help_page=image('image/menu/help/help_page.png')#帮助页面
black=image('image/board/black.png')#黑子图片的对象
white=image('image/board/white.png')#白字图片的对象
bwin=image('image/board/bwin.png')#白棋赢
wwin=image('image/board/wwin.png')#黑棋赢
nblack=image('image/board/nblack.png')
nwhite=image('image/board/nwhite.png')
choose_page=image('image/background/b2.jpg')



screen=set((670,537))#建立游戏窗口并设置大小
title("five chess")#窗口标题
bg1=screen.subsurface((3,3), (525,525))#建立子图层
update()
