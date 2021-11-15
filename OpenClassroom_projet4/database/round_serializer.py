from OpenClassroom_projet4.model.Round_model import Tour


class RoundSerializer:

    @staticmethod
    def serialize(round: Tour):
        serialized_round = {'round_name': round.round_name, 'start_date': round.start_date, 'matches': round.matches}
        return serialized_round

    @staticmethod
    def deserialize(serialized_round: dict):
        return Tour(round_name=serialized_round['round_name'], start_date=serialized_round['start_date'],
                    matches=serialized_round['matches'])
