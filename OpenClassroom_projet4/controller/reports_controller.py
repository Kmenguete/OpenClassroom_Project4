from OpenClassroom_projet4.database.tournament_table import TournamentTable
from OpenClassroom_projet4.errors.exceptions import TournamentDoesNotExistError
from OpenClassroom_projet4.view.view import View
from OpenClassroom_projet4.services.report_service import ReportService


class ReportsController:

    def __init__(self):
        self.report_service = ReportService()
        self.tournament_table = TournamentTable()

    def request_report(self):
        View.display_report_menu()
        choice = View.get_report_choice()
        if choice == '1':
            players = self.report_service.get_sorted_player_list_alphabetically()
            View.display_players(players)
            self.another_report_suggestion()
        elif choice == '2':
            players = self.report_service.get_sorted_player_list_by_rank()
            View.display_players(players)
            self.another_report_suggestion()
        elif choice == '3':
            tournaments = self.report_service.get_all_tournaments()
            View.display_tournaments(tournaments)
            self.another_report_suggestion()
        elif choice == '4':
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                players = self.report_service.get_tournament_players_in_alphabetical_order(tournament_id)
                View.display_players(players)
                self.another_report_suggestion()
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
        elif choice == '5':
            self.manage_report_choice_5()
            self.another_report_suggestion()
        elif choice == '6':
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                rounds = self.report_service.get_tournament_rounds(tournament_id)
                View.display_rounds(rounds)
                self.another_report_suggestion()
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
        elif choice == '7':
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                games = self.report_service.get_all_tournament_matches(tournament_id)
                View.display_all_games(games)
                self.another_report_suggestion()
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
        else:
            View.display_text('Invalid value, enter one of the menu numbers')

    def another_report_suggestion(self):
        while True:
            choice = View.get_choice("Do you want another report? Yes/No: ")
            if choice == 'Yes':
                self.request_report()
            elif choice == 'No':
                View.display_text("Thank you for your answer !!! Good bye !!!")
                exit()
            else:
                View.display_text("Invalid answer. You should answer the question by Yes or No")

    def manage_report_choice_5(self):
        while True:
            self.tournament_table.display_tournaments()
            tournament_id = View.get_tournament_id()
            try:
                players = self.report_service.get_tournament_players_sorted_by_rank(tournament_id)
                View.display_players(players)
                break
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
