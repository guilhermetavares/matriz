# -*- coding: utf-8 -*-
from matriz import Matriz


def run(matriz=None):
	options = raw_input('Entrada:')
	args = options.split(' ')
	op = args[0]
	if op == 'I':
		matriz = Matriz(int(args[1]), int(args[2]))
	elif op == 'X':
		return
	elif matriz:
		if op == 'L':
			matriz.color(int(args[1]), int(args[2]), args[3])
		elif op == 'F':
			matriz.region_draw(int(args[1]), int(args[2]), args[3])
		elif op == 'S':
			matriz.write(args[1])
		elif op == 'V':
			matriz.vertical_draw(int(args[1]), int(args[2]), int(args[3]), args[4])
		elif op == 'H':
			matriz.horizontal_draw(int(args[1]), int(args[2]), int(args[3]), args[4])
		elif op == 'K':
			matriz.retangular_draw(int(args[1]), int(args[2]), int(args[3]), int(args[4]), args[5])
		elif op == 'C':
			matriz.clean()
	else:
		print u'Entre apenas com os comandos: I, C, L, V, H, K, F, S e X'
		run(matriz)
	print matriz
	run(matriz)

if __name__ == '__main__':
	run()
