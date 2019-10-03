#Faça um Programa que leia três números e mostre o maior e o menor deles.

def maior(*numeros):
    maior = numeros[0][0]
    for i in numeros[0]:
        if i > maior:
            maior = i
    return maior

def menor(*numeros):
    menor = numeros[0][0]
    for i in numeros[0]:
        if i < menor:
            menor = i
    return menor
   

if __name__ == '__main__':
    numeros = []
    for i in range(1,4):
        numero = float(input(f'Digite o {i}º numero: '))
        numeros.append(numero)

    maior = maior(numeros)
    menor = menor(numeros)
    print(f'A sequencia de numeros: {numeros}')
    print(f'O maior numero é: {maior}')
    print(f'O menor numero é: {menor}')

