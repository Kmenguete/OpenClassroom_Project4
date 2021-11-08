
def transform_player_list_to_dictionary(players_list):
    new_players_dict = {}
    for player in players_list:
        new_players_dict[player.player_id] = player
    return new_players_dict
