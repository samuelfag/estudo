#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


def verificaPreco(*valores):
    menor = sorted(valores[0])[0]
    print(f'O produto de menor valor é o {menor[1]}º, e ele tem o valor de {menor[0]} reais')


if __name__ == '__main__':
    valores = []
    for i in range(1,4):
        valor = float(input(f'Digite o valor do {i}º produto: '))
        string = (valor, i)
        valores.append(string)

    verificaPreco(valores)





