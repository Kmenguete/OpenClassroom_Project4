from OpenClassroom_projet4.controller.Controller import Controller


class Match:
    def _init_(self, player_1, player_2, score_player_1, score_player_2):
        self.player_1 = player_1
        self.score_player_1 = score_player_1
        self.player_2 = player_2
        self.score_player_2 = score_player_2


def controller_update():
    return Controller
