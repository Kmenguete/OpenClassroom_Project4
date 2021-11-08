from OpenClassroom_projet4.services.match_service import MatchService
from OpenClassroom_projet4.services.player_service import PlayerService
from OpenClassroom_projet4.services.tournament_service import TournamentService


class MainController:

    def __init__(self):
        self.player_service = PlayerService()
        self.match_service = MatchService()
        self.tournament_service = TournamentService()
