# -*- coding: utf-8 -*-
import os
import sys
from time import time

t1 = time()

ficheros = {}

def countfiles(dir):
  listado = os.listdir(dir)
  for i in listado:
    item = os.path.join(dir, i)
    if os.path.isfile(item.lower()):
      if i in ficheros:
        ficheros[i] += 1
      else:
        ficheros[i] = 1
    elif os.path.isdir(item):
      countfiles(item)

if len(sys.argv) != 3:
  exit(1)
else:
  if os.path.isfile(sys.argv[2]):
    print "Has pasado un fichero, no puedo hacer nada más con esto :P"
    print sys.argv[2]
  else:
    countfiles(sys.argv[2])
    t2 = time()
    for i in ficheros.items():
      if i[1] >= sys.argv[1]:
        print i[0]+"  "+str(i[1])
    print len(ficheros)
    print t2 - t1