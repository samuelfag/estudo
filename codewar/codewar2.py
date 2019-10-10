def accum(s):
    i = 0
    while i <= len(s):
        if i < len(s):
            c = s[i]
            if i < len(s)-1:
                print((c * (i + 1)).capitalize(), end='-')
            else:
                print((c * (i + 1)).capitalize())
        i += 1


accum('ZpglnRxqenU')
