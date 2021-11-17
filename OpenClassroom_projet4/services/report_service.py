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

    def select_one_tournament(self):
        self.tournament_table.get_tournaments()
        tournament_selection = input('Please select one tournament: ')
        if tournament_selection not in self.tournament_table.get_tournaments():
            print('The tournament you selected does not exist. Please, select a tournament that exist.')
        else:
            self.tournament_table.get_tournament(tournament_selection)

    def get_tournament_data(self, player_list, tournament):
        self.select_one_tournament()
        self.get_sorted_player_list_alphabetically(player_list)
        self.get_sorted_player_list_by_rank()
        self.get_rounds_of_one_tournament()
        self.get_matches_of_one_tournament(tournament)

    def suggest_report(self):
        report_suggestion = input('Do you want a report? Yes/No: ')
        if report_suggestion != 'Yes' and report_suggestion != 'No':
            print('Invalid value, you should answer the question by Yes or No.')
        else:
            if report_suggestion == 'No':
                print('Thank you for your answer. Good bye !!!')
                exit()
            else:
                multiple_choice_question = input('If you want the list of tournaments, type A. \n '
                                                 'If you want the list of players of one tournament, type B. \n '
                                                 'If you want the list of rounds of one tournament, type C. \n '
                                                 'If you want the list of matches of one tournament, type D.')
                if multiple_choice_question == 'A':
                    self.tournament_table.get_tournaments()
                elif multiple_choice_question == 'B':
                    self.player_table.get_players()
                elif multiple_choice_question == 'C':
                    self.round_table.get_rounds()
                elif multiple_choice_question == 'D':
                    self.match_table.get_matches()
                else:
                    print('Invalid value, you should answer the question by either A,B,C or D.')
