import operator


def sort_players_by_rank(player_list):
    sorted_player_list = sorted(player_list, key=operator.attrgetter("rank"))
    return sorted_player_list
