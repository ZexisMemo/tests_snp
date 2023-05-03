import time
def date_in_future(integer):
    if type(integer) != int:
        return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
    else:
        return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time() + 24*3600*integer))


