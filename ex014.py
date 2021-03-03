# Escreva um programa que converta uma temperatura digitada em ºC para ºF. Fórmula (0 °C × 9/5) + 32

tc = float(input('Digite um valor de temperatura em ºC: '))
tf = (tc * 9/5) + 32
print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF'.format(tc, tf))
