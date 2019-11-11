from validators import getFloat

print( """КМ-94 Цахло Едуард Володимирович
Варіант 22 Завдання 2

Дано А, що більше 1. Вивести найменше із цілих K, для яких сума 1 + 1/2 + ... + 1/K буде більше A, і саму цю суму.
Приклад для значення А:
A = 4 -> K = 31\n""" )

a = getFloat(input( 'Введіть значення A:' ))
while( a <= 1 ):
	a = getFloat(input( 'А повинно бути більше 1! Введіть ще раз:' ))

sumOfNumbers = 0
k = 0

while( 1 == 1 ):

	k += 1
	sumOfNumbers += 1/k

	if( sumOfNumbers >= a ): break

print( 'Значення К: ', k )
print( 'Сума: ', round( sumOfNumbers, 3 ) )