"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
1 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
2 - A mensagem "Reprovado", se a média for menor do que sete;
3 - A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

def calcMedia(*notas):
    notas = notas[0]
    soma = 0
    for i in notas:
        soma += i
    media = (soma / len(notas))
    if media >= 7:
        print(f'A média é: {media:.2f} e o status é APROVADO')
    elif media < 7:
        print(f'A média é: {media:.2f} e o status é REPROVADO')
    elif media == 10:
        print(f'A média é: {media:.2f} e o status é APROVADO COM DISTINÇÃO')

if __name__ == '__main__':
    notas = []
    for i in range(1,3):
        nota = float(input(f'Digite a {i}º nota: '))
        notas.append(nota)

    calcMedia(notas)