class MyError(Exception):
    pass

def rps_game_winner(list):
    try:
        if len(list) >= 3:
            raise MyError("WrongNumberOfPlayersError")
        elif list[0][1] != 'P' and list[0][1] != 'R' and list[0][1] != 'S':
            raise MyError("NoSuchStrategyError")
        elif list[1][1] != 'P' and list[1][1] != 'R' and list[1][1] != 'S':
            raise MyError("NoSuchStrategyError")
    except MyError as err:
        print(err.args[0])
    else:
        a = ord(list[0][1]) - ord(list[1][1])
        if (a <= 0 or a == 3) and a != -3:
            r = True
        else:
            r = False
        string = " "
        if r:
            string = list[0][0] + " " + list[0][1]
        else:
            string = list[1][0] + " " + list[1][1]
        return string
    return
