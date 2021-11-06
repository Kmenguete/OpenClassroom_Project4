

def sort_players_by_total_score(tournament):
    sorted_dictionary_by_total_score = sorted(tournament.players_dict.items(), key=lambda x: x[1], reverse=True)
    tournament.players_dict = dict(sorted_dictionary_by_total_score)
    tournament.display_players()
