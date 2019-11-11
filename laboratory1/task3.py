from math import sin
from sys import exit
from validators import getFloat

print( """КМ-94 Цахло Едуард Володимирович
Варіант 22 Завдання 3

F(x) = {

	9 - x, при x > 1,1
	sin(3x)/(x**4 + 1), при x < - 1,1

}\n""" )

x = getFloat( input('Введіть значення x таке, що менше ніж -1.1, або більше за 1.1:') )

if( x > 1.1 ):
	formula = '9 - x'
	result = eval( formula.replace( 'x', str( x ) ) )

elif( x < -1.1 ):
	formula = 'sin(3*x)/(x**4 + 1)'
	result = eval( formula.replace( 'x', str( x ) ) )

else:
	print( 'Помилковий ввод.' )
	exit()

print( 'F(x) = {}, при x = {}\nF({}) = {}'.format( formula, x, x, round( result, 3 ) ) )