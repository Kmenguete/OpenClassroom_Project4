from OpenClassroom_projet4.view.Player_view import create_player
from OpenClassroom_projet4.view.Tournament_view import create_tournament, create_round, create_match


class Controller:
    def _init_(self):
        self.tournament = create_tournament()
        self.round = create_round()
        self.match = create_match()
        self.player = create_player()
