"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    * 326 = 3 centenas, 2 dezenas e 6 unidades
    * 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
import sys


def analisa_num(num):
    num = str(num)
    if len(num) == 4:
        milhar, centena, dezena, unidade = int(
            num[0]), int(num[1]), int(num[2]), int(num[3])
        string = f'{milhar} milhar, {centena} centena, {dezena} dezena e {unidade} unidade'
        print(string)

    elif len(num) == 3:
        centena, dezena, unidade = int(num[0]), int(num[1]), int(num[2])
        title_c, title_d, title_u = 'centena', 'dezena', 'unidade'
        if centena > 1:
            title_c = 'centenas'
        if dezena > 1:
            title_d = 'dezenas'
        if unidade > 1:
            title_u = 'unidades'
        string = f'{centena} {title_c}, {dezena} {title_d} e {unidade} {title_u}'
        print(string)

    elif len(num) == 2:
        dezena, unidade = int(num[0]), int(num[1])
        title_d, title_u = 'dezena', 'unidade'
        if dezena > 1:
            title_d = 'dezenas'
        if unidade > 1:
            title_u = 'unidades'
        string = f'{dezena} {title_d} e {unidade} {title_u}'
        print(string)

    elif len(num) == 1:
        unidade = int(num[0])
        if unidade > 1:
            title = 'unidades'
        else:
            title = 'unidade'
        string = f'{unidade} {title}'
        print(string)
    else:
        print(f'O numero {num} não atende as expecificações do programa')
        sys.exit(1)


if __name__ == '__main__':
    lista_test = [326, 300, 100, 320, 310, 305, 301,
                  101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]
    for i in lista_test:
        analisa_num(i)
