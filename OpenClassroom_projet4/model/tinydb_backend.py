from tinydb import TinyDB

from OpenClassroom_projet4.services.tournament_service import TournamentService

DATABASE = TinyDB('database.json')


class DataBase:

    def __init__(self, database=DATABASE):
        self.database = database
        self.tournament_service = TournamentService()

    def save_tournament_data(self):
        self.database.insert(self.tournament_service.tournament)
