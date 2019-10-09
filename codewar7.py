# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python


def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        string = '#' * (len(cc)-4)
        return f'{string}{cc[-4:]}'


print(maskify('4556364607935616'))
