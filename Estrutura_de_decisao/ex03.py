#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido


def getSexo(sexo):
    sexo = sexo
    if sexo == 'M':
        print('Sexo MASCULINO')
    elif sexo == 'F':
        print('Sexo FEMININO')
    else:
        print('Sexo INVALIDO')


if __name__ == '__main__':
    sexo = input('Digite desejado: ')
    sexo = sexo[0].upper()
    getSexo(sexo)