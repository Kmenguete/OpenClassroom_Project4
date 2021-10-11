

class Player:
    def __init__(self, last_name, firstname, rank, date_of_birth=None, sex=None):
        self.last_name = last_name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = int(rank)

    def __getitem__(self, player_list, item):
        return player_list[item]

    def __str__(self):
        return self.last_name + self.rank

    def __repr__(self):
        return "Player(" + repr(self.last_name + str(self.rank)) + ")"
