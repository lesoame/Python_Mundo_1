# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

al = float(input('Digite a altura da parede: '))
lg = float(input('Digite a largura da parede: '))
area = al*lg
print('A área é de {}m²'.format(area))
print('Para pintar uma área de {}m², são necessários {}l de tinta.'.format(area, area/2))

