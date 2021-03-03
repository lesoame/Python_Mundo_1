# Escreva um programa leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Digite a velocidade do seu carro: '))
multa = (vel-80)*7
if vel > 80:
    print('Sua velocidade excedeu {}km/h e sua multa foi de R${:.2f}'.format(vel-80, multa))
else:
    print('Sua velocidade está dentro do permitido, continue assim!')
