# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27.

real = float(input('Digite quanto dinheiro você tem na carteira: R$ '))
dolar = 3.27
print('Você consegue comprar US$ {:.3f} com R$ {}'.format(real/dolar, real))
