def median(lst):
    i = 0
    for x in lst:
        i += x
    return i / len(lst)


median([x for x in range(1, 10)])
