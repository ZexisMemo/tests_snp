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
    return list
