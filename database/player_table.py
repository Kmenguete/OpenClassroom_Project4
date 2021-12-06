from tinydb import Query, TinyDB

from OpenClassroom_projet4.serializers.player_serializer import PlayerSerializer
from OpenClassroom_projet4.utils.config import Config


class PlayerTable:
    """Here, this is the player table. The player table is a class that store players object in the database
    and gather them in a table named "player_table". In the database, there is a table for each object(a table for the
    tournament, a table for the rounds and so on.).
    """

    def __init__(self):
        """The init method is used to import every module required to save and update players."""
        self.database = TinyDB(Config.DATABASE_NAME)
        self.player_table = self.database.table(Config.PLAYER_TABLE_NAME)
        self.player_serializer = PlayerSerializer()

    def save_player(self, player):
        """The save_player method is used to save one player in the database."""
        serialized_player = self.player_serializer.serialize(player)
        self.player_table.insert(serialized_player)

    def get_player(self, player_id):
        """The get_player method is used to retrieve one player from the database."""
        player_query = Query()
        serialized_player = self.player_table.search(
            player_query.player_id == player_id
        )
        player = self.player_serializer.deserialize(serialized_player[0])
        return player

    def save_players(self, players: list):
        """The save_players method is used to save a list of players."""
        serialized_players = []
        for player in players:
            serialized_player = self.player_serializer.serialize(player)
            serialized_players.append(serialized_player)
        self.player_table.insert_multiple(serialized_players)

    def save_or_update(self, players: list):
        """The save_or_update method is used to save or update a list of players."""
        serialized_players = []
        for player in players:
            serialized_player = self.player_serializer.serialize(player)
            serialized_players.append(serialized_player)
            Player = Query()
            self.player_table.upsert(
                serialized_player, Player.player_id == player.player_id
            )

    def get_players(self):
        """The get_players method is used to retrieve a list of players from the database."""
        serialized_players = self.player_table.all()
        players = []
        for serialized_player in serialized_players:
            player = self.player_serializer.deserialize(serialized_player)
            players.append(player)
        return players

    def update_player_total_score(self, player_id, total_score):
        """The update_player_total_score method is used to update the total score of players in the database."""
        Player = Query()
        self.player_table.update(
            {"total_score": total_score}, Player.player_id == player_id
        )

    def clear_database(self):
        """The clear_database method is used to delete every player object in the database."""
        self.player_table.truncate()
