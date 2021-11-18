from datetime import datetime

from tinydb import Query

from OpenClassroom_projet4.database.match_serializer import MatchSerializer
from OpenClassroom_projet4.database.player_serializer import PlayerSerializer
from OpenClassroom_projet4.database.round_serializer import RoundSerializer
from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
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
    now = datetime.now()
    player_3 = Player(last_name='Don', firstname='Kyrus', rank=8, player_id='46464646QSDFSD64', total_score=0)
    player_4 = Player(last_name='Al awal', firstname='Nawal', rank=1, player_id='1234RF5456GH46TFD', total_score=4)
    player_a = PlayerSerializer().serialize(player_3)
    player_b = PlayerSerializer().serialize(player_4)
    match_1 = Match(match_id='Q7STS76FS87G', player_a=player_a, score_player_a=0, player_b=player_b,
                    score_player_b=1)
    match_2 = Match(match_id='Q7STS76FS87G', player_a=player_a, score_player_a=0.5, player_b=player_b,
                    score_player_b=0.5)
    serialized_match_1 = MatchSerializer().serialize(match_1)
    serialized_match_2 = MatchSerializer().serialize(match_2)
    round_3 = Tour(round_id='EER7FT7ZF32874RG', round_name='Round_1', start_date=now,
                   matches=[serialized_match_1, serialized_match_2])
    round_4 = Tour(round_id='9854UT948T458T9', round_name='Round_2', start_date=now,
                   matches=[serialized_match_1, serialized_match_2])
    RoundTable().save_rounds([round_3, round_4])
    dsr = RoundTable().get_rounds()
    print(dsr)
