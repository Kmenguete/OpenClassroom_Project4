import random


def sort_player_by_rank(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
    # The goal of this function is to sort players by rank.
    # My Player class instances will be store in variables player_1, player_2, player_3...etc.
    # The rank of my players are the key of my dictionary. my dictionary will be sorted by key.
    player_list = {'1st': player_1, '2nd': player_2, '3rd': player_3, '4th': player_4, '5th': player_5,
                   '6th': player_6, '7th': player_7, '8th': player_8}
    sorted_player_list = sorted(player_list)
    print("At the beginning of the first round, please, sort the players according the rank of each one: ",
          sorted_player_list)


def split_total_number_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                  player_8):
    # We want to split players in two group. The first half return the first half of the group. The second half return
    # the second half of the group.
    player_list = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
    first_half = player_list[:4]
    second_half = player_list[4:]
    print("Here this is the first half: ", first_half, "Here this is the second half: ", second_half)


def pairs_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
    # We want to generate pairs of players randomly from player_list_a and player_list_b
    # a player from player_list_a is randomly selected to play with a randomly selected player from player_list_b
    player_list_a = [player_1, player_2, player_3, player_4]
    player_list_b = [player_5, player_6, player_7, player_8]
    random.shuffle(player_list_a)
    random.shuffle(player_list_b)
    # Merge the two lists into a new list of pairs
    match_list = zip(player_list_a, player_list_b)
    print("Here is your randomly generated matches. Each parenthesis is a match. Player_a is on the left and "
          "player_b is on the right.")
    for match in match_list:
        print(match)


def sort_players_by_score_round(player_1, score_player_1, player_2, score_player_2, player_3, score_player_3, player_4,
                                score_player_4, player_5, score_player_5, player_6, score_player_6, player_7,
                                score_player_7, player_8, score_player_8):
    # We want to sort players by their score at the end of each round. We sort players in descending order.
    # Consequently, we sort our dictionary by value in descending order.
    player_list = {player_1: score_player_1, player_2: score_player_2, player_3: score_player_3,
                   player_4: score_player_4, player_5: score_player_5, player_6: score_player_6,
                   player_7: score_player_7, player_8: score_player_8}
    sorted_player_list = sorted(player_list.items(), key=lambda x: x[1], reverse=True)
    print("Players are sorted by their score in descending order at the end of each round:")
    for player in sorted_player_list:
        print(player[0], player[1])


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
    if ('player_1', 'player_2') in globals():
        match_1 = [player_1, player_3]
        print("Player 1 has already met player 2, here is match one: ", match_1)
    if ('player_3', 'player_4') in globals():
        match_2 = [player_3, player_5]
        print("Player 3 has already met player 4, here is match two: ", match_2)
    if ('player_5', 'player_6') in globals():
        match_3 = [player_5, player_7]
        print("Player 5 has already met player 6, here is match three: ", match_3)
    if ('player_7', 'player_8') in globals():
        match_4 = [player_7, player_1]
        print("Player 7 has already met player 8, here is match four: ", match_4)
# I repeat the two last functions until the end of tournament.
