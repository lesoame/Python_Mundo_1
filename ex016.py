# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127, o nº 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um valor qualquer: '))
print('A parte inteira de {} é igual a {}'.format(num, trunc(num)))

num1 = float(input('Digite um número: '))
print('A parte inteira do número {} é igual a {}'.format(num1, int(num1)))

