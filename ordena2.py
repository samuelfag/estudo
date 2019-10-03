lista = []
tamanho = int(input('Digite a quantidade de elementos da lista: '))

for i in range(0, tamanho):
    num = int(input(f'Digite o {i+1}º numero: '))
    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)

    else:
        index = 0
        while index < len(lista):
            if num in lista:
                break
            elif num <= lista[index]:
                lista.insert(index, num)
                break
            index += 1

for i in lista:
    print(f'{i}, ', end='')
