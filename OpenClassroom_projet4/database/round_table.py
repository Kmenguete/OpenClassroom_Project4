from tinydb import Query

from OpenClassroom_projet4.database.round_serializer import RoundSerializer
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.utils.config import Config


class RoundTable:

    def __init__(self):
        self.database = Config.DATABASE
        self.round_serializer = RoundSerializer()
        self.round_table = self.database.table('Round_table')

    def save_round(self, round):
        serialized_round = self.round_serializer.serialize(round)
        self.round_table.insert(serialized_round)

    def get_round(self, round_id):
        round_query = Query()
        serialized_round = self.round_table.search(round_query.round_id == round_id)
        round = self.round_serializer.deserialize(serialized_round[0])
        return round

    def save_rounds(self, rounds: list):
        serialized_rounds = []
        for round in rounds:
            serialized_round = self.round_serializer.serialize(round)
            serialized_rounds.append(serialized_round)
        self.round_table.insert_multiple(serialized_rounds)

    def get_rounds(self):
        serialized_rounds = self.round_table.all()
        rounds = []
        for serialized_round in serialized_rounds:
            round = self.round_serializer.deserialize(serialized_round)
            rounds.append(round)
        return rounds
    
    def update_round_name(self, name, round_id):
        round = Query()
        self.round_table.update({'round_name': name}, round.round_id == round_id)

    def clear_round_table(self):
        self.round_table.truncate()


if __name__ == '__main__':
    round_3 = Tour(round_id='EER7FT7ZF32874RG', round_name='Round_1', start_date='14/03/2020',
                   matches=['match_1', 'match_2', 'match_3', 'match_4'])
    round_4 = Tour(round_id='9854UT948T458T9', round_name='Round_2', start_date='21/09/2021',
                   matches=['match_1', 'match_2', 'match_3', 'match_4'])
    RoundTable().save_rounds([round_3, round_4])
    dsr = RoundTable().get_rounds()
    print(dsr)
