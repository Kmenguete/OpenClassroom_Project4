import operator

from database.player_table import PlayerTable
from utils.utils import (
    transform_player_list_to_dictionary,
    transform_player_dict_to_list,
)


class PlayerService:
    """The service package implement the business logic of the application. The player service update the player
    list and the player dictionary(for example when the total score of a player change, retrieve the score of a
    player in a match or update the rank of players at the end of the tournament). The player service is responsible
    for the manipulation of players.
    """

    def __init__(self, player_list=None):
        """The init method import the Player Table object and gives attributes to Player Service object."""
        self.player_table = PlayerTable()
        self.player_list = player_list
        self.players_dict = None

    def update_players_dict(self, players_dict):
        """The update_players_dict method update the players' dictionary."""
        self.players_dict = players_dict

    def update_player_list(self, player_list):
        """The update_player_list method update the players list."""
        self.player_list = player_list

    def generate_initial_player_pair(self):
        """The generate_initial_player_pair generate player pairs for the first round. These player pairs represents
        matches of the first round.
        """
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        first_half = sorted_player_list[: len(sorted_player_list) // 2]
        second_half = sorted_player_list[len(sorted_player_list) // 2:]
        initial_player_pairs = list(list(x) for x in zip(first_half, second_half))
        print(tuple(initial_player_pairs))
        return initial_player_pairs

    def sort_players_by_rank(self):
        """The sort_players_by_rank method sort players by rank."""
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        return sorted_player_list

    def seek_player_and_update_score(self, player, new_score):
        """The seek_player_and_update_score add score of players for each match to their total score."""
        # self.player_table.update_player_total_score(player_id=player.player_id,
        # total_score=player.total_score + new_score)
        # self.refresh()
        if player.player_id in self.players_dict:
            self.players_dict[player.player_id].total_score += new_score
        else:
            self.players_dict[player.player_id].total_score = (
                player.total_score + new_score
            )
        self.player_list = transform_player_dict_to_list(self.players_dict)

    def sort_players_by_total_score(self):
        """The sort_players_by_total_score method sort players by their total score."""
        sorted_list_by_total_score = sorted(
            self.players_dict.values(),
            key=operator.attrgetter("total_score"),
            reverse=True,
        )
        # self.update_player_list(sorted_list_by_total_score)
        # self.refresh()
        self.player_list = sorted_list_by_total_score
        self.players_dict = transform_player_list_to_dictionary(
            sorted_list_by_total_score
        )

    def update_rank_of_players(self):
        """The update_rank_of_players method updates the rank of players at the end of the tournament."""
        for index, player in enumerate(self.players_dict.values()):
            self.players_dict[player.player_id].rank = index + 1
        self.player_list = transform_player_dict_to_list(self.players_dict)

    def save(self):
        """The save method saves the list of players in the database. This method will let the user get the list
        of all players from every tournament when he/she requests it to the report service.
        """
        self.player_table.save_or_update(self.player_list)
