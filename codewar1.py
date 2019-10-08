def duplicate_count(text):
    counter = dict()
    dict_repeats = dict()
    for i in text.upper():
        counter[i] = counter.get(i, 0) + 1

    for k, v in counter.items():
        if v > 1:
            dict_repeats[k] = v

    if len(dict_repeats) == 0:
        return 0

    else:
        return len(dict_repeats)


if __name__ == '__main__':
    counter = duplicate_count('abindivisibilitycde')
