def max_odd(array):
    maxoddelem = -1
    for i in range(0,len(array)):
        if type(array[i]) == int or type(array[i]) == float:
            if array[i]%2 != 0 and array[i] > maxoddelem:
                maxoddelem = int(array[i])
    if maxoddelem == -1:
        print(None)
    else:
        print(maxoddelem)
    return maxoddelem


max_odd([1, 2, 3, 4, 4])
max_odd([21.0, 2, 3, 4, 4])
max_odd(['ololo', 2, 3, 4, [1, 2], None])
max_odd(['ololo', 'fufufu'])
max_odd([2, 2, 4])

                
