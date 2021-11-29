from tinydb import Query, TinyDB
from OpenClassroom_projet4.serializers.match_serializer import MatchSerializer
from OpenClassroom_projet4.model.match_model import Match
from OpenClassroom_projet4.model.player_model import Player
from OpenClassroom_projet4.utils.config import Config


class MatchTable:
    """ The match table is the table where match object are stored in the database. To store a match object,
    we first need to store two players because a match consist of two players and their score.
    """

    def __init__(self):
        self.database = TinyDB(Config.DATABASE_NAME)
        self.match_database = self.database.table(Config.MATCH_TABLE_NAME)
        self.match_serializer = MatchSerializer()

    def save_match(self, match):
        serialized_match = self.match_serializer.serialize(match)
        self.match_database.insert(serialized_match)

    def get_match(self, match_id):
        match_query = Query()
        serialized_match = self.match_database.search(match_query.match_id == match_id)
        match = self.match_serializer.deserialize(serialized_match[0])
        return match

    def save_matches(self, matches: list):
        serialized_matches = []
        for match in matches:
            serialized_match = self.match_serializer.serialize(match)
            serialized_matches.append(serialized_match)
        self.match_database.insert_multiple(serialized_matches)

    def get_matches(self):
        serialized_matches = self.match_database.all()
        matches = []
        for serialized_match in serialized_matches:
            match = self.match_serializer.deserialize(serialized_match)
            matches.append(match)
        for match in matches:
            print(match)
        return matches

    def update_match(self, match_id):
        match = Query()
        self.match_database.update({'match_id': match_id}, match.match_id == match_id)

    def clear_database(self):
        self.match_database.truncate()


if __name__ == '__main__':
    player_1 = Player(last_name='Darden', firstname='Mike', rank=5, player_id='46464646QSDFSD64', total_score=3)
    player_2 = Player(last_name='Mikaela', firstname='Arnold', rank=7, player_id='1234RF5456GH46TFD', total_score=1)

    match_1 = Match(match_id='Q7STS76FS87G', player_a=player_1, score_player_a=0, player_b=player_2,
                    score_player_b=1)
    match_2 = Match(match_id='Q7STS76FS87G', player_a=player_1, score_player_a=0.5, player_b=player_2,
                    score_player_b=0.5)
    MatchTable().save_matches([match_1, match_2])
    dsm = MatchTable().get_matches()
    print(dsm)
