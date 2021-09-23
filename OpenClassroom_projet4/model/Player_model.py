from OpenClassroom_projet4.controller.Controller import Controller


class Player:
    def _init_(self, surname, firstname, date_of_birth, sex, rank):
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = rank


def controller_update():
    return Controller
