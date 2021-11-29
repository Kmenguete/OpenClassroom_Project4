from OpenClassroom_projet4.database.tournament_table import TournamentTable
from OpenClassroom_projet4.errors.exceptions import TournamentDoesNotExistError
from OpenClassroom_projet4.view.view import View
from OpenClassroom_projet4.services.report_service import ReportService


class ReportsController:
    """ The Reports controller aim to manage the reports requested by the user.
        """

    def __init__(self):
        """ The init method import every modules required for the reports.
                """
        self.report_service = ReportService()
        self.tournament_table = TournamentTable()

    def request_report(self):
        """ The request_report method display the report menu.
                        """
        while True:
            View.display_report_menu()
            choice = View.get_report_choice()
            if choice == '1':
                self.manage_report_choice_1()
            elif choice == '2':
                self.manage_report_choice_2()
            elif choice == '3':
                self.manage_report_choice_3()
            elif choice == '4':
                self.manage_report_choice_4()
            elif choice == '5':
                self.manage_report_choice_5()
            elif choice == '6':
                self.manage_report_choice_6()
            elif choice == '7':
                self.manage_report_choice_7()
            else:
                View.display_text('Invalid value, enter one of the menu numbers')

    def another_report_suggestion(self):
        """ The another_report_suggestion is called when the user got the information requested from the report service.
        Concretely, this method ask the user whether he/she wants another report or not.
                                """
        while True:
            choice = View.get_choice("Do you want another report? Yes/No: ")
            if choice == 'Yes':
                self.request_report()
            elif choice == 'No':
                View.display_text("Thank you for your answer !!! Good bye !!!")
                exit()
            else:
                View.display_text("Invalid answer. You should answer the question by Yes or No")

    def manage_report_choice_1(self):
        """ If the user choose the question 1, the report service will display the list of every players of every
        tournaments sorted alphabetically.
                                        """
        while True:
            players = self.report_service.get_sorted_player_list_alphabetically()
            View.display_players(players)
            self.another_report_suggestion()

    def manage_report_choice_2(self):
        """ If the user choose the question 2, the report service will display the list of every players of every
                tournaments sorted by rank.
                                                """
        while True:
            players = self.report_service.get_sorted_player_list_by_rank()
            View.display_players(players)
            self.another_report_suggestion()

    def manage_report_choice_3(self):
        """ If the user choose the question 3, the report service will display the list of every tournaments.
                                                        """
        while True:
            tournaments = self.report_service.get_all_tournaments()
            View.display_tournaments(tournaments)
            self.another_report_suggestion()

    def manage_report_choice_4(self):
        """ If the user choose the question 4, the report service will display the list of every players for a
        specific tournament sorted alphabetically.
                                                                """
        while True:
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                players = self.report_service.get_tournament_players_in_alphabetical_order(tournament_id)
                View.display_players(players)
                self.another_report_suggestion()
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)

    def manage_report_choice_5(self):
        """ If the user choose the question 5, the report service will display the list of every players for a
                specific tournament sorted by rank.
                                                                        """
        while True:
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                players = self.report_service.get_tournament_players_sorted_by_rank(tournament_id)
                View.display_players(players)
                self.another_report_suggestion()
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)

    def manage_report_choice_6(self):
        """ If the user choose the question 6, the report service will display the list of every rounds for a specific
        tournament.
                                                                                """
        while True:
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                rounds = self.report_service.get_tournament_rounds(tournament_id)
                View.display_rounds(rounds)
                self.another_report_suggestion()
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)

    def manage_report_choice_7(self):
        """ If the user choose the question 7, the report service will display the list of every matches for a specific
                tournament.
                                                                                        """
        while True:
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                games = self.report_service.get_all_tournament_matches(tournament_id)
                View.display_all_games(games)
                self.another_report_suggestion()
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
