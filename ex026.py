# Faça um programa que leia a frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" aparece {} vezes na sua frase'.format(frase.count('A')))
print('A letra "a" aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "a" aparece a última vez na posição {}'.format(frase.rfind('A')+1))


