# -*- coding: cp1251 -*-
#
#
class Results:
	def __init__ (self):
		
		self.title = ''				# ��������� ������
		self.system = 'SI'		# ����������� ���������

		self.node_scalar= []			# ������ ��������� ����� �� �����
		self.element_scalar= []			# ������ ��������� ����� �� ��������� 

		self.node_vector= []			# ������ ��������� ����� �� �����
		self.element_vector= []			# ������ ��������� ����� �� ��������� 
		
class ScalarSet:
	def __init__ (self):
		self.title = ''					# ��� ���� �����������
		self.dimension =''				# �����������
		
		self.values = []				# ��������. id ���� ��� �������� ����������� �� ������ �������� � ������

class VectorSet:
	def __init__ (self):
		self.title = ''					# ��� ���� �����������
		self.dimension =''				# �����������
		
		self.values = []

		