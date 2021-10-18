DEFAULT_ROUNDS_NUMBER = 4


class Tournament:
    def __init__(self, name, place, date, description, number_of_rounds=DEFAULT_ROUNDS_NUMBER, rounds=None,
                 players=None):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.rounds = rounds
        self.players = players
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
        if self.check_if_match_already_happened(player_a, self.players[next_player_index]) or \
                self.players[next_player_index] in non_available_players:
            self.get_next_available_player(player_a, next_player_index + 1, non_available_players)
        else:
            return self.players[next_player_index]
