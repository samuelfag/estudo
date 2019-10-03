#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário


def calcSquareArea(unidade_medida, lado):
    lado = int(lado)
    area = (lado * lado)
    dobro = area * 2
    if unidade_medida == 1:
        print(f'O lado do quadrado é: {lado} metros\nA área do quadrado é {area} metros\nO dobro da área é: {dobro} metros')
    else:
        print(f'O lado do quadrado é: {lado} centimetros\nA área do quadrado é {area} centimetros\nO dobro da área é: {dobro} centimetros')


if __name__ == '__main__':
    lado = input(f'Digite o tamanho do lado do quadrado: ')
    unidade_medida = input(f'Selecione unidade de medida que deseja utilizar\n[ 1 ] Metros\n[ 2 ] Centimetros\nOpção escolhida: ')
    calcSquareArea(unidade_medida, lado)
    