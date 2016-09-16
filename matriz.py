# -*- coding: utf-8 -*-


class Matriz(object):
	data = None
	
	def __init__(self, M, N):
		self.data = [[0] * M for i in range(N)]

	def __str__(self):
		return u'{0}'.format(self.data)

	def color(self, x, y, color):
		try:
			self.data[x][y] = color
			return color
		except IndexError:
			return False