"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do 
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

def calcMulta(peso):
    peso = peso

    if peso >= 50:
        multa = ((peso - 50) * 4)
        print(f'Existe um excedente de {peso - 50} kilos e você deve pagar uma multa de R$ {multa:.2f} reais')

    else:
        print(f'O peso dos peixes não passam do limete de 50 kilos')


if __name__ == '__main__':
    peso = int(input('Digite o peso total dos peixes: '))

    calcMulta(peso)
