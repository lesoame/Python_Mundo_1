# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city = str(input('Em que cidade você nasceu? ')).strip()
print(city[:5].upper() == 'SANTO')

# O .strip() serve para eliminar os espaços tanto antes como após o término do nome da cidade
# O .upper() serve para transformar a variável city toda em maiúscula, assim se o usuário digitar tudo em minúsculo,
# o operador lógico booleano vai ser True, pois transformou para maiúsculo que é a minha condição




