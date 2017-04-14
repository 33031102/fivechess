#!/usr/bin/python
#-*-coding:utf-8-*-
import sys,time
from window import *
from music import * 
class chess (object):
	def __init__ (self, forbidden = 0):
		self.__board = [ [ 0 for n in xrange(15) ] for m in xrange(15) ]
		self.__dirs = ( (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), \
			(1, -1), (0, -1), (-1, -1) )
		self.DIRS = self.__dirs
	
	def reset (self):
		for j in xrange(15):
			for i in xrange(15):
				self.__board[i][j] = 0
		return 0
	
	def get (self, row, col):
		if row < 0 or row >= 15 or col < 0 or col >= 15:
			return 0
		return self.__board[row][col]

	def put (self, row, col, x):
		if row >= 0 and row < 15 and col >= 0 and col < 15:
			self.__board[row][col] = x
		return 0
	
	def check (self):
		board = self.__board
		dirs = ((1, -1), (1, 0), (1, 1), (0, 1))
		for i in xrange(15):
			for j in xrange(15):
				if board[i][j] == 0: continue
				id = board[i][j]
				for d in dirs:
					x, y = j, i
					count = 0
					for k in xrange(5):
						if self.get(y, x) != id: break
						y += d[0]
						x += d[1]
						count += 1
					if count == 5:
						r, c = i, j
						for z in xrange(5):
							r += d[0]
							c += d[1]
						return id
		return 0
	
	def board (self):
		return self.__board
	def chboard(self,b):
		self.__board=b

	def win(self,result):
         if result==1:
            screen.blit(bwin,(550,193))
            win_sound.play()
            turn=3
            result=0 
         if result==2:
                screen.blit(wwin,(550,193))
                win_sound.play()  
                turn=3
                result=0 
         update() 