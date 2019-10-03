"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1 - O produto do dobro do primeiro com metade do segundo .
2 - A soma do triplo do primeiro com o terceiro.
3 - O terceiro elevado ao cubo.
"""

def getNumbers(*args):
    num1 = int(args[0][0])
    num2 = int(args[0][1])
    num3 = float(args[0][2])
    conta1 = ((num1 * 2) + int((num2 / 2)))
    conta2 = ((num1 * 3) + num3)
    conta3 = (num3 * num3 * num3)
    print(f'{conta1}\n{conta2}\n{conta3:.2f}')


if __name__ == '__main__':
    numeros = []
    for i in range(1,4):
        numero = input(f'Digite o {i}º numero: ')
        numeros.append(numero)
    getNumbers(numeros)
