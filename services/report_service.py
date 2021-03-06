import operator

from database.match_table import MatchTable
from database.player_table import PlayerTable
from database.round_table import RoundTable
from database.tournament_table import TournamentTable
from errors.exceptions import TournamentDoesNotExistError


class ReportService:
    """The service package implement the business logic of the application. The report service is responsible to
    generate a report when the user request it.
    """

    def __init__(self):
        """The init method import every required modules to generate reports."""
        self.player_table = PlayerTable()
        self.match_table = MatchTable()
        self.round_table = RoundTable()
        self.tournament_table = TournamentTable()

    def get_tournament(self, tournament_id):
        """The get_tournament method let the user select a specific tournament in the report menu."""
        tournament = self.tournament_table.get_tournament(tournament_id)
        if tournament is None:
            raise TournamentDoesNotExistError("This tournament id does not exist")
        return tournament

    def get_sorted_player_list_alphabetically(self):
        """The get_sorted_player_list_alphabetically method let the user get the list of all players from all
        tournament sorted alphabetically.
        """
        players = self.player_table.get_players()
        return self.__sort_alphabetically(players)

    def get_sorted_player_list_by_rank(self):
        """The get_sorted_player_list_by_rank method let the user get the list of all players from all
        tournament sorted by rank.
        """
        players = self.player_table.get_players()
        return self.__sort_by_rank(players)

    @staticmethod
    def __sort_alphabetically(players):
        """The __sort_alphabetically method is called to sort players alphabetically in
        get_sorted_player_list_alphabetically method.
        """
        sorted_player_list = [
            players[player_index].last_name + " " + players[player_index].firstname
            for player_index in range(0, len(players))
        ]
        return sorted(sorted_player_list)

    @staticmethod
    def __sort_by_rank(players):
        """The __sort_by_rank method is called to sort players alphabetically in
        get_sorted_player_list_by_rank method.
        """
        return sorted(players, key=operator.attrgetter("rank"))

    def get_tournament_players_in_alphabetical_order(self, tournament_id):
        """The get_tournament_players_in_alphabetical_order method let the user get the list of all players for a
        specific tournament sorted alphabetically.
        """
        tournament = self.get_tournament(tournament_id)
        return self.__sort_alphabetically(tournament.players)

    def get_tournament_players_sorted_by_rank(self, tournament_id):
        """The get_tournament_players_sorted_by_rank method let the user get the list of all players for a
        specific tournament sorted by rank.
        """
        tournament = self.get_tournament(tournament_id)
        return self.__sort_by_rank(tournament.players)

    def get_all_tournaments(self):
        """The get_all_tournaments method let the user get the list of all tournaments."""
        return self.tournament_table.get_tournaments()

    def get_tournament_rounds(self, tournament_id):
        """The get_tournament_rounds method let the user get the list of all rounds for a specific tournament."""
        tournament = self.get_tournament(tournament_id)
        return tournament.rounds

    def get_all_tournament_matches(self, tournament_id):
        """The get_all_tournament_matches method let the user get the list of all matches for a specific
        tournament. """
        tournament = self.get_tournament(tournament_id)
        match_list = []
        for round in tournament.rounds:
            match_list.extend(round.matches)
        return match_list

    @staticmethod
    def get_round_matches(round):
        """The get_round_matches method let the user get the list of all matches for a specific round."""
        return round.matches
