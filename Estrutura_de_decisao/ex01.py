#Faça um Programa que peça dois números e imprima o maior deles.


def comparaNum(*args):
    numeros = args[0]
    menor = 999999999999999
    maior = 0

    for i in numeros:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    print(f'O maior numero é: {maior} e o menor é: {menor}')
    

if __name__ == '__main__':
    numeros = []
    for i in range(1,3):
        numero = int(input(f'Digite o {i}º numero: '))
        numeros.append(numero)
    comparaNum(numeros)