from random import randint

def Ordena(lista):
    lista2 = []
    
    for i in lista:
        index = 0
        while True:
            if i in lista2:
                break
            elif i <= lista[index]:
                lista2.insert(index, i)
                break
            index += 1

    print(lista)
    print(lista2)


if __name__ == '__main__':
    tamanho = int(input('Digite o tamanho da lista: '))
    n = 0
    lista = []
    while True:
        if n < tamanho:
            num = randint(0,100)
            lista.append(num)
            n += 1
        else:
            break
        
    Ordena(lista)
