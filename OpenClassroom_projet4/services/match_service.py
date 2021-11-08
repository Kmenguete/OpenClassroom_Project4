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
