import operator


class ReportService:
    def __init__(self):
        self.player_list = None
        self.round_list = None
        self.tournament = None

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

    def suggest_report(self, player_list, round_list):
        pass
