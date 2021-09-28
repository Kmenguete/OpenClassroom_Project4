from tinydb import TinyDB


class Match:
    def __init__(self, round_number, match_number, player_a, player_b, score_player_a, score_player_b):
        self.round_number = round_number
        self.match_number = match_number
        self.player_a = player_a
        self.score_player_a = score_player_a
        self.player_b = player_b
        self.score_player_b = score_player_b

    def __str__(self):
        return self.round_number + " " + self.match_number + " " + self.player_a + " " + self.score_player_a + " " + \
               self.player_b + " " + self.score_player_b


if __name__ == '__main__':
    round_number = input("enter the round number: ")
    match_number = input("enter the match number: ")
    player_a = input("enter the firstname and surname of player a: ")
    score_player_a = input("enter the score of player a: ")
    player_b = input("enter the firstname and surname of player b: ")
    score_player_b = input("enter the score of player b: ")
    match = Match(round_number, match_number, player_a, player_b, score_player_a, score_player_b)
    print("Here is the result of the match: " + str(match))
    match_database = TinyDB('Match.json')
    match_database.insert({'round_number': round_number})
    match_database.insert({'match_number': match_number})
    match_database.insert({'player_a': player_a})
    match_database.insert({'score_of_player_a': score_player_a})
    match_database.insert({'player_b': player_b})
    match_database.insert({'score_of_player_b': score_player_b})
