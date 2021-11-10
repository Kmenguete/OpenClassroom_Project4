import operator


class ReportService:
    def __init__(self, player_list, tournaments_list):
        self.player_list = player_list
        self.tournaments_list = tournaments_list

    def get_sorted_player_list_alphabetically(self, player_list):
        self.player_list = player_list.sort()

    def get_sorted_player_list_by_rank(self):
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        return sorted_player_list

    def get_tournaments_list(self, tournaments_list):
        self.tournaments_list = tournaments_list

    def get_rounds_of_tournament(self):
        pass
    
    def get_matches_of_tournament(self):
        pass
