from tinydb import TinyDB, Query

from OpenClassroom_projet4.database.round_serializer import RoundSerializer
from OpenClassroom_projet4.model.Round_model import Tour


class RoundTable:

    def __init__(self):
        self.round_database = TinyDB('round_database.json')
        self.round_serializer = RoundSerializer()

    def save_round(self, round):
        serialized_round = self.round_serializer.serialize(round)
        self.round_database.insert(serialized_round)

    def get_round(self, round_name):
        round_query = Query()
        serialized_round = self.round_database.search(round_query.round_name == round_name)
        round = self.round_serializer.deserialize(serialized_round[0])
        return round

    def save_rounds(self, rounds: list):
        serialized_rounds = []
        for round in rounds:
            serialized_round = self.round_serializer.serialize(round)
            serialized_rounds.append(serialized_round)
        self.round_database.insert_multiple(serialized_rounds)

    def get_rounds(self):
        serialized_rounds = self.round_database.all()
        rounds = []
        for serialized_round in serialized_rounds:
            round = self.round_serializer.deserialize(serialized_round)
            rounds.append(round)
        return rounds
    
    def update_name(self, name):
        self.round_database.update({'round_name': name})


if __name__ == '__main__':
    round_1 = Tour(round_name='Round_1', start_date='14/03/2020', matches=['match_1', 'match_2', 'match_3', 'match_4'])
    round_2 = Tour(round_name='Round_2', start_date='21/09/2021', matches=['match_1', 'match_2', 'match_3', 'match_4'])
    RoundTable().save_rounds([round_1, round_2])
    dsr = RoundTable().get_rounds()
    print(dsr)
