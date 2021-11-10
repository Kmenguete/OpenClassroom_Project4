import operator


class ReportService:
    def __init__(self, player_list, tournaments_list, round_list):
        self.player_list = player_list
        self.tournaments_list = tournaments_list
        self.round_list = round_list

    def get_sorted_player_list_alphabetically(self, player_list):
        self.player_list = player_list.sort()

    def get_sorted_player_list_by_rank(self):
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        return sorted_player_list

    def get_tournaments_list(self, tournaments_list):
        self.tournaments_list = tournaments_list
        return tournaments_list

    def get_rounds_of_one_tournament(self):
        return self.round_list
    
    def get_matches_of_one_tournament(self):
        pass

    def select_one_tournament(self, tournament_index):
        return self.tournaments_list[tournament_index]
