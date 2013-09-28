# -*- coding: cp1251 -*-
#
#	ls-dyna nodout file reader
#
import mesh
import results


def create_box ():
	
	box = mesh.Mesh( )
	box.title = 'Box mesh'
	
	# создать список узлов
	for i in xrange (10):
		x = i
		for j in xrange (10):
			y = j
			for k in xrange (10):
				z = k
				node = mesh.Node ()
				node.values = (x,y,z)
				box.nodes.append (node)
				
	# создать список элементов 
	for i in xrange (9):
		
		el = mesh.Element ()
		el.type = 'hexa8'
		el.values = [i,i+1,10+i,11+i, 100+i,100+i+1,100+10+i,100+11+i]
		
		box.elements.append (el)
	
	# создать граничный элемент
	inlet_element= mesh.Element ()
	inlet_element.type = 'quad4'
	inlet_element.values = [i,10+i, 110+i,100+i]
	box.elements.append (inlet_element)
	
	# создать границу как набор узлов 
	nset = mesh.NodeSet()
	nset.title = 'inlet_nodes'
	nset.values = [1,11,100,111]
	
	box.node_sets.append (nset)
	
	# создать набор элементов
	eset = mesh.ElementSet()
	nset.title = 'part1'
	nset.values = [1,2,3,4]

	box.element_sets.append (eset)
	
	# создать границу
	inlet = mesh.Boundary ()
	inlet.title = 'inlet'
	inlet.elements = [11]

	box.boundaries.append (inlet)
	
	# создать домен или деталь
	domain = mesh.Domain()
	domain.title = 'domain 1'
	domain.elements = [1,2]
	domain.boundaries = 0  # id границы inlet 
	
	box.domains.append (domain)
	
	return box
	
def create_scalar(amesh):

	result  =  results.Results()
	result.title = 'test results'
	
	pressure = results.ScalarSet()        # поле давления на узлах
	pressure.title = 'pressure'
	pressure.dimension = 'Pa'
	
	pl = []
	for i in amesh.nodes:
		(x,y,z) = i.values
		
		value = x**2+y**2+z**2  # функция давления
		pl.append (value)
	pressure.values = pl
		 
	temperature = results.ScalarSet()			# поле температур на элементах
	temperature.title = 'temperature'
	temperature.dimension = 'K'
	
	pl = []
	for i in amesh.elements:
		nodes = i.values
		value = 0
		for i in nodes:
			node = amesh.nodes[i]
			(x,y,z) = node.values
		
			value += x+y+z  # функция температуры 
			
		pl.append (value)
	temperature.values = pl
	
	result.node_scalar = [pressure]
	result.element_scalar = [temperature]
	
	return result

	
def create_vector(amesh, result):

	
	velocity = results.VectorSet()        # поле скоростей на узлах
	velocity.title = 'velocity'
	velocity.dimension = 'm s^-1'
	
	pl = []
	for i in amesh.nodes:
		(x,y,z) = i.values
		
		value = (x,y,z)  # функция скорости как кортеж из 3-х элементов 
		pl.append (value)
	velocity.values = pl
		 
	stress = results.VectorSet()			# поле напряжений на элементах
	stress.title = 'stress'
	stress.dimension = 'Pa'
	
	pl = []
	for i in amesh.elements:
		nodes = i.values
		valuex = valuey = valuez = 0.0
		for i in nodes:
			node = amesh.nodes[i]
			(x,y,z) = node.values
		
			valuex += x  # функция Х напряжения  
			valuey += y  # функция Х напряжения  
			valuez += z  # функция Х напряжения  
			
		pl.append ((valuex, valuey, valuez))
	stress.values = pl
	
	result.node_vector = [velocity]
	result.element_vector = [stress]
	
	return result
	
	
mesh1 = create_box ()
print mesh1 

result = create_scalar (mesh1)
print result

result = create_vector (mesh1, result)
print result