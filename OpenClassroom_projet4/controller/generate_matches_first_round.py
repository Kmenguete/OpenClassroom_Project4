import operator


def generate_matches_first_round(player_list):
    print("\n ****************************** We are generating the player pair... ****************************")
    sorted_player_list = sorted(player_list, key=operator.attrgetter("rank"))
    first_half = sorted_player_list[:len(sorted_player_list) // 2]
    second_half = sorted_player_list[len(sorted_player_list) // 2:]
    player_pairs = list(list(x) for x in zip(first_half, second_half))
    print(tuple(player_pairs))
    return tuple(player_pairs)
