# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras no total (sem considerar espaços).
# Quantas letras tem o primeiro nome.
# Obs:. A função .strip exclui todos os espaços que o usuário possa colocar antes da primeira palavra e depois da última.
# Obs:. A função .split() separa todas as palavras de uma str por espaços e as coloca dentro de uma lista.

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu sobrenome é {} e ele tem {} letras'.format(separa[1], len(separa[1])))



