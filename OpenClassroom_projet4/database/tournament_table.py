from tinydb import TinyDB, Query

from OpenClassroom_projet4.database.tournament_serializer import TournamentSerializer
from OpenClassroom_projet4.model.Tournament_model import Tournament


class TournamentTable:

    def __init__(self):
        self.tournament_database = TinyDB('tournament_database.json')
        self.tournament_serializer = TournamentSerializer()

    def save_tournament(self, tournament):
        serialized_tournament = self.tournament_serializer.serialize(tournament)
        self.tournament_database.insert(serialized_tournament)

    def get_tournament(self, tournament_id):
        tournament_query = Query()
        serialized_tournament = self.tournament_database.search(tournament_query.tournament_id == tournament_id)
        tournament = self.tournament_serializer.deserialize(serialized_tournament[0])
        return tournament

    def save_tournaments(self, tournaments: list):
        serialized_tournaments = []
        for tournament in tournaments:
            serialized_tournament = self.tournament_serializer.serialize(tournament)
            serialized_tournaments.append(serialized_tournament)
        self.tournament_database.insert_multiple(serialized_tournaments)

    def get_tournaments(self):
        serialized_tournaments = self.tournament_database.all()
        tournaments = []
        for serialized_tournament in serialized_tournaments:
            tournament = self.tournament_serializer.deserialize(serialized_tournament)
            tournaments.append(tournament)
        return tournaments

    def update_name(self, tournament_id, name):
        tournament = Query()
        self.tournament_database.update({'name': name}, tournament.tournament_id == tournament_id)


if __name__ == '__main__':
    tournament_1 = Tournament(name='Tournament of Magdalena', place='Pointe-à-Pitre', date='16/03/2018',
                              description='Are you ready fo this tournament?', number_of_rounds=6,
                              tournament_id='SDFG34535GT35T')
    tournament_2 = Tournament(name='Tournament of Malagasy', place='Nosy-be', date='07/10/2021',
                              description='Do not panic !!! This is just a test !!! relax !!!', number_of_rounds=5,
                              tournament_id='ZS78SF8ZS7ERFG4GF')
    TournamentTable().save_tournaments([tournament_1, tournament_2])
    dst = TournamentTable().get_tournaments()
    print(dst)
