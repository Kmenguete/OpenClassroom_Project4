import operator
from OpenClassroom_projet4.database.match_table import MatchTable
from OpenClassroom_projet4.database.player_table import PlayerTable
from OpenClassroom_projet4.database.round_table import RoundTable
from OpenClassroom_projet4.database.tournament_table import TournamentTable
from OpenClassroom_projet4.errors.exceptions import TournamentDoesNotExistError


class ReportService:
    """ The service package implement the business logic of the application. The report service is responsible to
    generate a report when the user request it.
    """

    def __init__(self):

        self.player_table = PlayerTable()
        self.match_table = MatchTable()
        self.round_table = RoundTable()
        self.tournament_table = TournamentTable()

    def get_tournament(self, tournament_id):
        tournament = self.tournament_table.get_tournament(tournament_id)
        if tournament is None:
            raise TournamentDoesNotExistError("This tournament id does not exist")
        return tournament

    def get_sorted_player_list_alphabetically(self):
        players = self.player_table.get_players()
        return self.__sort_alphabetically(players)

    def get_sorted_player_list_by_rank(self):
        players = self.player_table.get_players()
        return sorted(players, key=operator.attrgetter("rank"))

    @staticmethod
    def __sort_alphabetically(players):
        sorted_player_list = [players[player_index].last_name + " " + players[player_index].firstname
                              for player_index in range(0, len(players))]
        return sorted(sorted_player_list)

    @staticmethod
    def __sort_by_rank(players):
        return sorted(players, key=operator.attrgetter("rank"))

    def get_tournament_players_in_alphabetical_order(self, tournament_id):
        tournament = self.get_tournament(tournament_id)
        return self.__sort_alphabetically(tournament.players)

    def get_tournament_players_sorted_by_rank(self, tournament_id):
        tournament = self.get_tournament(tournament_id)
        return self.__sort_by_rank(tournament.players)

    def get_all_tournaments(self):
        return self.tournament_table.get_tournaments()

    def get_tournament_rounds(self, tournament_id):
        tournament = self.get_tournament(tournament_id)
        return tournament.rounds

    def get_all_tournament_matches(self, tournament_id):
        tournament = self.get_tournament(tournament_id)
        match_list = []
        for round in tournament.rounds:
            match_list.extend(round.matches)
        return match_list

    @staticmethod
    def get_round_matches(round):
        return round.matches
