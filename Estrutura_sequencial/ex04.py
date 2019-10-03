#Faça um Programa que peça as 4 notas bimestrais e mostre a média

def mediaNotas(*args):
    soma = 0
    qtd_notas = len(args[0])
    for i in args[0]:
        soma += int(i)
    print(f'A media de notas do aluno é = {int(soma) / int(qtd_notas)}')


if __name__ == '__main__':
    notas = []
    for i in range(1,5):
        nota = input(f'Digite a {i}º nota do aluno: ')
        notas.append(nota)
    mediaNotas(notas)