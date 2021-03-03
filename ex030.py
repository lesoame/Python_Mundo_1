# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
# Conceito: O resto da divisão de qualquer número PAR por 2 é zero e o resto da divisão de qualquer número ÍMPAR por 2 é um.

num = int(input('Digite qualquer número inteiro: '))
resultado = num % 2
if resultado == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))
