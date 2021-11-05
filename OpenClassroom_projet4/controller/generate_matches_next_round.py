from OpenClassroom_projet4.model.Match_model import Match


def generate_matches_next_round(player_list, tournament):
    non_available_players = []
    match_list = []
    for index_player in range(len(player_list) - 1):
        player_a = player_list[index_player]
        if player_a in non_available_players:
            pass
        else:
            try:
                player_b = tournament.get_next_available_player(player_a, index_player + 1, non_available_players)
                non_available_players.append(player_a)
                non_available_players.append(player_b)
                match = Match(player_a, player_b)
                match_list.append(match)
                match.display_match()
            except IndexError:
                print("Unable to get player B as opponent of player A: " + player_a.firstname + " " +
                      player_a.last_name)
    return match_list
