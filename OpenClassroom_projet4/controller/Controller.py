

class Controller:
    def _init_(self, tournament, round, match, player, score_of_player):
        self.tournament = tournament()
        self.round = round()
        self.match = match()
        self.player = player()
        self.score_of_player = score_of_player()
