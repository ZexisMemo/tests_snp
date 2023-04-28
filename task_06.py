class Error(Exception):
    pass

def rps_game_winner(list):
    try:
        if len(list) >= 3:
            raise Error("WrongNumberOfPlayersError")
        elif list[0][1] != 'P' and list[0][1] != 'R' and list[0][1] != 'S':
            raise Error("NoSuchStrategyError")
        elif list[1][1] != 'P' and list[1][1] != 'R' and list[1][1] != 'S':
            raise Error("NoSuchStrategyError")
    except Error as err:
        print(err.args[0])
        return
    a = ord(list[0][1]) - ord(list[1][1])
    if (a <= 0 or a == 3) and a != -3:
        r = True
    else:
        r = False
    if r:
        print(list[0][0], list[0][1])
    else:
        print(list[1][0], list[1][1])
    
        
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'A']])
rps_game_winner([['player1', 'P'], ['player2', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'P']])

rps_game_winner([['player1', 'S'], ['player2', 'P']])
rps_game_winner([['player1', 'R'], ['player2', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'R']])

rps_game_winner([['player1', 'R'], ['player2', 'P']])
        
