# -*- coding: utf-8 -*-
from matriz import Matriz


def run(matriz=None):
	options = raw_input('Entrada:')
	args = options.strip().split(' ')
	op = args[0]

	params = list()
	for a in args[1:]:
		params.append(int(a) if a.isdigit() else a)

	if op == 'I':
		matriz = Matriz(*params)
	elif op == 'X':
		return
	elif matriz:
		function = Matriz.FUNCTIONS.get(op, None)
		if function:
			try:
				getattr(matriz, function)(*params)
			except (ValueError, TypeError, IndexError):
				print u'Entre com as opções válidas de cada função'
		else:
			print u'Entre apenas com os comandos: I, C, L, V, H, K, F, S e X'
	print matriz
	run(matriz)

if __name__ == '__main__':
	run()
