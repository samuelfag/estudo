#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def consultaLetra(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    letra = letra[0].lower()
    if (letra.isnumeric()) == True:
        print(f'Você não digitou um letra do alfabeto, você digitou o numero: {letra}')
    else:
        if letra in vogais:
            print(f'A letra {letra} é uma vogal')
        else:
            print(f'A letra {letra} é uma consoante')


if __name__ == '__main__':
    letra = input('Digite uma letra: ')
    consultaLetra(letra)