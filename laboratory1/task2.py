from math import sqrt
from validators import getInt

print( """КМ-94 Цахло Едуард Володимирович
Варіант 22 Завдання 2

Ввести координати чотирьох точок А1 (х1, у1), А2 (x2, у2), А3 (x3, у3), А4 (х4, у4).
Визначити, чи будуть вони вершинами паралелограма.\n""" )

print( 'Введіть координати в один рядок:' )

coords = [ getInt('x1": '), getInt('y1": '), getInt('x2": '), getInt('y2": '),
getInt('x3": '), getInt('y3": '), getInt('x4": '), getInt('y4": ') ] # Координати: [ x1, y1, ... ]
vectors = []

for i in range( 0, len(coords), 4 ): # Створюю вектори з координатами [ x, y ] із двух протилежних прямих
	vectors.append( [ coords[i+2] - coords[i], coords[i+3] - coords[i+1] ] )

v = vectors # Скорочення

isColinear = ( v[0][0] / v[1][0] == v[0][1] / v[1][1] ) # Чи колінеарні вектори
isEqual = sqrt( v[0][0]**2 + v[0][1]**2 ) == sqrt( v[1][0]**2 + v[1][1]**2 ) # Чи рівні вони

if( isColinear and isEqual ):
	print( 'Так. Ці точки вершини паралелограма.' )

else:
	print( 'Ні. Ці точки не є вершинами паралелограма.' )