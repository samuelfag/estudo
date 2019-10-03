"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

def calcIMC(altura, sexo):
    altura = float(altura)
    sexo = sexo.upper()

    if sexo == 'M':
        imc = ((72.7 * altura) - 58)
    if sexo == 'F':
        imc = ((62.1 * altura) -44.7)
    
    print(f'O peso ideal é de: {imc:.2f}')


if __name__ == '__main__':
    altura = input('Digite a sua altura em metros: ')
    while True:
        sexo = input('Digite [ M ] para Masculino e [ F ] para feminino: ')
        if sexo in 'MmFf':
            break
    calcIMC(altura, sexo)