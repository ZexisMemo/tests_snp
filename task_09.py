def connect_dicts(dict1, dict2):
    if sum(dict1.values()) > sum(dict2.values()):
        dict2.update(dict1)
        bigdict = dict2
    else:
        dict1.update(dict2)
        bigdict = dict1
    values = sorted(bigdict.items(), key = lambda item: item[1])
    resdict = {k: v for k, v in values if v >= 10}
    print(resdict)
        


connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })
