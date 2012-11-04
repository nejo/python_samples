# -*- coding: utf-8 -*-
class myclase:
	def __init__ (self):
		self.a=[1,2,3,4,5,6,7,8,9] # crea lista del 1 al 9
		self.index=len(self.a)
	
	def __iter__ (self):
		self.index=len(self.a) # crea el indice, lo pone en = 9
		return self

	def next(self):
		if not self.index:
			raise StopIteration # si no tiene indice para la iteración con excepción
		self.index-=1 # va decreciendo el índice en 1 unidad
		return self.a[self.index] # devuelve el elemento de la lista de cuyo indice es el mismo numero que el indice en el que estamos actualmente

class myrange:
	def __init__ (self, start_input, end_input=0, step_input=1):
		self.start = start_input
		self.end = end_input
		self.step = step_input
	
	def __iter__ (self):
		self.index = self.start
		return self

	def next (self):
		if self.end == 0:
			if not self.index:
				raise StopIteration
			self.index -= self.step
		else:
			if self.index >= self.end:
				raise StopIteration
			self.index += self.step
		
		return self.index

class jedi_range:
	def __init__ (self, start, end=0, step=1):
		if not end:
			self.fin = start
			self.start = 0
		else:
			self.start = start
			self.fin = end
		self.step = step
	
	def __iter__ (self):
		self.curr = self.start
		return self
	
	def next (self):
		if self.curr >= self.fin:
			raise StopIteration
		res = self.curr
		self.curr += self.step
		return res
	

'''
c = myclase()
for i in c:
	print i
'''

r = myrange(10)

for i in r:
	print i
