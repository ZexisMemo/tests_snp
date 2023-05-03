def coincidence(list=[], range=range(0,1)):
    i = 0
    arr = []
    while i < len(list):
        if type(list[i]) == int or type(list[i]) == float:
            if list[i] >= min(range) and list[i] <= max(range):
                arr.append(list[i])
        i = i + 1
    return arr

