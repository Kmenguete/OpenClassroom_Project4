from tinydb import TinyDB


class Round:
    def __init__(self, name_of_tournament, round_number, match_number, score_player_1, score_player_2):
        self.name_of_tournament = name_of_tournament
        self.round_number = round_number
        self.match_number = match_number
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        return self.name_of_tournament + " " + self.round_number + " " + self.match_number + " " + self.score_player_1 +\
               " " + self.score_player_2


if __name__ == '__main__':
    name_of_tournament = input("enter the name of the tournament: ")
    round_number = input("enter the round number: ")
    match_number = input("enter the match number: ")
    score_player_1 = input("enter the score of player 1: ")
    score_player_2 = input("enter the score of player 2: ")
    round = Round(name_of_tournament, round_number, match_number, score_player_1, score_player_2)
    print("Here is the last information about the selected match: " + str(round))
    round_database = TinyDB('Round.json')
    round_database.insert({'name of tournament': name_of_tournament})
    round_database.insert({'round number': round_number})
    round_database.insert({'match number': match_number})
    round_database.insert({'score player 1': score_player_1})
    round_database.insert({'score player 2': score_player_2})
