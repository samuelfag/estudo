#Faça um Programa que leia três números e mostre-os em ordem decrescente.

def inverteSequencia(*numeros):
    numeros = numeros[0]
    original = numeros
    numeros.sort(reverse=True)  
    print(f'Sequencia que foi digitada: {original}')
    print(f'Sequencia em ordem decrescente: {numeros}')
    


if __name__ == '__main__':
    numeros = []
    for i in range(1,4):
        numero = float(input(f'Digite um numero: '))
        numeros.append(numero)

    inverteSequencia(numeros)
