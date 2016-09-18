# -*- coding: utf-8 -*-
import unittest
from matriz import Matriz


class MatrizTestCase(unittest.TestCase):

	def test_01_create(self):
		assert Matriz(1, 'c').data == []
		M, N = 5, 6
		assert Matriz(M, N).data == [['O'] * M for i in range(N)]

	def test_02_color(self):
		M, N = 5, 6
		matriz = Matriz(M, N)
		assert matriz.color(2, 3, 'A') == 'A'
		assert matriz.color(13, 3, 'C') == False
		assert matriz.item(2, 3) == 'A'
		assert matriz.item(13, 3) == None

	def test_03_clean(self):
		M, N = 5, 6
		matriz = Matriz(M, N)
		matriz.color(1, 2, 'C')
		matriz.color(1, 1, 'E')
		assert matriz.data != [['O'] * M for i in range(N)]
		matriz.clean()
		assert matriz.data == [['O'] * M for i in range(N)]

	def test_04_horizontal_draw(self):
		M, N = 5, 6
		matriz = Matriz(M, N)
		matriz.horizontal_draw(3, 4, 2, 'Z')
		assert matriz.item(2, 2) != 'Z'
		assert matriz.item(3, 2) == 'Z'
		assert matriz.item(4, 2) == 'Z'
		assert matriz.item(5, 2) != 'Z'

	def test_05_vertical_draw(self):
		M, N = 5, 6
		matriz = Matriz(M, N)
		assert matriz.interval(3, 4) == [3, 4]
		matriz.vertical_draw(2, 3, 4, 'W')
		assert matriz.item(2, 2) != 'W'
		assert matriz.item(2, 3) == 'W'
		assert matriz.item(2, 4) == 'W'
		assert matriz.item(2, 5) != 'W'

	def test_06_retangular_draw(self):
		M, N = 10, 9
		matriz = Matriz(M, N)
		matriz.retangular_draw(2, 7, 8, 8, 'E')
		assert matriz.item(1, 2) != 'E'
		assert matriz.item(2, 7) == 'E'
		assert matriz.item(2, 8) == 'E'
		assert matriz.item(3, 8) == 'E'
		assert matriz.item(2, 9) != 'E'

	def test_07_region_draw(self):
		M, N = 10, 9
		matriz = Matriz(M, N)
		matriz.region_draw(9, 9, 'R')
		assert matriz.data == [['R'] * M for i in range(N)]

	def test_08_image_draw(self):
		M, N = 10, 9
		matriz = Matriz(M, N)
		matriz.region_draw(9, 9, 'R')
		matriz.write('tests.bmp')
		r = open('tests.bmp').read()
		assert r == str(matriz)

	def test_09_input_firts_sequence(self):
		one = [
			['O', 'O', 'O', 'O', 'O'],
			['O', 'O', 'O', 'O', 'O'],
			['O', 'A', 'O', 'O', 'O'],
			['O', 'O', 'O', 'O', 'O'],
			['O', 'O', 'O', 'O', 'O'],
			['O', 'O', 'O', 'O', 'O'],
		]
		matriz = Matriz(5, 6)
		matriz.color(2, 3, 'A')
		matriz.write('tests_1_1.bmp')
		r = open('tests_1_1.bmp').read()
		one = '\n'.join([''.join(i) for i in one])
		assert r == str(matriz)
		assert r == one
		assert str(matriz) == one

		two = [
			['J', 'J', 'J', 'J', 'J'],
			['J', 'J', 'Z', 'Z', 'J'],
			['J', 'W', 'J', 'J', 'J'],
			['J', 'W', 'J', 'J', 'J'],
			['J', 'J', 'J', 'J', 'J'],
			['J', 'J', 'J', 'J', 'J'],
		]
		matriz.vertical_draw(2, 3, 4, 'W')
		matriz.horizontal_draw(3, 4, 2, 'Z')
		matriz.region_draw(3, 3, 'J')
		matriz.write('tests_1_2.bmp')
		r = open('tests_1_2.bmp').read()
		two = '\n'.join([''.join(i) for i in two])
		assert r == str(matriz)
		assert r == two
		assert str(matriz) == two

	def test_10_input_second_sequence(self):
		one = [
			['J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J'],
			['J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J'],
			['J', 'W', 'J', 'J', 'A', 'J', 'J', 'J', 'J', 'J'],
			['J', 'W', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J'],
			['Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z'],
			['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
			['R', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'R', 'R'],
			['R', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'R', 'R'],
			['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
		]
		matriz = Matriz(10, 9)
		matriz.color(5, 3, 'A')
		matriz.vertical_draw(2, 3, 4, 'W')
		matriz.horizontal_draw(1, 10, 5, 'Z')
		matriz.region_draw(3, 3, 'J')
		matriz.retangular_draw(2, 7, 8, 8, 'E')
		matriz.region_draw(9, 9, 'R')
		matriz.write('tests_2.bmp')
		r = open('tests_2.bmp').read()
		one = '\n'.join([''.join(i) for i in one])
		assert r == str(matriz)
		assert one == r
		assert str(matriz) == one

if __name__ == '__main__':
	unittest.main()
