import operator

from OpenClassroom_projet4.database.match_table import MatchTable
from OpenClassroom_projet4.database.player_table import PlayerTable
from OpenClassroom_projet4.database.round_table import RoundTable
from OpenClassroom_projet4.database.tournament_table import TournamentTable


class ReportService:
    def __init__(self):
        self.player_list = None
        self.player_table = PlayerTable()
        self.match_table = MatchTable()
        self.round_table = RoundTable()
        self.tournament_table = TournamentTable()

    def get_sorted_player_list_alphabetically(self, player_list):
        self.player_list = player_list.sort()
        print(player_list)
        return player_list

    def get_sorted_player_list_by_rank(self):
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        print(sorted_player_list)
        return sorted_player_list

    @staticmethod
    def get_tournaments_list():
        pass

    def get_rounds_of_one_tournament(self):
        pass

    def get_matches_of_one_tournament(self, tournament):
        pass

    @staticmethod
    def select_one_tournament():
        pass

    def get_tournament_data(self, player_list, tournament):
        self.select_one_tournament()
        self.get_sorted_player_list_alphabetically(player_list)
        self.get_sorted_player_list_by_rank()
        self.get_rounds_of_one_tournament()
        self.get_matches_of_one_tournament(tournament)

    def suggest_report(self):
        pass
