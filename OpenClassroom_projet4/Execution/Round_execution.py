from tinydb import TinyDB


class Round:
    def __init__(self, name_of_tournament, round_number, match_number, player_a, player_b, score_player_a, score_player_b):
        self.name_of_tournament = name_of_tournament
        self.round_number = round_number
        self.match_number = match_number
        self.player_a = player_a
        self.player_b = player_b
        self.score_player_a = score_player_a
        self.score_player_b = score_player_b

    def __str__(self):
        return self.name_of_tournament + " " + self.round_number + " " + self.match_number + " " + self.player_a + " " \
               + self.player_b + " " + self.score_player_a + " " + self.score_player_b


if __name__ == '__main__':
    name_of_tournament = input("enter the name of the tournament: ")
    round_number = input("enter the round number: ")
    match_number = input("enter the match number: ")
    player_a = input("enter the firstname and surname of player a: ")
    player_b = input("enter the firstname and surname of player b: ")
    score_player_a = input("enter the score of player a: ")
    score_player_b = input("enter the score of player b: ")
    round = Round(name_of_tournament, round_number, match_number, player_a, player_b, score_player_a,
                  score_player_b)
    print("Here is the last information about the selected match: " + str(round))
    round_database = TinyDB('Round.json')
    round_database.insert({'name_of_tournament': name_of_tournament})
    round_database.insert({'round_number': round_number})
    round_database.insert({'match_number': match_number})
    round_database.insert({'player_a': player_a})
    round_database.insert({'player_b': player_b})
    round_database.insert({'score_player_a': score_player_a})
    round_database.insert({'score_player_b': score_player_b})
