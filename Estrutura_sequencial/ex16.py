"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

def calcQtdTinta(tamanho):
    tamanho = tamanho
    cobertura = (tamanho / 3)
    qtd_latas = (cobertura / 18)
    if qtd_latas >= 1:
        valor_gasto = (qtd_latas * 80)
    else:
        valor_gasto = 80
    print(f'A quantidade de latas para pintar a área {tamanho} é de: {qtd_latas:.2f}\nO valor para pintar a área {tamanho} é de: {valor_gasto:.2f}')


if __name__ == '__main__':
    tamanho = float(input('Digite o tamanho da área em metros quadrados: '))
    calcQtdTinta(tamanho)
