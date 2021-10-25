

class Match:
    def __init__(self, player_a, player_b, score_player_a=None, score_player_b=None):
        self.player_a = player_a
        self.score_player_a = score_player_a
        self.player_b = player_b
        self.score_player_b = score_player_b

    def display_match(self):
        print("Match: " + self.player_a.last_name + " vs " + self.player_b.last_name)
