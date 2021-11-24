from datetime import datetime
from tinydb import Query, TinyDB, where
from OpenClassroom_projet4.serializers.tournament_serializer import TournamentSerializer
from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.model.Tournament_model import Tournament
from OpenClassroom_projet4.utils.config import Config


class TournamentTable:

    def __init__(self):
        self.database = TinyDB('db.json')
        self.tournament_table = self.database.table(Config.TOURNAMENT_TABLE_NAME)
        self.tournament_serializer = TournamentSerializer()

    def save_tournament(self, tournament):
        serialized_tournament = self.tournament_serializer.serialize(tournament)
        self.tournament_table.insert(serialized_tournament)

    def get_tournament(self, tournament_id):
        tournament_query = Query()
        serialized_tournament = self.tournament_table.search(tournament_query.tournament_id == tournament_id)
        tournament = self.tournament_serializer.deserialize(serialized_tournament)
        print(tournament)
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
        for tournament in tournaments:
            print(tournament)
        return tournaments

    def delete_and_save(self, tournament):
        self.tournament_table.remove(where('tournament_id') == tournament.tournament_id)
        self.save_tournament(tournament)

    def update_name(self, tournament_id, name):
        tournament = Query()
        self.tournament_table.update({'name': name}, tournament.tournament_id == tournament_id)

    def get_rounds(self, tournament_id):
        tournament_query = Query()
        serialized_tournament = self.tournament_table.search(tournament_query.tournament_id == tournament_id)
        tournament = self.tournament_serializer.deserialize(serialized_tournament[0])
        return tournament.rounds

    def update_rounds(self, tournament_id, new_rounds):
        Tournament = Query()
        serialized_rounds = self.tournament_serializer.serialize_tournament_rounds(new_rounds)
        self.tournament_table.update({'rounds': serialized_rounds}, Tournament.tournament_id == tournament_id)

    def update_round_matches(self, tournament_id, round, match_list):
        Tournament = Query()
        serialized_tournament = self.tournament_table.search(Tournament.tournament_id == tournament_id)
        tournament = self.tournament_serializer.deserialize(serialized_tournament[0])
        tournament.rounds.remove(self._find_round(round.round_id, tournament.rounds))
        round.matches = match_list
        tournament.rounds.append(round)
        self.update_rounds(tournament_id, tournament.rounds)

    def get_players_of_one_tournament(self, tournament: Tournament):
        players_query = Query()
        serialized_players = self.tournament_table.search(players_query.players == tournament.players)
        return serialized_players

    @staticmethod
    def _find_round(round_id, rounds):
        for round in rounds:
            if round.round_id == round_id:
                return round

    def update_players(self, tournament_id, players):
        Tournament = Query()
        serialized_players, serialized_player_dict = self.tournament_serializer.serialize_tournament_players(players)
        self.tournament_table.update({'players': serialized_players, 'players_dict': serialized_player_dict},
                                     Tournament.tournament_id == tournament_id)


if __name__ == '__main__':

    player_1 = Player(last_name='Darden', firstname='Mike', rank=5, player_id='46464646QSDFSD64', total_score=3)
    player_2 = Player(last_name='Mikaela', firstname='Arnold', rank=7, player_id='1234RF5456GH46TFD', total_score=1)

    match_1 = Match(match_id='Q7STS76FS87G', player_a=player_1, score_player_a=0, player_b=player_2,
                    score_player_b=1)
    match_2 = Match(match_id='Q7STS76FS87G', player_a=player_1, score_player_a=0.5, player_b=player_2,
                    score_player_b=0.5)

    round_3 = Tour(round_id='EER7FT7ZF32874RG', round_name='Round_1', start_date=datetime.now(),
                   matches=[match_1, match_2])

    tournament_1 = Tournament(name='Tournament of Magdalena', place='Pointe-à-Pitre', date=datetime.now(),
                              description='Are you ready fo this tournament?', number_of_rounds=6,
                              tournament_id='SDFG34535GT35T', rounds=[round_3], players=[player_1, player_2])

    TournamentTable().save_tournaments([tournament_1])
    dst = TournamentTable().get_tournaments()
    print(dst)
