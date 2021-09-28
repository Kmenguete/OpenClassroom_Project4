from tinydb import TinyDB


class Match:
    def __init__(self, player_1, player_2, score_player_1, score_player_2):
        self.player_1 = player_1
        self.score_player_1 = score_player_1
        self.player_2 = player_2
        self.score_player_2 = score_player_2

    def __str__(self):
        return self.player_1 + " " + self.score_player_1 + " " + self.player_2 + " " + self.score_player_2


if __name__ == '__main__':
    player_1 = input("enter the firstname and surname of player 1: ")
    score_player_1 = input("enter the score of player 1: ")
    player_2 = input("enter the firstname and surname of player 2: ")
    score_player_2 = input("enter the score of player 2: ")
    match = Match(player_1, player_2, score_player_1, score_player_2)
    print("Here is the result of the match: " + str(match))
    match_database = TinyDB('Match.json')
    match_database.insert({'player_1': player_1})
    match_database.insert({'score_of_player_1': score_player_1})
    match_database.insert({'player_2': player_2})
    match_database.insert({'score_of_player_2': score_player_2})
