# -*- coding: utf-8 -*-
import sys
import re

if len(sys.argv) != 3:
	print "El número de parámetros es incorrecto"
else:
	pattern = sys.argv[1]
	file = sys.argv[2]

	try:
		f = open(file)
		for i in f:
			if re.match(pattern, i):
				print i,
		f.close()
	except:
		print "Error en el fichero "+file