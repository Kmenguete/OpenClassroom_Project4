
DEFAULT_ROUNDS_NUMBER = 4


def create_list_dict(players_list):
    new_players_dict = {}
    for player in players_list:
        new_players_dict[player.player_id] = player.total_score
    return new_players_dict


class Tournament:
    def __init__(self, name, place, date, description, number_of_rounds=DEFAULT_ROUNDS_NUMBER, rounds=None,
                 players=None, players_dict=None):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.rounds = rounds
        self.players = players
        self.players_dict = players_dict
        self.description = description

    def __len__(self):
        return len(self.players)

    def __getitem__(self, players, i):
        return self.players[i]

    def check_if_match_already_happened(self, player_a, player_b):
        already_happened = False
        for tour in self.rounds:
            for match in tour.matches:
                if (match.player_a == player_a and match.player_b == player_b) or (match.player_a == player_b and
                                                                                   match.player_b == player_a):
                    already_happened = True
        return already_happened

    def get_next_available_player(self, player_a, next_player_index, non_available_players):
        if self.check_if_match_already_happened(player_a, self.players[next_player_index]):
            self.get_next_available_player(player_a, next_player_index + 1, non_available_players)
            return self.players[next_player_index + 1]
        else:
            return self.players[next_player_index]

    def seek_player_and_update_score(self, player, new_score):
        if player.player_id in self.players_dict:
            self.players_dict[player.player_id] += new_score
        else:
            self.players_dict[player.player_id] = player.total_score + new_score
        return self.players_dict

    def display_players(self):
        print("******************** list of players with length: {} *******************".format(len(self.players_dict)))
        for player in self.players_dict.items():
            print(player)
