def high_and_low(numbers):
    numbers = numbers.split(' ')
    high, low = numbers[0], numbers[0]

    for i in numbers:
        if int(i) >= int(high):
            high = i
        elif int(i) <= int(low):
            low = i
    numbers = f'{str(high)} {str(low)}'
    return numbers


lista = '4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'
print(high_and_low(lista))
