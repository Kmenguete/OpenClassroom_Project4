import uuid


class Match:
    def __init__(self, player_a, player_b, score_player_a=None, score_player_b=None,  match_id=None):
        self.match_id = self.get_match_id(match_id)
        self.player_a = player_a
        self.score_player_a = score_player_a
        self.player_b = player_b
        self.score_player_b = score_player_b

    def display_match(self):
        print("Match: " + self.player_a.firstname + " " + self.player_a.last_name + " vs " + self.player_b.firstname +
              " " + self.player_b.last_name)
        return "Match: " + self.player_a.firstname + " " + self.player_a.last_name + " vs " + self.player_b.firstname \
               + " " + self.player_b.last_name

    @staticmethod
    def get_match_id(match_id):
        if match_id is None:
            match_id = str(uuid.uuid4())
        return match_id

    def __str__(self):
        return "Match_id: " + self.match_id + " " + "Match: " + str(self.player_a) + ", score: " + \
               str(self.score_player_a) + " vs " + str(self.player_b) + ", score: " + str(self.score_player_b)

    def __repr__(self):
        return "Match_id: " + self.match_id + " " + "Match: " + str(self.player_a) + ", score: " + \
               str(self.score_player_a) + " vs " + str(self.player_b) + ", score: " + str(self.score_player_b)
