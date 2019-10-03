#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit


def convert_temp(celsius):
    celsius = float(celsius)
    farenheit = ((celsius * 9/5) + 32)
    print(f'{celsius}º em farenheit é {farenheit}º')


if __name__ == '__main__':
    celsius = input('Digite a temperatura em graus celsius: ')
    convert_temp(celsius)