# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.


# Utilizando a condição composta

from random import randint  # Ou seja, do módulo/biblioteca random eu vou utilizar apenas a função randint
from time import sleep

n = randint(0, 5)  # Faz o computador "PENSAR"
num = int(input('Chute um número de 0 a 5: '))  # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(1)
if num == n:
    print('Você acertou! PARABÉNS!')
else:
    print('Você errou! TENTE MAIS UMA VEZ!')

# Utilizando a condição simplificada
