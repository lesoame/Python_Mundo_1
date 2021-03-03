# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor total da sua compra: '))
print('Parabéns você ganhou 5% de desconto e vai pagar apenas R$ {:.2f} economizando R$ {:.2f}'.format(preco*0.95, preco-(preco*0.95)))
