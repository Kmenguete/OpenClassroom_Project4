import operator
import random


def generate_match_first_round(player_list):
    # We first sort players by rank.
    sorted_player_list = sorted(player_list, key=operator.attrgetter("rank"))
    print("At the beginning of the first round, players are sorted by rank.")
    print(sorted_player_list)

    # Once, we sorted our players by rank, we split them in two part(an upper half and a lower half).
    first_half = sorted_player_list[:len(sorted_player_list) // 2]
    second_half = sorted_player_list[len(sorted_player_list) // 2:]
    print("Here is the first half: ", first_half, "Here is the second half: ", second_half)
    # And finally, we generates matches according rank and group. The best player of the first group meet the best
    # player of the second group. The second best player of the first group meet the second best player of the second
    # group and so on.
    match_list = zip(first_half, second_half)
    print("Here are the matches of the first round. Each parenthesis is a match. Player a is on the left and player b"
          " on the right.")
    for match in match_list:
        print(match)


def pairs_of_players(player_list):
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
            i += 1


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


def generate_new_pairs_of_players(player_list):
    # For the next round, the player 1 meet the player 2, the player 3 meet the player 4 and so on.
    # If the player 1 has already met the player 2 then he meet the player 3. If the player 3 has already
    # met the player 4 then he meet the player 5 and so on.
    for player in player_list:
        match_next_round = (player[0], player[1])
        print("Here is the match for the next round: ")
        print(match_next_round)
        i = 0
        n = 1
        if match_next_round in globals():
            match_next_round = (player[0], player[2])
            print("The player {} has already met the player {}. Here is the match for the next round: ".format(i, n),
                  match_next_round)
            i += 1
            n += 1
