'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% 
para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% 
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    ex:
    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00  
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
'''

def holerite(*kargs):
    valor_hora = kargs[0][0]
    qtd_horas = kargs[0][1]
    salario = (valor_hora * qtd_horas)

    if salario <= 900:
        ir = 0
    elif 900 < salario <= 1500:
        ir = 5
    elif 1500 < salario <= 2500:
        ir = 10
    elif salario > 2500:
        ir = 20

    inss = ((salario / 100) * 10)
    valor_ir = ((salario / 100) * ir)
    fgts = ((salario / 100) * 11)
    total_desconto = (inss + valor_ir)
    salario_liquido = (salario - total_desconto)

    print(f'Salário Bruto: ({int(valor_hora)} * {int(qtd_horas)})       : R$ {salario:.2f}')
    print(f'(-) IR ({ir}%)                    : R$ {valor_ir:.2f}')
    print(f'(-) INSS ( 10%)                : R$ {inss:.2f}')
    print(f'FGTS (11%)                     : R$ {fgts:.2f}')
    print(f'Total de descontos             : R$ {total_desconto:.2f}')
    print(f'Salário Liquido                : R$ {salario_liquido:.2f}')



if __name__ == '__main__':
    kargs = []
    valor_hora = float(input('Digite o valor da hora trabalhadas: '))
    qtd_horas = int(input('Digite a quantidades de horas trabalhadas: '))
    kargs.append(valor_hora)
    kargs.append(qtd_horas)
    holerite(kargs)
