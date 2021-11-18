from tinydb import Query

from OpenClassroom_projet4.database.match_serializer import MatchSerializer
from OpenClassroom_projet4.database.player_serializer import PlayerSerializer
from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.utils.config import Config


class MatchTable:

    def __init__(self):
        self.database = Config.DATABASE
        self.match_serializer = MatchSerializer()
        self.match_table = self.database.table('Match_table')

    def save_match(self, match):
        serialized_match = self.match_serializer.serialize(match)
        self.match_table.insert(serialized_match)

    def get_match(self, match_id):
        match_query = Query()
        serialized_match = self.match_table.search(match_query.match_id == match_id)
        match = self.match_serializer.deserialize(serialized_match[0])
        return match

    def save_matches(self, matches: list):
        serialized_matches = []
        for match in matches:
            serialized_match = self.match_serializer.serialize(match)
            serialized_matches.append(serialized_match)
        self.match_table.insert_multiple(serialized_matches)

    def get_matches(self):
        serialized_matches = self.match_table.all()
        matches = []
        for serialized_match in serialized_matches:
            match = self.match_serializer.deserialize(serialized_match)
            matches.append(match)
        return matches

    def update_match(self, match_id):
        match = Query()
        self.match_table.update({'match_id': match_id}, match.match_id == match_id)

    def clear_match_table(self):
        self.match_table.truncate()


if __name__ == '__main__':
    player_3 = Player(last_name='Don', firstname='Kyrus', rank=8, player_id='46464646QSDFSD64', total_score=0)
    player_4 = Player(last_name='Al awal', firstname='Nawal', rank=1, player_id='1234RF5456GH46TFD', total_score=4)
    player_a = PlayerSerializer().serialize(player_3)
    player_b = PlayerSerializer().serialize(player_4)
    match_1 = Match(match_id='Q7STS76FS87G', player_a=player_a, score_player_a=0, player_b=player_b,
                    score_player_b=1)
    match_2 = Match(match_id='Q7STS76FS87G', player_a=player_a, score_player_a=0.5, player_b=player_b,
                    score_player_b=0.5)
    MatchTable().save_matches([match_1, match_2])
    dsm = MatchTable().get_matches()
    print(dsm)
