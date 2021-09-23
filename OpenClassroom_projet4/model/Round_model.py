from OpenClassroom_projet4.controller.Controller import Controller


class Round:
    def _init_(self, name_of_tournament, round_number, match_number, score_player_1, score_player_2):
        self.name_of_tournament = name_of_tournament
        self.round_number = round_number
        self.match_number = match_number
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2


def controller_update():
    return Controller
