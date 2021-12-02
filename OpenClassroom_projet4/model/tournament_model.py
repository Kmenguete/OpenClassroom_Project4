import uuid

DEFAULT_ROUNDS_NUMBER = 4


class Tournament:
    """The tournament model is the class that let the user create a tournament. Once, the user created a tournament,
    a tournament object is created from the tournament model. At the beginning of the tournament, when it is created by
    the user, rounds does not exist yet. rounds and players will be progressively attached to the tournament during the
    running of the application. Each time, players, rounds and matches are created, they are automatically attached to
    the tournament.
    """

    def __init__(
        self,
        name,
        place,
        date,
        description,
        number_of_rounds=DEFAULT_ROUNDS_NUMBER,
        tournament_id=None,
        rounds=None,
        players=None,
        players_dict=None,
    ):
        """The init method gives the attributes of Tournament object."""
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.tournament_id = self.get_tournament_id(tournament_id)
        self.rounds = rounds
        self.players = players
        self.players_dict = players_dict
        self.description = description

    @staticmethod
    def get_tournament_id(tournament_id):
        """The get_tournament_id method return the tournament_id of Tournament object."""
        if tournament_id is None:
            tournament_id = str(uuid.uuid4())
        return tournament_id

    def __str__(self):
        """The str method gives a string representation of Tournament object when it is printed."""
        return (
            "name: "
            + self.name
            + ", "
            + "place: "
            + self.place
            + ", "
            + "description: "
            + self.description
            + ", "
            + " number_of_rounds: "
            + str(self.number_of_rounds)
            + ", "
            + "tournament_id: "
            + self.tournament_id
            + " rounds: "
            + str(self.rounds)
            + " "
            + str(self.date)
        )

    def __repr__(self):
        """The repr method return the str method of Tournament object."""
        return self.__str__()

    def __len__(self):
        """The len method return the length of player list of Tournament object."""
        return len(self.players)

    def __getitem__(self, players, i):
        """The getitem method let to access a Player object from the player list of Tournament object."""
        return self.players[i]
