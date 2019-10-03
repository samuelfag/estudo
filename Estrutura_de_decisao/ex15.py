'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
'''

lados = dict()


def checkTriangulo(lado_1, lado_2, lado_3):
    cond = ((lado_1 + lado_2) > lado_3)
    if cond != False:
        if lado_1 == lado_2 and lado_1 == lado_3:
            tipo = 'Equilátero'
        elif lado_1 != lado_2 and lado_1 == lado_3 or lado_1 == lado_2 and lado_1 != lado_3 or lado_1 != lado_2 and lado_2 == lado_3:
            tipo = 'Isósceles'
        else:
            tipo = 'Escaleno'
    else:
        tipo = 'não se pode ter um triangulo com essas medidas'
    print(tipo)


if __name__ == '__main__':

    for i in range(1, 4):
        lados[f'lado_{i}'] = float(
            input(f'Digite um valor para o {i}º lado: '))
    for k, v in lados.items():
        if k == 'lado_1':
            lado_1 = v
        elif k == 'lado_2':
            lado_2 = v
        elif k == 'lado_3':
            lado_3 = v

    checkTriangulo(lado_1, lado_2, lado_3)
