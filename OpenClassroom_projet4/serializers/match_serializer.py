from OpenClassroom_projet4.serializers.player_serializer import PlayerSerializer
from OpenClassroom_projet4.model.Match_model import Match


class MatchSerializer:

    def __init__(self):
        self.player_serializer = PlayerSerializer()

    def serialize(self, match: Match):
        serialized_player_a = self.player_serializer.serialize(match.player_a)
        serialized_player_b = self.player_serializer.serialize(match.player_b)
        serialized_match = {'match_id': match.match_id, 'player_a': serialized_player_a,
                            'score_player_a': match.score_player_a, 'player_b': serialized_player_b,
                            'score_player_b': match.score_player_b}
        return serialized_match

    def deserialize(self, serialized_match: dict):
        deserialized_player_a = self.player_serializer.deserialize(serialized_match['player_a'])
        deserialized_player_b = self.player_serializer.deserialize(serialized_match['player_b'])
        return Match(match_id=serialized_match['match_id'], player_a=deserialized_player_a,
                     score_player_a=serialized_match['score_player_a'], player_b=deserialized_player_b,
                     score_player_b=serialized_match['score_player_b'])
