#Faça um Programa que leia três números e mostre o maior deles.

def maiorNum(*numeros):
    numeros = numeros[0]
    maior = 0
    for i in numeros:
        if i > maior:
            maior = i
    
    print(f'O maior numero é {maior}')


if __name__ == '__main__':
    numeros = []
    for i in range(1,4):
        numero = float(input(f'Digite o {i}º numero: '))
        numeros.append(numero)

    maiorNum(numeros)