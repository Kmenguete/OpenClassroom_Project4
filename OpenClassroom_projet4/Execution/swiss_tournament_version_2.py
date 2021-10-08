import random


def generate_match_first_round(*player):
    return player


def pairs_of_players(*player):
    # We want to generate pairs of players randomly from player_list
    player_list = [*player]
    matches = {}
    while len(player_list) > 1:
        # We split our list in two part(player list a and player list b)
        # We randomly pop out one player in each list
        player_list_a = random.randrange(0, len(player_list))
        player_a = player_list.pop(player_list_a)
        player_list_b = random.randrange(0, len(player_list))
        player_b = player_list.pop(player_list_b)
        # Our selected players are paired and then a match is generated(in a dictionary format)
        matches[player_a] = player_b
        # Our players are now in a dictionary. Now we well print our pairs of players(matches)
        i = 1
        for key, value in matches.items():
            print("match {}: {} and {}".format(i, key, value))


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


def generate_new_pairs_of_players(player_1, rank_player_1, player_2, rank_player_2, player_3, rank_player_3, player_4,
                                  rank_player_4, player_5, rank_player_5, player_6, rank_player_6, player_7,
                                  rank_player_7, player_8, rank_player_8):
    # For the next round, the player 1 meet the player 2, the player 3 meet the player 4 and so on.
    # If the player 1 has already met the player 2 then he meet the player 3. If the player 3 has already
    # met the player 4 then he meet the player 5 and so on.
    match_1 = ((player_1, rank_player_1), (player_2, rank_player_2))
    match_2 = ((player_3, rank_player_3), (player_4, rank_player_4))
    match_3 = ((player_5, rank_player_5), (player_6, rank_player_6))
    match_4 = ((player_7, rank_player_7), (player_8, rank_player_8))
    print("Here is the match one: ", match_1, "Here is the match two: ", match_2, "Here is the match three: ", match_3,
          "Here is the match four: ", match_4)
    if ((player_1, rank_player_1), (player_2, rank_player_2)) in globals():
        match_1 = ((player_1, rank_player_1), (player_3, rank_player_3))
        print("Player 1 has already met player 2, here is match one: ", match_1)
    if ((player_3, rank_player_3), (player_4, rank_player_4)) in globals():
        match_2 = ((player_3, rank_player_3), (player_5, rank_player_5))
        print("Player 3 has already met player 4, here is match two: ", match_2)
    if ((player_5, rank_player_5), (player_6, rank_player_6)) in globals():
        match_3 = ((player_5, rank_player_5), (player_7, rank_player_7))
        print("Player 5 has already met player 6, here is match three: ", match_3)
    if ((player_7, rank_player_7), (player_8, rank_player_8)) in globals():
        match_4 = ((player_7, rank_player_7), (player_1, rank_player_1))
        print("Player 7 has already met player 8, here is match four: ", match_4)
# I repeat the two last functions until the end of tournament.
