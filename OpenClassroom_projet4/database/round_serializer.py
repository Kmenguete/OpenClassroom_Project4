from datetime import datetime

from OpenClassroom_projet4.model.Round_model import Tour


class RoundSerializer:

    @staticmethod
    def serialize(round: Tour):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        serialized_round = {'round_id': round.round_id, 'round_name': round.round_name, 'start_date': date_time,
                            'matches': round.matches}
        return serialized_round

    @staticmethod
    def deserialize(serialized_round: dict):
        return Tour(round_id=serialized_round['round_id'], round_name=serialized_round['round_name'],
                    start_date=serialized_round['start_date'], matches=serialized_round['matches'])
