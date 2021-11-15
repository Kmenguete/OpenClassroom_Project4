import uuid


class Player:

    def __init__(self, last_name, firstname, rank, total_score=0, date_of_birth=None,
                 sex=None):
        self.player_id = str(uuid.uuid4())
        self.last_name = last_name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = int(rank)
        self.total_score = total_score

    def __getitem__(self, player):
        player = self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank) + ", " + "score: " + \
                 str(self.total_score)
        return player

    def __str__(self):
        return self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank) + ", " + "score: " + \
               str(self.total_score)

    def __repr__(self):
        return "Player(" + repr(self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank)) + ", " \
               + "score: " + str(self.total_score) + ")"

    def __add__(self, other):
        return self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank) + ", " + "score: " + \
               str(self.total_score) + " " + other.firstname + " " + other.last_name + " " + "rank: " + \
               str(other.rank) + ", " + "score: " + str(other.total_score)

    def update_rank(self, player_list, index):
        self.rank = index + 1
        return player_list[index]
