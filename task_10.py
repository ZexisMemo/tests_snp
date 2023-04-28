import re

def count_words(string):
    a = re.split("\W+", string)
    dictres = {}
    for i in range(0, len(a)):
        if dictres.get(a[i].lower(), False) == False:
            dictres.update({a[i].lower(): 1})
        else:
            dictres.update({a[i].lower(): dictres.get(a[i].lower()) + 1})
    print(dictres)



count_words("A man, a plan, a canal -- Panama")
count_words("Doo bee doo bee doo")
