from tinydb import Query, TinyDB
from OpenClassroom_projet4.serializers.match_serializer import MatchSerializer
from OpenClassroom_projet4.utils.config import Config


class MatchTable:
    """The match table is the table where match object are stored in the database. To store a match object,
    we first need to store two players because a match consist of two players and their score.
    """

    def __init__(self):
        """The init method is used to import every module required to save and update matches."""
        self.database = TinyDB(Config.DATABASE_NAME)
        self.match_database = self.database.table(Config.MATCH_TABLE_NAME)
        self.match_serializer = MatchSerializer()

    def save_match(self, match):
        """The save_match method is used to save one match in the database."""
        serialized_match = self.match_serializer.serialize(match)
        self.match_database.insert(serialized_match)

    def get_match(self, match_id):
        """The get_match method is used to retrieve one match from the database."""
        match_query = Query()
        serialized_match = self.match_database.search(match_query.match_id == match_id)
        match = self.match_serializer.deserialize(serialized_match[0])
        return match

    def save_matches(self, matches: list):
        """The save_matches method is used to save a list of matches."""
        serialized_matches = []
        for match in matches:
            serialized_match = self.match_serializer.serialize(match)
            serialized_matches.append(serialized_match)
        self.match_database.insert_multiple(serialized_matches)

    def get_matches(self):
        """The get_matches method is used to retrieve a list of matches from the database."""
        serialized_matches = self.match_database.all()
        matches = []
        for serialized_match in serialized_matches:
            match = self.match_serializer.deserialize(serialized_match)
            matches.append(match)
        return matches

    def update_match(self, match_id):
        """The update_match method is used to update one match in the database."""
        match = Query()
        self.match_database.update({"match_id": match_id}, match.match_id == match_id)

    def clear_database(self):
        """The clear_database method is used to delete every match object in the database."""
        self.match_database.truncate()
