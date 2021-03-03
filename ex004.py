# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É numérico? ', a.isnumeric())
print('É somente espaços? ', a.isspace())
print('Contém somente letras maiúsculas? ', a.isupper())
print('Contém somente letras minúsculas? ', a.islower())
print('É capitalizado?', a.istitle())

