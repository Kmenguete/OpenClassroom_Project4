

def add_final_score_to_players(player_list, players_dict):
    for player_index in range(0, len(player_list)):
        player_list[player_index].total_score = players_dict[player_list[player_index].player_id]
        return player_list[player_index].total_score
