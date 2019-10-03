#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

def getNumber(number):
    print(f'O número informado foi {number}')

if __name__ == '__main__':
    number = input('Digite um numero: ')
    getNumber(number)
