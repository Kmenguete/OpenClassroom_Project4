from OpenClassroom_projet4.model.player_model import Player


class PlayerSerializer:
    """The serialization is the way that let us store our class object in the database. The package used to store
    data is called "TinyDB". Unfortunately, we found that this package was not very suitable
    for this project but this package was required by the customer. To store a player object, we should convert it into
    a dictionary. The serialization let us convert an object into a dictionary and to get this object back
    to the program (in particular when a report is requested), we deserialize it(meaning we convert our dictionary into
    an object).
    """

    @staticmethod
    def serialize(player: Player):
        """The serialize method serializes Player object."""
        serialized_player = {
            "first_name": player.firstname,
            "last_name": player.last_name,
            "rank": player.rank,
            "player_id": player.player_id,
            "total_score": player.total_score,
            "date_of_birth": player.date_of_birth,
        }
        return serialized_player

    @staticmethod
    def deserialize(serialized_player: dict):
        """The deserialize method deserializes Player object."""
        return Player(
            last_name=serialized_player["last_name"],
            firstname=serialized_player["first_name"],
            rank=serialized_player["rank"],
            player_id=serialized_player["player_id"],
            total_score=serialized_player["total_score"],
            date_of_birth=serialized_player["date_of_birth"],
        )
