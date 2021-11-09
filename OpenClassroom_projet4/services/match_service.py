from OpenClassroom_projet4.model.Match_model import Match


class MatchService:

    def __init__(self):
        self.match_list = None
        # TODO we may need to take this off this class

    def create_matches_from_player_pairs(self, player_pairs):
        match_list = []
        for player_pair in player_pairs:
            match = Match(player_pair[0], player_pair[1])
            match_list.append(match)
        self.update_match_list(match_list)

    def update_match_list(self, match_list):
        self.match_list = match_list

    def generate_matches_for_next_round(self, player_list, tournament_service):
        non_available_players = []
        match_list = []
        for index_player in range(len(player_list) - 1):
            player_a = player_list[index_player]
            if player_a in non_available_players:
                pass
            else:
                try:
                    player_b = tournament_service.get_next_available_player(player_a, index_player + 1,
                                                                            non_available_players)
                    non_available_players.append(player_a)
                    non_available_players.append(player_b)
                    match = Match(player_a, player_b)
                    match_list.append(match)
                    match.display_match()
                except IndexError:
                    print("Unable to get player B as opponent of player A: " + player_a.firstname + " " +
                          player_a.last_name)
        self.update_match_list(match_list)
        return match_list