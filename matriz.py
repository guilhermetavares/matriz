# -*- coding: utf-8 -*-


class Matriz(object):
	data = []
	directions = (
		(-1, -1), (-1, 0), (-1, 1),
		(0, -1), (0, 0), (0, 1),   
		(1, -1), (1, 0), (1, 1),
	)
	
	def __init__(self, M, N):
		self.M = M
		self.N = N
		self.clean()

	def __str__(self):
		return '\n'.join([''.join(i) for i in self.data])

	def fill(self, x, y, color):
		try:
			self.data[y][x] = str(color)
			return color
		except IndexError:
			return False

	def clean(self):
		self.data = [['O'] * self.M for i in range(self.N)]

	def item(self, x, y):
		try:
			return self.data[y - 1][x - 1]
		except:
			return None

	def interval(self, starts, ends):
		return range(starts, ends + 1)

	def color(self, x, y, color):
		return self.fill(x - 1, y - 1, color)

	def vertical_draw(self, x, y1, y2, color):
		for y in self.interval(y1, y2):
			self.color(x, y, color)

	def horizontal_draw(self, x1, x2, y, color):
		for x in self.interval(x1, x2):
			self.color(x, y, color)

	def retangular_draw(self, x1, y1, x2, y2, color):
		for x in self.interval(x1, x2):
			self.vertical_draw(x, y1, y2, color)

	def region_draw(self, x, y, color, original_color=None):
		if original_color is None:
			original_color = self.item(x, y)

		if self.item(x, y) == original_color:
			self.color(x, y, color)

			for s_x, s_y in self.directions:
				self.region_draw(x + s_x, y + s_y, color, original_color)

	def write(self, filename):
		arq = open(filename, 'w')
		arq.write(u'{0}'.format(self))
		arq.close()
		return arq
