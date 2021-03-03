# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ag = float(input('Digite o valor do ângulo: '))
print('O valor do seno desse ângulo é {:.2f}'.format(sin(radians(ag))))
print('O valor do cosseno desse ângulo é {:.2f}'.format(cos(radians(ag))))
print('O valor da tangente desse ângulo é {:.2f}'.format(tan(radians(ag))))

