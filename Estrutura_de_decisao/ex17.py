"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""


def chec_anoBissexto(ano):
    caso1 = ano % 4
    caso2 = ano % 100
    caso3 = ano % 400
    
    if caso1 == 0 and caso2 != 0:
        print(f'O ano {ano} é bissexto')
    elif caso1 != 0 and caso3 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')



if __name__ == '__main__':
    while True:
        try:
            ano = int(input('Digite o ano a ser consultado: '))
            break
        except ValueError as error:
            print('Digite um ano valido')

    chec_anoBissexto(ano)