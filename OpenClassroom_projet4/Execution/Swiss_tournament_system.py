
def sort_player_by_rank(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
    # The goal of this function is to sort players by rank.
    # My Player class instances will be store in variables player_1, player_2, player_3...etc.
    # The rank of my players are the key of my dictionary. my dictionary will be sorted by key.
    player_list = {'1st': player_1, '2nd': player_2, '3rd': player_3, '4th': player_4, '5th': player_5,
                   '6th': player_6, '7th': player_7, '8th': player_8}
    sorted_player_list = sorted(player_list)
    print("Please, sort the players according the rank of each one: ", sorted_player_list)


def split_total_number_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                  player_8):
    # We want to split players in two group. The first half return the first half of the group. The second half return
    # the second half of the group.
    player_list = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
    first_half = player_list[:3]
    second_half = player_list[3:]
    print("Here this is the first half: ", first_half, "Here this is the second half: ", second_half)


def pairs_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
    # Pairs of players are generated according the rank of each group of players. The best player of the first group
    # will play with the best player of the 2nd group. The 2nd best player of the first group will play with the 2nd
    # best player of the 2nd group and so on.
    match_1 = [player_1, player_2]
    match_2 = [player_3, player_4]
    match_3 = [player_5, player_6]
    match_4 = [player_7, player_8]
    print("Here is the match one: ", match_1, "Here is the match two: ", match_2, "Here is the match three: ", match_3,
          "Here is the match four: ", match_4)


def sort_players_by_score_round(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                player_8):
    # When a round is finished, players should be sorted according their total number of points for the round.
    # This new sorted list will be the new rank for the next round. If two players has the same number of points,
    # they are sorted by rank.
    player_list = {'1st': player_1, '2nd': player_2, '3rd': player_3, '4th': player_4, '5th': player_5,
                   '6th': player_6, '7th': player_7, '8th': player_8}
    sorted_player_list = sorted(player_list)
    print("Please, update the rank of players according their scores, if two players has the same score then promote "
          "the best rank of the last round: ", sorted_player_list)


def generate_new_pairs_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                  player_8):
    # For the next round, the player 1 meet the player 2, the player 3 meet the player 4 and so on.
    # If the player 1 has already met the player 2 then he meet the player 3. If the player 3 has already
    # met the player 4 then he meet the player 5 and so on.
    match_1 = [player_1, player_2]
    match_2 = [player_3, player_4]
    match_3 = [player_5, player_6]
    match_4 = [player_7, player_8]
    print("Here is the match one: ", match_1, "Here is the match two: ", match_2, "Here is the match three: ", match_3,
          "Here is the match four: ", match_4)

# I repeat the two last functions until the end of tournament.
