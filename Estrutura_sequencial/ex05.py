#Faça um Programa que converta metros para centímetros.

def getMetros(medida):
    metros = float(medida) * 100
    print(f'{medida} em metros é igual a {metros:.2f} centimetros')
    

if __name__ == '__main__':
    medida = input('Digite a medida em metros para ser convertida: ')
    getMetros(medida)