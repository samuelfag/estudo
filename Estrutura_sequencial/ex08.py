#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


def calcSalario(valor, qtd_horas):
    valor = int(valor)
    qtd_horas = int(qtd_horas)

    salario = (valor * qtd_horas)

    print(f'O salário é {salario} com um total de {qtd_horas} trabalhadas com o valor de {valor}')


if __name__ == '__main__':
    valor = input('Digite o valor da hora trabalhada: ')
    qtd_horas = input('Digite a quantidade de horas trabalhadas no mês: ')
    calcSalario(valor, qtd_horas)
