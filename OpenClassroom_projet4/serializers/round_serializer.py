from datetime import datetime

from OpenClassroom_projet4.serializers.match_serializer import MatchSerializer
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.utils.config import Config


class RoundSerializer:

    def __init__(self):
        self.match_serializer = MatchSerializer()

    def serialize(self, round: Tour):
        serialized_matches = []
        for match in round.matches:
            serialized_match = self.match_serializer.serialize(match)
            serialized_matches.append(serialized_match)

        date_time = round.start_date.strftime(Config.DATE_STRING_FORMAT)
        serialized_round = {'round_id': round.round_id, 'round_name': round.round_name, 'start_date': date_time,
                            'matches': serialized_matches}
        return serialized_round

    def deserialize(self, serialized_round: dict):
        deserialized_matches = []
        for serialized_match in serialized_round['matches']:
            match = self.match_serializer.deserialize(serialized_match)
            deserialized_matches.append(match)

        date_time_obj = datetime.strptime(serialized_round['start_date'], Config.DATE_STRING_FORMAT)

        return Tour(round_id=serialized_round['round_id'], round_name=serialized_round['round_name'],
                    start_date=date_time_obj, matches=deserialized_matches)
