# -*- coding: utf-8 -*-
import unittest
from matriz import Matriz

class MatrizTestCase(unittest.TestCase):

	def test_01_create(self):
		M, N = 2, 3
		assert Matriz(M, N).data == [[0] * N for i in range(M)]

	def test_02_color(self):
		matriz = Matriz(2, 3)
		assert matriz.color(3, 3, 'C') == False
		assert matriz.color(1, 2, 'C') == 'C'
		assert matriz.data[1][2] == 'C'

	def test_03_clean(self):
		matriz = Matriz(2, 3)

	def test_04_horizontal_draw(self):
		pass

	def test_05_vertical_draw(self):
		pass

	def test_06_retangular_draw(self):
		pass

	def test_07_region_draw(self):
		pass

	def test_08_image_draw(self):
		pass

	def test_09_exit(self):
		pass

if __name__ == '__main__':
	unittest.main()
