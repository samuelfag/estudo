"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    c) A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""


def check_status(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if 7 <= media < 10:
        print(f'Aluno Aprovado com a média {media:.2f}')
    elif media < 7:
        print(f'Aluno Reprovado com a média {media:.2f}')
    elif media == 10:
        print(f'Aluno Aprovado com Distinção com a média {media:.2f}')


if __name__ == '__main__':
    n1 = float(input('Digite o 1º numero: '))
    n2 = float(input('Digite o 2º numero: '))
    n3 = float(input('Digite o 3º numero: '))

    check_status(n1, n2, n3)
