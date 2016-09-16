# -*- coding: utf-8 -*-
import unittest
from matriz import Matriz

class MatrizTestCase(unittest.TestCase):

	def test_01_create(self):
		M, N = 2, 3
		assert Matriz(M, N).data == [[0] * M for i in range(N)]

	def test_02_clean(self):
		pass

	def test_03_color(self):
		pass

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
