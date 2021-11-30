import uuid


class Match:
    """ The match model is the class that let to create a match object. It is not possible to create a match object
    without creating players object. This is why, in the running of the tournament, we first ask the user to create
    players before the application creates the first round and generate matches.
    """
    def __init__(self, player_a, player_b, score_player_a=None, score_player_b=None,  match_id=None):
        """ The init method gives the attributes of Match object.
        """
        self.match_id = self.get_match_id(match_id)
        self.player_a = player_a
        self.score_player_a = score_player_a
        self.player_b = player_b
        self.score_player_b = score_player_b

    def display_match(self):
        """ The display_match method display matches during the running of the tournament.
                """
        print("Match: " + self.player_a.firstname + " " + self.player_a.last_name + " vs " + self.player_b.firstname +
              " " + self.player_b.last_name)
        return "Match: " + self.player_a.firstname + " " + self.player_a.last_name + " vs " + self.player_b.firstname \
               + " " + self.player_b.last_name

    @staticmethod
    def get_match_id(match_id):
        """ The get_match_id method return the match_id of every matches.
                        """
        if match_id is None:
            match_id = str(uuid.uuid4())
        return match_id

    def __str__(self):
        """ The str method define the string representation of Match object when it is printed.
                                """
        return "Match_id: " + self.match_id + " " + "Match: " + str(self.player_a) + ", score: " + \
               str(self.score_player_a) + " vs " + str(self.player_b) + ", score: " + str(self.score_player_b)

    def __repr__(self):
        """ The repr method define the representation of Match object when it is printed.
                                        """
        return "Match_id: " + self.match_id + " " + "Match: " + str(self.player_a) + ", score: " + \
               str(self.score_player_a) + " vs " + str(self.player_b) + ", score: " + str(self.score_player_b)
