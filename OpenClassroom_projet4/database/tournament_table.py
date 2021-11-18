from datetime import datetime

from tinydb import Query

from OpenClassroom_projet4.database.match_serializer import MatchSerializer
from OpenClassroom_projet4.database.player_serializer import PlayerSerializer
from OpenClassroom_projet4.database.round_serializer import RoundSerializer
from OpenClassroom_projet4.database.tournament_serializer import TournamentSerializer
from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.model.Tournament_model import Tournament
from OpenClassroom_projet4.utils.config import Config


class TournamentTable:

    def __init__(self):
        self.database = Config.DATABASE
        self.tournament_serializer = TournamentSerializer()
        self.tournament_table = self.database.table('Tournament_table')

    def save_tournament(self, tournament):
        serialized_tournament = self.tournament_serializer.serialize(tournament)
        self.tournament_table.insert(serialized_tournament)

    def get_tournament(self, tournament_id):
        tournament_query = Query()
        serialized_tournament = self.tournament_table.search(tournament_query.tournament_id == tournament_id)
        tournament = self.tournament_serializer.deserialize(serialized_tournament[0])
        return tournament

    def save_tournaments(self, tournaments: list):
        serialized_tournaments = []
        for tournament in tournaments:
            serialized_tournament = self.tournament_serializer.serialize(tournament)
            serialized_tournaments.append(serialized_tournament)
        self.tournament_table.insert_multiple(serialized_tournaments)

    def get_tournaments(self):
        serialized_tournaments = self.tournament_table.all()
        tournaments = []
        for serialized_tournament in serialized_tournaments:
            tournament = self.tournament_serializer.deserialize(serialized_tournament)
            tournaments.append(tournament)
        return tournaments

    def update_name(self, tournament_id, name):
        tournament = Query()
        self.tournament_table.update({'name': name}, tournament.tournament_id == tournament_id)

    def update_tournament(self, tournament):
        self.tournament_table.update(tournament)

    def clear_tournament_table(self):
        self.tournament_table.truncate()

    def clear_database(self):
        self.database.truncate()


if __name__ == '__main__':
    now = datetime.now()
    player_3 = Player(last_name='Don', firstname='Kyrus', rank=8, player_id='46464646QSDFSD64', total_score=0)
    player_4 = Player(last_name='Al awal', firstname='Nawal', rank=1, player_id='1234RF5456GH46TFD', total_score=4)
    serialized_player_3 = PlayerSerializer().serialize(player_3)
    serialized_player_4 = PlayerSerializer().serialize(player_4)
    match_1 = Match(match_id='Q7STS76FS87G', player_a=serialized_player_3, score_player_a=0,
                    player_b=serialized_player_4, score_player_b=1)
    match_2 = Match(match_id='Q7STS76FS87G', player_a=serialized_player_3, score_player_a=0.5,
                    player_b=serialized_player_4, score_player_b=0.5)
    serialized_match_1 = MatchSerializer().serialize(match_1)
    serialized_match_2 = MatchSerializer().serialize(match_2)
    round_3 = Tour(round_id='EER7FT7ZF32874RG', round_name='Round_1', start_date=now,
                   matches=[serialized_match_1, serialized_match_2])
    round_4 = Tour(round_id='9854UT948T458T9', round_name='Round_2', start_date=now,
                   matches=[serialized_match_1, serialized_match_2])
    serialized_round_3 = RoundSerializer().serialize(round_3)
    serialized_round_4 = RoundSerializer().serialize(round_4)
    tournament_1 = Tournament(name='Tournament of Magdalena', place='Pointe-à-Pitre', date=now,
                              description='Are you ready fo this tournament?', number_of_rounds=6,
                              tournament_id='SDFG34535GT35T', rounds=[serialized_round_3, serialized_round_4],
                              players=[serialized_player_3, serialized_player_4],
                              players_dict={player_3.player_id: serialized_player_3,
                                            player_4.player_id: serialized_player_4})
    tournament_2 = Tournament(name='Tournament of Malagasy', place='Nosy-be', date=now,
                              description='Do not panic !!! This is just a test !!! relax !!!', number_of_rounds=5,
                              tournament_id='ZS78SF8ZS7ERFG4GF', rounds=[serialized_round_3, serialized_round_4],
                              players=[serialized_player_3, serialized_player_4],
                              players_dict={player_3.player_id: serialized_player_3,
                                            player_4.player_id: serialized_player_4})
    TournamentTable().save_tournaments([tournament_1, tournament_2])
    dst = TournamentTable().get_tournaments()
    print(dst)
