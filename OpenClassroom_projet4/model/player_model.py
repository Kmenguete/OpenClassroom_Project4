import uuid


class Player:
    """ The player model is the class that let to create a player object(in other words, an instance of class Player).
    """

    def __init__(self, last_name, firstname, rank, total_score=0, player_id=None, date_of_birth=None, sex=None):
        """ The init method gives the attributes of Player object.
        """
        self.player_id = self.get_player_id(player_id)
        self.last_name = last_name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = int(rank)
        self.total_score = total_score

    @staticmethod
    def get_player_id(player_id):
        """ The get_player_id method return the player_id of Player object.
                """
        if player_id is None:
            player_id = str(uuid.uuid4())
        return player_id

    def __getitem__(self, player):
        """ The getitem method let to access a Player object as an item.
                        """
        player = self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank) + ", " + "score: " + \
            str(self.total_score)
        return player

    def __str__(self):
        """ The str method gives the string representation of a Player object when it is printing.
                                """
        return self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank) + ", " + "score: " + \
            str(self.total_score)

    def __repr__(self):
        """ The repr method gives the representation of a Player object when it is printing.
                                        """
        return "Player(" + repr(self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank)) + ", " \
               + "score: " + str(self.total_score) + ")"

    def __add__(self, other):
        """ The add method let to add different instances of Player in a list.
                                                """
        return self.firstname + " " + self.last_name + " " + "rank: " + str(self.rank) + ", " + "score: " + \
            str(self.total_score) + " " + other.firstname + " " + other.last_name + " " + "rank: " + \
            str(other.rank) + ", " + "score: " + str(other.total_score)
