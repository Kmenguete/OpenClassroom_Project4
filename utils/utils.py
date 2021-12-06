""" The utils file stores utils functions of the application.
"""


def transform_player_list_to_dictionary(players_list):
    new_players_dict = {}
    for player in players_list:
        new_players_dict[player.player_id] = player
    return new_players_dict


def transform_player_dict_to_list(player_dict: dict):
    return [v for v in player_dict.values()]
