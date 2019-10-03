#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


def calcCircleArea(raio):
    pi = 3.14
    raio = int(raio)
    area = (pi * (raio * raio))
    print(f'Com o raio informado {raio} a area do circulo é de {area} centimetros')


if __name__ == '__main__':
    raio = input(f'Digite o raio para calculo da área do circulo: ')
    calcCircleArea(raio)
