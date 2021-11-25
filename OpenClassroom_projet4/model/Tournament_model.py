import uuid

DEFAULT_ROUNDS_NUMBER = 4


def create_list_dict(players_list):
    new_players_dict = {}
    for player in players_list:
        new_players_dict[player.player_id] = player.total_score
    return new_players_dict


class Tournament:
    def __init__(self, name, place, date, description, number_of_rounds=DEFAULT_ROUNDS_NUMBER, tournament_id=None,
                 rounds=None, players=None, players_dict=None):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.tournament_id = self.get_tournament_id(tournament_id)
        self.rounds = rounds
        self.players = players
        self.players_dict = players_dict
        self.description = description

    @staticmethod
    def get_tournament_id(tournament_id):
        if tournament_id is None:
            tournament_id = str(uuid.uuid4())
        return tournament_id

    def __str__(self):
        return "name: " + self.name + ", " + "place: " + self.place + ", " + "description: " + self.description + ", " \
               + " number_of_rounds: " + str(self.number_of_rounds) + ", " + "tournament_id: " + self.tournament_id + \
               " rounds: " + str(self.rounds) + " " + str(self.date)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.players)

    def __getitem__(self, players, i):
        return self.players[i]
