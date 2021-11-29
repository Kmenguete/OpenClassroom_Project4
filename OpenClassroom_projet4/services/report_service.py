import operator
from OpenClassroom_projet4.database.match_table import MatchTable
from OpenClassroom_projet4.database.player_table import PlayerTable
from OpenClassroom_projet4.database.round_table import RoundTable
from OpenClassroom_projet4.database.tournament_table import TournamentTable
from OpenClassroom_projet4.errors.exceptions import TournamentDoesNotExistError
from OpenClassroom_projet4.model.tournament_model import DEFAULT_ROUNDS_NUMBER


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

    def way_of_display_player_list(self):
        self.select_one_tournament()
        way_of_display_players = input('If you want players sorted by rank. type A: \n '
                                       'If you want players sorted alphabetically. type B: ')
        if way_of_display_players == 'A':
            self.get_sorted_player_list_by_rank()
        elif way_of_display_players == 'B':
            self.get_sorted_player_list_alphabetically()
        else:
            print('Invalid value, you should answer the question by A or B.')

    def get_rounds_of_one_tournament(self):
        tournament = self.select_one_tournament()
        print(tournament.rounds)

    def get_matches_of_one_tournament(self):
        tournament = self.select_one_tournament()
        for round_index in range(0, DEFAULT_ROUNDS_NUMBER):
            print(tournament.rounds[round_index].matches)

    def select_one_tournament(self):
        self.tournament_table.get_tournaments()
        tournament = self.tournament_table.get_tournament(tournament_id=input('Please select one '
                                                                              'tournament by their id: '))
        tournament_selection = tournament
        if tournament_selection != tournament:
            print('The tournament you selected does not exist. Please, select a tournament that exist.')
        else:
            self.tournament_table.get_tournament(tournament)
        return tournament

    def suggest_report(self):
        report_suggestion = input('Do you want a report? Yes/No: ')
        if report_suggestion != 'Yes' and report_suggestion != 'No':
            print('Invalid value, you should answer the question by Yes or No.')
        else:
            if report_suggestion == 'No':
                print('Thank you for your answer. Good bye !!!')
                exit()
            else:
                multiple_choice_question = input('If you want the list of tournaments, type A: \n '
                                                 'If you want the list of players of one tournament, type B: \n '
                                                 'If you want the list of rounds of one tournament, type C: \n '
                                                 'If you want the list of matches of one tournament, type D:')
                if multiple_choice_question == 'A':
                    self.tournament_table.get_tournaments()
                elif multiple_choice_question == 'B':
                    self.way_of_display_player_list()
                elif multiple_choice_question == 'C':
                    self.get_rounds_of_one_tournament()
                elif multiple_choice_question == 'D':
                    self.get_matches_of_one_tournament()
                else:
                    print('Invalid value, you should answer the question by either A,B,C or D.')
