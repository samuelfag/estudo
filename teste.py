dict_transacao = dict()


def emprestimo(nome1, nome2, valor):
    dict_transacao[nome1] = dict_transacao.get(nome1, 0) - valor
    dict_transacao[nome2] = dict_transacao.get(nome2, 0) + valor

    return dict_transacao


def consulta(nome):
    for k, v in dict_transacao.items():
        if k == nome:
            print(k, v)


if __name__ == '__main__':
    emprestimo('samuel', 'teste', 50)
    emprestimo('teste', 'samuel', 150)
    emprestimo('samuel', 'teste', 100)
    consulta('teste')
    consulta('samuel')
