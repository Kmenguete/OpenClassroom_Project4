

class Round:
    def __init__(self, name_of_tournament, round_number, match_1, match_2, match_3, match_4):
        self.name_of_tournament = name_of_tournament
        self.round_number = round_number
        self.match_1 = match_1
        self.match_2 = match_2
        self.match_3 = match_3
        self.match_4 = match_4

    def __str__(self):
        return self.name_of_tournament + " " + self.round_number + " " + self.match_1 + " " + self.match_2 + " " \
               + self.match_3 + " " + self.match_4


if __name__ == '__main__':
    name_of_tournament = input("enter the name of the tournament: ")
    round_number = input("enter the round number: ")
    match_1 = input("enter the pair of players for the match 1: ")
    match_2 = input("enter the pair of players for the match 2: ")
    match_3 = input("enter the pair of players for the match 3: ")
    match_4 = input("enter the pair of players for the match 4: ")
    round = Round(name_of_tournament, round_number, match_1, match_2, match_3, match_4)
    print("Here is the 4 pairs of match for the current round: " + str(round))

