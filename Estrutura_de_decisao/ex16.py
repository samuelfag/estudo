"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:

    a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""


def calcEquacao(a, b, c):
    delta = ((b * b) -4 * a * c) ** 0.5
    if delta < 0:
        print('Delta menor que ZERO não possui raizes reais')
    elif delta == 0:
        x1 = ((b * -1 + delta) / (2 * a))
        print(f'A equação possui somente uma raiz real, o valor da raiz é {x1}')
    else:
        x1 = ((b * -1 + delta) / (2 * a))
        x2 = ((b * -1 - delta) / (2 * a))
        print(f'A equação possui duas raizes:\nX1 = {x1}\nX2 = {x2}')


if __name__ == '__main__':
    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    
    if a == 0:
        print('A equação não é do segundo grau')
    else:
        calcEquacao(a, b, c)
