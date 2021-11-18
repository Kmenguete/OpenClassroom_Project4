from datetime import datetime

from OpenClassroom_projet4.database.match_serializer import MatchSerializer
from OpenClassroom_projet4.model.Round_model import Tour


class RoundSerializer:

    def __init__(self):
        self.match_serializer = MatchSerializer()

    def serialize(self, round: Tour):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        serialized_matches = []
        for match in round.matches:
            serialized_match = self.match_serializer.serialize(match)
            serialized_matches.append(serialized_match)
        serialized_round = {'round_id': round.round_id, 'round_name': round.round_name, 'start_date': date_time,
                            'matches': serialized_matches}
        return serialized_round

    @staticmethod
    def deserialize(serialized_round: dict):
        return Tour(round_id=serialized_round['round_id'], round_name=serialized_round['round_name'],
                    start_date=serialized_round['start_date'], matches=serialized_round['matches'])
