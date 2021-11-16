from tinydb import TinyDB, Query

from OpenClassroom_projet4.database.match_serializer import MatchSerializer
from OpenClassroom_projet4.model.Match_model import Match


class MatchTable:

    def __init__(self):
        self.match_database = TinyDB('matches_database.json')
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
        return matches

    def update_match(self, match_id):
        match = Query()
        self.match_database.update({'match_id': match_id}, match.match_id == match_id)

    def clear_database(self):
        self.match_database.truncate()


if __name__ == '__main__':
    match_1 = Match(match_id='Q7STS76FS87G', player_a='Samantha Paraba', score_player_a=0, player_b='Daniel Pepeou',
                    score_player_b=1)
    match_2 = Match(match_id='Q7STS76FS87G', player_a='Sarah Heynes', score_player_a=0.5, player_b='Rosalie Seicheine',
                    score_player_b=0.5)
    MatchTable().save_matches([match_1, match_2])
    dsm = MatchTable().get_matches()
    print(dsm)
