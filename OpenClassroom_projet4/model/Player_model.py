
class Player:
    def __init__(self, last_name, firstname, rank, date_of_birth=None, sex=None):
        self.last_name = last_name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = int(rank)

    def __getitem__(self, player):
        player = self.last_name + " " + str(self.rank)
        return player

    def __str__(self):
        return self.last_name + " " + str(self.rank)

    def __repr__(self):
        return "Player(" + repr(self.last_name + " " + str(self.rank)) + ")"

    def __add__(self, other):
        return self.last_name + " " + str(self.rank) + " " + other.last_name + " " + str(other.rank)

    def update_rank(self, player_list, index):
        self.rank = index + 1
        return player_list[index]
