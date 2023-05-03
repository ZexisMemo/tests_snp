def is_palindrome(string):
    string = str(string)
    flag = True
    i = 0
    j = len(string) - 1
    while i < j:
        while not string[i].isalpha() and i < len(string) - 1:
            i = i + 1
        while not string[j].isalpha() and j > 0:
            j = j - 1
        if string[i].lower() != string[j].lower():
            flag = False
            break
        i = i + 1
        j = j - 1
    return flag
