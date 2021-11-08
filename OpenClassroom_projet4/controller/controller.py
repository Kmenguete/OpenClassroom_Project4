from datetime import date

from OpenClassroom_projet4.View.view import View
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Tournament_model import DEFAULT_ROUNDS_NUMBER
from OpenClassroom_projet4.services.match_service import MatchService
from OpenClassroom_projet4.services.player_service import PlayerService
from OpenClassroom_projet4.services.tournament_service import TournamentService
from OpenClassroom_projet4.utils.config import Config


class MainController:

    def __init__(self):
        self.player_service = PlayerService()
        self.match_service = MatchService()
        self.tournament_service = TournamentService()

    def start(self):
        self.create_tournament()
        self.create_players()

    def create_tournament(self):
        name_choice, place_choice, description_choice = View.get_tournament_information()
        date_choice = date.today  # This is the date of today
        self.tournament_service.update_tournament(name=name_choice, place=place_choice, date=date_choice,
                                                  description=description_choice,
                                                  number_of_rounds=DEFAULT_ROUNDS_NUMBER)

    def create_players(self):
        player_list = []
        for index in range(Config.DEFAULT_PLAYERS_NUMBER):
            first_name, last_name = View.get_player_information()
            rank = index + 1
            player = Player(last_name, first_name, rank)
            player_list.append(player)
            View.display_text("\n *************** Player number {} created *****************".format(index))
        self.tournament_service.tournament.players = player_list

