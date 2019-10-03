#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


def verificaNum(numero):
    numero = numero

    if numero < 0:
        print(f'O {numero} é negativo')
    else:
        print(f'O {numero} é positivo')


if __name__ == '__main__':
    numero = float(input('Digite um numero: '))
    verificaNum(numero)