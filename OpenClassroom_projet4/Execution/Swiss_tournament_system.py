
def sort_player_by_rank(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
    # The goal of this function is to sort players by rank.
    # My Player class instances will be store in variables player_1, player_2, player_3...etc.
    # The rank of my players are the key of my dictionary. my dictionary will be sorted by key.
    player_list = {'2nd': player_1, '8th': player_2, '1st': player_3, '5th': player_4, '4th': player_5,
                   '3rd': player_6, '6th': player_7, '7th': player_8}
    sorted_player_list = sorted(player_list)
    return sorted_player_list


class SwissTournamentSystem:

    def split_total_number_of_players(self, player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                      player_8):
        pass

    def pairs_of_players(self, player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
        pass

    def sort_players_by_score_round(self, player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                    player_8):
        pass

    def generate_new_pairs_of_players(self, player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                      player_8):
        pass

# I repeat the two last functions until the end of tournament.
