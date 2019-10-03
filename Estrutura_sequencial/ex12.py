#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def calcIMC(altura):
    altura = float(altura)

    imc = ((72.7 * altura) - 58)
    print(f'O seu peso ideal é: {imc:.2f}')


if __name__ == '__main__':
    altura = input('Digite a altura em metros: ')
    calcIMC(altura)