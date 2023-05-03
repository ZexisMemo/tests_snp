def max_odd(array):
    maxoddelem = -1
    for i in range(0,len(array)):
        if type(array[i]) == int or type(array[i]) == float:
            if array[i]%2 != 0 and array[i] > maxoddelem:
                maxoddelem = int(array[i])
    if maxoddelem == -1:
        return None
    return maxoddelem
