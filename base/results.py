# -*- coding: cp1251 -*-
#
#
class Results:
	def __init__ (self):
		
		self.title = ''				# заголовок модели
		self.system = 'SI'		# размерность координат

		self.node_scalar= []			# список скалярных полей по узлам
		self.element_scalar= []			# список скалярных полей по элементам 

		self.node_vector= []			# список векторных полей по узлам
		self.element_vector= []			# список векторных полей по элементам 
		
class ScalarSet:
	def __init__ (self):
		self.title = ''					# имя поля результатов
		self.dimension =''				# размерность
		
		self.values = []				# значения. id узла или элемента принимается по номеру значения в списке

class VectorSet:
	def __init__ (self):
		self.title = ''					# имя поля результатов
		self.dimension =''				# размерность
		
		self.values = []

		