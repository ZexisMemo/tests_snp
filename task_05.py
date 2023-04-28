import time
def date_in_future(integer):
    if type(integer) != int:
        print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
    else:
        print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time() + 24*3600*integer)))


date_in_future([])
date_in_future(2)
date_in_future(60)
