# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa.

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))

from math import hypot

co1 = float(input('Digite o valor do cateto oposto: '))
ca2 = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co1, ca2)
print('A hipotenusa vai medir {:.2f}'.format(hi))





