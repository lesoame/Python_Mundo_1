# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

# O in não é um método, ele é um OPERADOR LÓGICO DE ANÁLISE do Python
# O in significa "Existe silva na variável nome?", o lower é um método de transformação da str p/ minúsculo



