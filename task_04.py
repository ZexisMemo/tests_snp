def sort_list(list):
    if list != []:
        minelem = list[0]
        maxelem = list[0]
        for i in range(0, len(list)):
            if list[i] < minelem:
                minelem = list[i]
            elif list[i] > maxelem:
                maxelem = list[i]
        for i in range(0, len(list)):
            if list[i] == minelem:
                list[i] = maxelem
            elif list[i] == maxelem:
                list[i] = minelem
        list.append(minelem)
    print(list)


sort_list([])
sort_list([2, 4, 6, 8])
sort_list([1])
sort_list([1, 2, 1, 3])
