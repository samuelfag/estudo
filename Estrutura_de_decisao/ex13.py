#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido


def getDia_semana(dia):
    dias_semana = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado']
    print(dias_semana[int(dia) - 1])


if __name__ == '__main__':
    dias = ['1', '2', '3', '4', '5', '6', '7']
    while True:
        dia = input('Digite um numero entre 1 e 7: ')
        if dia in dias:
            break
        else:
            print('Valor invalido') 
    getDia_semana(dia)