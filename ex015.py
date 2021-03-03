# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input('Quantos km rodados: '))
dias = int(input('Quantos dias ficou alugado? '))
preco = km * 0.15 + dias * 60
print('O total do aluguel ficou R${:.2f}'.format(preco))

