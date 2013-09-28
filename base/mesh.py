# -*- coding: cp1251 -*-
#
#
class Mesh:
	def __init__ (self):
		
		self.title = ''				# ��������� ������
		self.dimension = 'm'		# ����������� ���������

		self.domains= []			# ������ �������
		self.boundaries= []			# ������ ������
		self.node_sets= []			# ������ ������� �����
		self.element_sets= []		# ������ ������� ���������
		
		self.nodes = []				# ������ �����
		self.elements = []			# ������ ���������
		
		self.keys = []				# ������ ������
		
class Node:
	def __init__ (self):
		
		self.values = (0.0,0.0,0.0)


class Element:
	def __init__ (self):
		self.type = ''		# ��� ��������: tria3,quad4,tetra4,tetra10,hexa8,hexa20
		self.values = []
		
		
class NodeSet:		
	def __init__ (self):

		self.title = ''	
		self.values = []			# ������ id ����� 
		
class ElementSet:		
	def __init__ (self):

		self.title = ''	
		self.values = []			# ������ id ���������
		
		
		
class Domain:
	
	def __init__ (self):
	
		self.title = ''
		
		self.boundaries = []	# ������ id ������
		self.elements = []   	# ������ id ��������� 


class Boundary:
	
	def __init__ (self):
		
		self.title = ''
		self.elements = []		# ������ id ��������� 
	
	
class Key:

	def __init__ (self):
		
		self.name = ''
		self.values = []
	

				