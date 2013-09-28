# -*- coding: cp1251 -*-
#
#
class Mesh:
	def __init__ (self):
		
		self.title = ''				# заголовок модели
		self.dimension = 'm'		# размерность координат

		self.domains= []			# список доменов
		self.boundaries= []			# список границ
		self.node_sets= []			# список наборов узлов
		self.element_sets= []		# список наборов элементов
		
		self.nodes = []				# список узлов
		self.elements = []			# список элементов
		
		self.keys = []				# список ключей
		
class Node:
	def __init__ (self):
		
		self.values = (0.0,0.0,0.0)


class Element:
	def __init__ (self):
		self.type = ''		# тип элемента: tria3,quad4,tetra4,tetra10,hexa8,hexa20
		self.values = []
		
		
class NodeSet:		
	def __init__ (self):

		self.title = ''	
		self.values = []			# список id узлов 
		
class ElementSet:		
	def __init__ (self):

		self.title = ''	
		self.values = []			# список id элементов
		
		
		
class Domain:
	
	def __init__ (self):
	
		self.title = ''
		
		self.boundaries = []	# список id границ
		self.elements = []   	# список id элементов 


class Boundary:
	
	def __init__ (self):
		
		self.title = ''
		self.elements = []		# список id элементов 
	
	
class Key:

	def __init__ (self):
		
		self.name = ''
		self.values = []
	

				