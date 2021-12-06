from tinydb import Query, TinyDB
from OpenClassroom_projet4.serializers.round_serializer import RoundSerializer
from OpenClassroom_projet4.utils.config import Config


class RoundTable:
    """The round table stores rounds object of a tournament. To store a round, we need to store matches and to store
    matches, we need to store players. Each table, depend on each other to save properly, an entire tournament.
    """

    def __init__(self):
        """The init method is used to import every module required to save and update rounds."""
        self.database = TinyDB(Config.DATABASE_NAME)
        self.round_database = self.database.table(Config.ROUND_TABLE_NAME)
        self.round_serializer = RoundSerializer()

    def save_round(self, round):
        """The save_round method is used to save one round in the database."""
        serialized_round = self.round_serializer.serialize(round)
        self.round_database.insert(serialized_round)

    def get_round(self, round_id):
        """The get_round method is used to retrieve one round from the database."""
        round_query = Query()
        serialized_round = self.round_database.search(round_query.round_id == round_id)
        round = self.round_serializer.deserialize(serialized_round[0])
        return round

    def save_rounds(self, rounds: list):
        """The save_rounds method is used to save a list of rounds."""
        serialized_rounds = []
        for round in rounds:
            serialized_round = self.round_serializer.serialize(round)
            serialized_rounds.append(serialized_round)
        self.round_database.insert_multiple(serialized_rounds)

    def get_rounds(self):
        """The get_rounds method is used to retrieve a list of rounds from the database."""
        serialized_rounds = self.round_database.all()
        rounds = []
        for serialized_round in serialized_rounds:
            round = self.round_serializer.deserialize(serialized_round)
            rounds.append(round)
        for round in rounds:
            print(round)
        return rounds

    def clear_database(self):
        """The clear_database method is used to delete every round object in the database."""
        self.round_database.truncate()
