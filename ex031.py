# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem
# cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longes.

# -------------------------- Utilizando a condição COMPOSTA -----------------------

d = float(input('Qual a distância da sua viagem em km? '))
if d <= 200:
    preco = d * 0.5
else:
    preco = d * 0.45
print('O preço da sua viagem considerando {:.0f}km é de R${:.2f}'.format(d, preco))

# -------------------------- Utilizando a condição SIMPLIFICADA -----------------------

d1 = float(input('Qual a distância da sua viagem em km? '))
preco = d1 * 0.5 if d1 <= 200 else d1 * 0.45
print('O preço da sua passagem considerando {:.0f}km é de R${:.2f}'.format(d1, preco))
