import re

def count_words(string):
    a = re.split("\W+", string)
    dictres = {}
    for i in range(0, len(a)):
        if dictres.get(a[i].lower(), False) == False:
            dictres.update({a[i].lower(): 1})
        else:
            dictres.update({a[i].lower(): dictres.get(a[i].lower()) + 1})
    return dictres
