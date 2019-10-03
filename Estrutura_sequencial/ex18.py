"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

def calcTaxa(tamanho, velocidade):
    tamanho = tamanho
    velocidade = (velocidade / 8)
    tempo = ((tamanho / velocidade) / 60)
    print(f'O arquivo tem {tamanho:.2f} MBs\nA sua velocidade de internet é de: {velocidade * 8} Mbps e tem uma taxa de download de {velocidade:.2f} Mbps')
    print(f'O tempo total de download é de: {tempo:.2f}')



if __name__ == '__main__':
    tamanho = float(input('Digite o tamanho do arquivo em MB: '))
    velocidade = int(input('Digite a velocidade do link em Mbps: '))
    calcTaxa(tamanho, velocidade)