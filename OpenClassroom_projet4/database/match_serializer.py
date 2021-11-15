from OpenClassroom_projet4.model.Match_model import Match


class MatchSerializer:

    @staticmethod
    def serialize(match: Match):
        serialized_match = {'player_a': match.player_a, 'score_player_a': match.score_player_a,
                            'player_b': match.player_b, 'score_player_b': match.score_player_b}
        return serialized_match

    @staticmethod
    def deserialize(serialized_match: dict):
        return Match(player_a=serialized_match['player_a'], score_player_a=serialized_match['score_player_a'],
                     player_b=serialized_match['player_b'], score_player_b=serialized_match['score_player_b'])
        