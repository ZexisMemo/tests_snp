def coincidence(list=[], range=range(0,1)):
    i = 0
    arr = []
    while i < len(list):
        if type(list[i]) == int or type(list[i]) == float:
            if list[i] >= min(range) and list[i] <= max(range):
                arr.append(list[i])
        i = i + 1
    print(arr)

coincidence([1, 2.5, 3, 4, 12, "adad"], range(0,10))
coincidence([1, 2, 3, 4, 5])
coincidence(range(3, 6))

coincidence([1, 2, 3, 4, 5], range(3, 6))
coincidence()
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))
