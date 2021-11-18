import operator

from OpenClassroom_projet4.database.player_table import PlayerTable
from OpenClassroom_projet4.database.tournament_table import TournamentTable
from OpenClassroom_projet4.utils.utils import transform_player_list_to_dictionary


class PlayerService:

    def __init__(self, player_list=None):
        self.player_list = player_list
        self.players_dict = None
        self.player_table = PlayerTable()
        self.tournament_table = TournamentTable()

    def update_players_dict(self, players_dict):
        self.players_dict = players_dict
        self.tournament_table.update_players_dict(players_dict)

    def update_player_list(self, player_list):
        self.player_list = player_list
        self.player_table.update_players(player_list)

    def generate_initial_player_pair(self):
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        first_half = sorted_player_list[:len(sorted_player_list) // 2]
        second_half = sorted_player_list[len(sorted_player_list) // 2:]
        initial_player_pairs = list(list(x) for x in zip(first_half, second_half))
        print(tuple(initial_player_pairs))
        return initial_player_pairs

    def sort_players_by_rank(self):
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        return sorted_player_list

    def seek_player_and_update_score(self, player, new_score):
        if player.player_id in self.players_dict:
            self.players_dict[player.player_id].total_score += new_score
        else:
            self.players_dict[player.player_id].total_score = player.total_score + new_score

    def sort_players_by_total_score(self):
        sorted_list_by_total_score = sorted(self.players_dict.values(), key=operator.attrgetter("total_score"),
                                            reverse=True)
        self.players_dict = transform_player_list_to_dictionary(sorted_list_by_total_score)

    def update_rank_of_players(self):
        for index, player in enumerate(self.players_dict.values()):
            self.players_dict[player.player_id].rank = index + 1
