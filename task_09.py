def connect_dicts(dict1, dict2):
    if sum(dict1.values()) > sum(dict2.values()):
        dict2.update(dict1)
        bigdict = dict2
    else:
        dict1.update(dict2)
        bigdict = dict1
    values = sorted(bigdict.items(), key = lambda item: item[1])
    resdict = {k: v for k, v in values if v >= 10}
    return resdict
        
