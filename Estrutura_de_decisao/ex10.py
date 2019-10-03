# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


def verificaSaudacao(escolha):
    if escolha == 'M':
        print('Bom Dia!')

    if escolha == 'V':
        print('Boa Tarde!')

    if escolha == 'N':
        print('Boa Noite!')


if __name__ == '__main__':
    while True:
        periodo = input(
            f'Digite o periodo em que você estuda\n[ M ] Matutino\n[ V ] Vespertino\n[ N ] Noturno\nSua escolha: ')
        periodo = periodo[0].upper()
        periodos = ['M', 'V', 'N']
        if periodo in periodos:
            break
        else:
            print('Opção invalida')

    verificaSaudacao(periodo)
