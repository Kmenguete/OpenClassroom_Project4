import operator

from OpenClassroom_projet4.database.player_table import PlayerTable
from OpenClassroom_projet4.utils.utils import transform_player_list_to_dictionary, transform_player_dict_to_list


class PlayerService:

    def __init__(self, player_list=None):
        self.player_table = PlayerTable()
        self.player_list = player_list
        self.players_dict = None

    def update_players_dict(self, players_dict):
        self.players_dict = players_dict

    def update_player_list(self, player_list):
        self.player_list = player_list

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
        # self.player_table.update_player_total_score(player_id=player.player_id,
        # total_score=player.total_score + new_score)
        # self.refresh()
        if player.player_id in self.players_dict:
            self.players_dict[player.player_id].total_score += new_score
        else:
            self.players_dict[player.player_id].total_score = player.total_score + new_score
        self.player_list = transform_player_dict_to_list(self.players_dict)

    def sort_players_by_total_score(self):
        sorted_list_by_total_score = sorted(self.players_dict.values(), key=operator.attrgetter("total_score"),
                                            reverse=True)
        # self.update_player_list(sorted_list_by_total_score)
        # self.refresh()
        self.player_list = sorted_list_by_total_score
        self.players_dict = transform_player_list_to_dictionary(sorted_list_by_total_score)

    def update_rank_of_players(self):
        for index, player in enumerate(self.players_dict.values()):
            self.players_dict[player.player_id].rank = index + 1
        self.player_list = transform_player_dict_to_list(self.players_dict)

    def save(self):
        self.player_table.save_or_update(self.player_list)
