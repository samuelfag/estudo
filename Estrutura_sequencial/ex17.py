"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
1 - Comprar apenas latas de 18 litros;
2 - Comprar apenas galões de 3,6 litros;
3 - Misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

from math import ceil

def calTinta(tamanho):
    tamanho = tamanho
    qtd_tinta = (tamanho / 6)
    lata_18 = (qtd_tinta / 18)
    lata_36 = (qtd_tinta / 3.6)
    lata_18 = ceil(lata_18)
    lata_36 = ceil(lata_36)
    total_18 = (lata_18 * 80)
    total_36 = (lata_36 * 25)

    if (qtd_tinta % 18) == 0:
        qtd_lata18 = (qtd_tinta / 18)
    else:
        resto = (qtd_tinta % 18)
        qtd_lata18 = (qtd_tinta / 18)
        resto = (float(resto) / 3.6)
        
    print(f'É preciso comprar {lata_18} de latas de 18 litros com um valor total de {total_18:.2f}')
    print(f'É preciso comprar {lata_36} de latas de 3,6 litros com um valor total de {total_36:.2f}')


if __name__ == '__main__':
    tamanho = float(input('Digite o tamanho da área a ser pintada em metros quadrados: '))
    calTinta(tamanho)