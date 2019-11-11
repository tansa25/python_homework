from validators import *

print( """КМ-94 Цахло Едуард Володимирович
Варіант 22 Завдання 1

Знайти алгебраїчну суму ( ( 2*x + 1 )**i / ( x - 1 ) ) ), де n та x вводить користувач, а i - індекс сумування.\n""" )

limit = getInt(input( 'Введіть натуральне число N:' )) # >= 1
while( limit < 1 ):
	limit = getInt(input( 'N повинно бути додатнім натуральним числом! Введіть ще раз:' ))

x = getFloat(input( 'Введіть такий X, що більше 1:' )) # > 1
while( x <= 1 ):
	x = getFloat(input( 'X повинен бути більше 1! Введіть ще раз:' ))

print( 'Відповідь:' )

answer = sum( [ ( ( 2*x + 1 )**index / ( x - 1 ) ) for index in range(limit) ] )

print( answer )