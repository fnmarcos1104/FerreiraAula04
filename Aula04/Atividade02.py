import os

os.system('cls')

resp = input('Insira F para Feminino e M para Masculino: ').upper()


if resp != '':
    g = resp
    if g == 'M':
        print('Masculino')
    elif g == 'F':
        print('Feminino')
    else:
        print('Caracter inválido.')
else:
    print('Insira uma das opcões')