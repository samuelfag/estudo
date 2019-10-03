#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.  C = (5 * (F-32) / 9).


def convert_temp(farenheit):
    farenheit = float(farenheit)
    celsius = (5 * (farenheit - 32) / 9)
    print(f'{farenheit}º em celsius é: {celsius:.2f}º')


if __name__ == '__main__':
    farenheit = input('Digite a temperatura em farenheit: ')
    convert_temp(farenheit)