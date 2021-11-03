import operator


def sort_player_by_final_score(player_list):
    sorted_player_list = sorted(player_list, key=operator.attrgetter("total_score"), reverse=True)
    player_list = sorted_player_list
    return player_list
