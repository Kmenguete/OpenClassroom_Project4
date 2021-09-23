from OpenClassroom_projet4.controller.Controller import Controller


class Round:
    def _init_(self, name_of_tournament, round_number, match_number):
        self.name_of_tournament = name_of_tournament
        self.round_number = round_number
        self.match_number = match_number


def controller_update():
    return Controller
