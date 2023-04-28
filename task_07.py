def combine_anagrams(words_array):
    anagr = []
    result = []
    while words_array != []:
        a = words_array[0]
        anagr.append(a)
        length = len(words_array)
        k = 0
        for i in range(1, length):
            if (sorted(a.lower()) == sorted(words_array[i - k].lower())):
                anagr.append(words_array[i - k])
                words_array.pop(i - k)
                k = k + 1
        words_array.pop(0)
        result.append(anagr)
        anagr = []
    print(result)


combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"])

combine_anagrams(["Cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"])
                
            
