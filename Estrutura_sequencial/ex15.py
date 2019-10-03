'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
1 - Salário bruto.
2 - Quanto pagou ao INSS.
3 - Quanto pagou ao sindicato.
4 - O salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

def calcSalario(qtd_horas, valor_horas):
    qtd_horas = qtd_horas
    valor_horas = valor_horas
    salario_bruto = (qtd_horas * valor_horas)
    imposto_renda = ((salario_bruto / 100) * 11)
    inss = ((salario_bruto / 100) * 8)
    sindicato = ((salario_bruto / 100) * 5)
    salario_liquido = (salario_bruto - (imposto_renda + inss + sindicato))
    print(salario_liquido)
    print(salario_bruto)


if __name__ == '__main__':
    qtd_horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))
    valor_horas = float(input('Digite o valor da hora trabalhada: '))
    calcSalario(qtd_horas, valor_horas)


