

class Round:
    def __init__(self, name_of_tournament, round_number, match_list):
        self.name_of_tournament = name_of_tournament
        self.round_number = round_number
        self.match_list = match_list

    def __str__(self):
        return '{}, {}, {}'.format(self.name_of_tournament, self.round_number, self.match_list)


if __name__ == '__main__':
    name_of_tournament = input("enter the name of the tournament: ")
    round_number = input("enter the round number: ")
    match_list = input("enter the randomly generated matches: ")
    round = Round(name_of_tournament, round_number, match_list)
    print("Here are the matches for the current round: " + str(round))
