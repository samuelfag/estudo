# https://www.codewars.com/kata/exes-and-ohs/python
def xo(s):
    X, O = s.lower().count('x'), s.lower().count('o')
    if int(X) != int(O):
        return False
    else:
        return True


print(xo('zzoo'))
