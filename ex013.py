# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s1 = float(input('Digite aqui o seu salário: R$ '))
s2 = s1 * 1.15
print('Você recebeu 15% de aumento no seu salário de R$ {:.2f}, agora seus vencimentos são de R$ {:.2f}.'.format(s1, s2))
