#-*-coding:utf-8-*-
from evaluation import *
class searcher(object):
	def __init__(self):
		self.evaluator = evaluation()
		self.board = [ [ 0 for n in xrange(15) ] for i in xrange(15) ]
		self.gameover = 0
		self.overvalue = 0
		self.maxdepth = 3

	def genmove(self, turn):
		moves = []
		board = self.board
		POSES = self.evaluator.POS
		flag=0
		mini,maxi,minj,maxj=0,0,0,0
		for i in xrange(15):
			for j in xrange(15):
				if board[i][j] != 0:
						flag+=1
						if flag==1:
								mini,maxi,minj,maxj = i,i,j,j                        							
						if i < mini:
								mini = i
						if i>maxi:
								maxi = i
						if j<minj:
								minj = j
						if j>maxj:
								maxj = j
		if mini<=2:
			mini=0
		else:
			mini=mini-2
		if minj<=2:
			minj=0
		else:
			minj=minj-2
		if maxj>=13:
			maxj=15
		else:
			maxj=maxj+2

		if maxi>=13:
			maxi=15
		else:
			maxi=maxi+2

		for i in xrange(mini,maxi):
			for j in xrange(minj,maxj):
				if board[i][j] == 0:
					score = POSES[i][j]
					moves.append((score, i, j))
		moves.sort()
		moves.reverse()
		return moves
		
	def __search(self, turn, depth, alpha = -0x7fffffff, beta = 0x7fffffff):

		if depth <= 0:
			score = self.evaluator.evaluate(self.board, turn)
			return score
		score = self.evaluator.evaluate(self.board, turn)
		if abs(score) >= 9999 and depth < self.maxdepth: 
			return score	
		moves = self.genmove(turn)
		bestmove = None

		for score, row, col in moves:	
			self.board[row][col] = turn					
			nturn = turn == 1 and 2 or 1	
			score = - self.__search(nturn, depth - 1, -beta, -alpha)
			self.board[row][col] = 0
			if score > alpha:
				alpha = score
				bestmove = (row, col)
				if alpha >= beta:
					break		
		if depth == self.maxdepth and bestmove:
			self.bestmove = bestmove
		return alpha

	def search(self, turn, depth):
		self.maxdepth = depth
		self.bestmove = None
		score = self.__search(turn, depth)
		if abs(score) > 8000:
			self.maxdepth = depth
			score = self.__search(turn, 1)
		row, col = self.bestmove
		return score, row, col
