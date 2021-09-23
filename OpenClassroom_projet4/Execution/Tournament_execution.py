
class Tournament:
    def __init__(self, name_of_tournament, place_of_tournament, date_of_tournament, duration_of_tournament,
                 number_of_round, number_of_match, description_of_tournament):
        self.name_of_tournament = name_of_tournament
        self.place_of_tournament = place_of_tournament
        self.date_of_tournament = date_of_tournament
        self.duration_of_tournament = duration_of_tournament
        self.number_of_round = number_of_round
        self.number_of_match = number_of_match
        self.description_of_tournament = description_of_tournament

    def __str__(self):
        return self.name_of_tournament + " " + self.place_of_tournament + " " + self.date_of_tournament + " " + \
               self.duration_of_tournament + " " + self.number_of_round + " " + self.number_of_match + " " + \
               self.description_of_tournament


if __name__ == '__main__':
    name_of_tournament = input("enter the name of tournament: ")
    place_of_tournament = input("enter the place of tournament: ")
    date_of_tournament = input("enter the date of tournament: ")
    duration_of_tournament = input("enter the duration of tournament: ")
    number_of_round = input("enter the number of round: ")
    number_of_match = input("enter the number of match: ")
    description_of_tournament = input("enter a description for this tournament: ")
    tournament = Tournament(name_of_tournament, place_of_tournament, date_of_tournament, duration_of_tournament,
                            number_of_round, number_of_match, description_of_tournament)
    print("You have successfully created the following tournament: " + str(tournament))
