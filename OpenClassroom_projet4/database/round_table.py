from datetime import datetime
from tinydb import Query, TinyDB
from OpenClassroom_projet4.serializers.round_serializer import RoundSerializer
from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.utils.config import Config


class RoundTable:
    """ The round table stores rounds object of a tournament. To store a round, we need to store matches and to store
    matches, we need to store players. In fact, each table, depend each other to save properly, an entire tournament.
    """

    def __init__(self):
        self.database = TinyDB(Config.DATABASE_NAME)
        self.round_database = self.database.table(Config.ROUND_TABLE_NAME)
        self.round_serializer = RoundSerializer()

    def save_round(self, round):
        serialized_round = self.round_serializer.serialize(round)
        self.round_database.insert(serialized_round)

    def get_round(self, round_id):
        round_query = Query()
        serialized_round = self.round_database.search(round_query.round_id == round_id)
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
        for round in rounds:
            print(round)
        return rounds

    def update_round_name(self, name, round_id):
        round = Query()
        self.round_database.update({'round_name': name}, round.round_id == round_id)

    def clear_database(self):
        self.round_database.truncate()


if __name__ == '__main__':
    player_1 = Player(last_name='Darden', firstname='Mike', rank=5, player_id='46464646QSDFSD64', total_score=3)
    player_2 = Player(last_name='Mikaela', firstname='Arnold', rank=7, player_id='1234RF5456GH46TFD', total_score=1)

    match_1 = Match(match_id='Q7STS76FS87G', player_a=player_1, score_player_a=0, player_b=player_2,
                    score_player_b=1)
    match_2 = Match(match_id='Q7STS76FS87G', player_a=player_1, score_player_a=0.5, player_b=player_2,
                    score_player_b=0.5)

    round_3 = Tour(round_id='EER7FT7ZF32874RG', round_name='Round_1', start_date=datetime.now(),
                   matches=[match_1, match_2])
    # round_4 = Tour(round_id='9854UT948T458T9', round_name='Round_2', start_date='21/09/2021',
    # matches=['match_1', 'match_2', 'match_3', 'match_4'])
    RoundTable().save_rounds([round_3])
    dsr = RoundTable().get_rounds()
    print(dsr)
