from OpenClassroom_projet4.services.player_service import PlayerService


class MainController:

    def __init__(self):
        self.player_service = PlayerService()
        self.match_service = None
        self.tournament_service = None
