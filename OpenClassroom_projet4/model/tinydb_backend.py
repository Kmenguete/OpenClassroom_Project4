from tinydb import TinyDB

from OpenClassroom_projet4.services.match_service import MatchService
from OpenClassroom_projet4.services.tournament_service import TournamentService

DATABASE = TinyDB('database.json')


class DataBase:

    def __init__(self, database=DATABASE):
        self.database = database
        self.tournament_service = TournamentService()
        self.match_service = MatchService()

    def save_tournament_data(self):
        self.database.insert(self.tournament_service.tournament)

    def save_players_data(self):
        self.database.insert(self.tournament_service.tournament.players)

    def save_matches_data(self):
        self.database.insert(self.match_service.match_list)

    def save_fist_rounds_data(self):
        self.database.insert(self.tournament_service.create_first_round(self.match_service.match_list))

    def save_next_rounds_data(self, index, new_match_list):
        self.database.insert(self.tournament_service.create_next_round(index + 1, new_match_list))
