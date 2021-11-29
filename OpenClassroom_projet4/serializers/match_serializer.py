from OpenClassroom_projet4.serializers.player_serializer import PlayerSerializer
from OpenClassroom_projet4.model.match_model import Match


class MatchSerializer:
    """ The serialization is the way that let us to store our class object in the database. The package used to store
    data is called "TinyDB". During the development of the application, we found that this package was not very suitable
    for this project but this package was required by the customer. To store a match object, we should convert it into
    a dictionary. The serialization is the process of converting an object into a dictionary and to get this object
    back to the program (in particular when a report is requested), we deserialize it(meaning we convert our dictionary
    into an object). To serialize a match object, we should first serialize two players because a match consist of two
    players and their score.
    """

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
