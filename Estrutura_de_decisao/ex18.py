"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
import sys


def check_anoBissexto(ano):
    caso1 = ano % 4
    caso2 = ano % 100
    caso3 = ano % 400

    if caso1 == 0 and caso2 != 0:
        return True
    elif caso1 != 0 and caso3 == 0:
        return True
    else:
        return False


def check_data(ano):
    ano = ano.split('/')
    dia, mes, ano = int(ano[0]), int(ano[1]), int(ano[2])
    bissexto = check_anoBissexto(int(ano))
    mes_30 = [4, 6, 9, 11]
    mes_31 = [1, 3, 5, 7, 8, 10, 12]

    if len(str(dia)) < 1 or len(str(mes)) < 1 or len(str(ano)) != 4:
        print('Data invalida')
        sys.exit(1)

    if dia not in range(1, 32) or mes not in range(1, 13):
        print('Data invalida')
        sys.exit(1)

    if mes in mes_30 and dia not in range(1, 31):
        print(f'Data invalida {dia}/{mes}/{ano}')
    elif mes == 2:
        if bissexto == True and dia not in range(1, 30):
            print(f'Data invalida {dia}/{mes}/{ano}')
        elif bissexto == False and dia not in range(1, 29):
            print(f'Data invalida {dia}/{mes}/{ano}')
        else:
            print(f'Data valida {dia}/{mes}/{ano}')
    elif mes in mes_31 and dia in range(1, 32):
        print(f'Data valida {dia}/{mes}/{ano}')
    elif mes in mes_30 and dia in range(1, 31):
        print(f'Data valida {dia}/{mes}/{ano}')


if __name__ == '__main__':
    while True:
        try:
            ano = str(input('Digite uma data no seguinte formato dd/mm/aaaa: '))
            check_data(ano)
            break
        except ValueError as error:
            print(error)
