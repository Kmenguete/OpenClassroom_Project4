
def sort_player_by_rank(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
    # The goal of this function is to sort players by rank.
    # My Player class instances will be store in variables player_1, player_2, player_3...etc.
    # The rank of my players are the key of my dictionary. my dictionary will be sorted by key.
    player_list = {'2nd': player_1, '8th': player_2, '1st': player_3, '5th': player_4, '4th': player_5,
                   '3rd': player_6, '6th': player_7, '7th': player_8}
    sorted_player_list = sorted(player_list)
    print(sorted_player_list)


def split_total_number_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                  player_8):
    # We want to split players in two group. The first half return the first half of the group. The second half return
    # the second half of the group.
    player_list = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
    first_half = player_list[:3]
    second_half = player_list[3:]
    print(first_half, second_half)


def pairs_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
    # Pairs of players are generated according the rank of each group of players. The best player of the first group
    # will play with the best player of the 2nd group. The 2nd best player of the first group will play with the 2nd
    # best player of the 2nd group and so on.
    pair_of_player_a = {'1st': player_3, '3rd': player_6}
    pair_of_player_b = {'2nd': player_1, '4th': player_5}
    pair_of_player_c = {'5th': player_4, '6th': player_7}
    pair_of_player_d = {'8th': player_2, '7th': player_8}
    print(pair_of_player_a, pair_of_player_b, pair_of_player_c, pair_of_player_d)


def sort_players_by_score_round(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                player_8):
    # When a round is finished, players should be sorted according their total number of points for the round.
    # This new sorted list will be the new rank for the next round. If two players has the same number of points,
    # they are sorted by rank.
    player_list = [{player_1: "Kevin", "score of round": 5.5}, {player_2: "Sarah", "score of round": 1},
                   {player_3: "Alexandra", "score of round": 6}, {player_4: "Isaac", "score of round": 2},
                   {player_5: "Eddy", "score of round": 4}, {player_6: "Thomas", "score of round": 5},
                   {player_7: "Elodie", "score of round": 2}, {player_8: "Ines", "score of round": 1.5}]
    print("The player list sorted by total score of round:")
    print(sorted(player_list, key=lambda i: (i["score of round"])))


class SwissTournamentSystem:

    def generate_new_pairs_of_players(self, player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                      player_8):
        pass

# I repeat the two last functions until the end of tournament.
