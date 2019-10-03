'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

def calcConceito(*notas):
    notas = (notas[0])
    soma = 0
    for i in notas:
        soma += float(i)
    
    media = (soma / len(notas))
    
    if 9 <= float(media) <= 10:
        conceito = 'A'
        status = 'APROVADO'

    elif 7.5 <= float(media) < 9 :
        conceito = 'B'
        status = 'APROVADO'
        
    elif 6 <= float(media) < 7.5 :
        conceito = 'C'
        status = 'APROVADO'

    elif 4 <= float(media) < 6 :
        conceito = 'D'
        status = 'REPROVADO'

    elif 0 <= float(media) < 4 :
        conceito = 'E'
        status = 'REPROVADO'
    
    print(f'Conceito: {conceito} com o status {status}')


if __name__ == '__main__':
    notas = []
    for i in range(1,3):
        nota = float(input(f'Digite a {i}º nota: '))
        notas.append(nota)
    calcConceito(notas)
