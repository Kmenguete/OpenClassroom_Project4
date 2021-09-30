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
    # We want to generate pairs of players randomly
    player_list = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
    matches = {}
    while len(player_list) > 1:
        r1 = random.randrange(0, len(player_list))
        elem1 = player_list.pop(r1)
        r2 = random.randrange(0, len(player_list))
        elem2 = player_list.pop(r2)
        matches[elem1] = elem2
        i = 1
        for key, value in matches.items():
            print("Match {}: {} and {}".format(i, key, value))
            i += 1


def sort_players_by_score_round(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                player_8):
    # When a round is finished, players should be sorted according their total number of points for the round.
    # This new sorted list will be the new rank for the next round. If two players has the same number of points,
    # they are sorted by rank.
    player_list = {'1st': player_1, '2nd': player_2, '3rd': player_3, '4th': player_4, '5th': player_5,
                   '6th': player_6, '7th': player_7, '8th': player_8}
    sorted_player_list = sorted(player_list)
    print("When a round is finished, please, update the rank of players according their scores, if two players has "
          "the same score then promote "
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
    print("If the player 1 has already met the player 2 then he meet the player 3. If the player 3 has already met "
          "the player 4 then he meet the player 5 and so on.")
    print("Please, repeat the process until the end of tournament")

# I repeat the two last functions until the end of tournament.
