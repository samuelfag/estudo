#Faça um Programa que peça dois números e imprima a soma

def somaNumbers(num1, num2):
    print(f'A soma dos numeros é {int(num1) + int(num2)}')


if __name__ == '__main__':
    num1= input(f'Digite o primeiro numero da soma: ')
    num2= input(f'Digite o segundo numero da soma: ')
    somaNumbers(num1, num2)