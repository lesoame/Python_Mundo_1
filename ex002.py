# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas

nome = str(input('Digite seu nome: '))
print('Seja Bem vindo(a) {}{}!!!{} É um prazer te conhecer!'.format('\033[36m', nome, '\033[m'))
