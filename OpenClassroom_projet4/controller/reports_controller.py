from OpenClassroom_projet4.errors.exceptions import TournamentDoesNotExistError
from OpenClassroom_projet4.view.view import View
from OpenClassroom_projet4.services.report_service import ReportService


class ReportsController:

    def __init__(self):
        self.report_service = ReportService()

    def request_report(self):
        View.display_report_menu()
        choice = View.get_report_choice()
        if choice == '1':
            players = self.report_service.get_sorted_player_list_alphabetically()
            View.display_players(players)
        elif choice == '2':
            players = self.report_service.get_sorted_player_list_by_rank()
            View.display_players(players)
        elif choice == '3':
            tournaments = self.report_service.get_all_tournaments()
            View.display_tournaments(tournaments)
        elif choice == '4':
            tournament_id = View.get_tournament_id()
            try:
                players = self.report_service.get_tournament_players_in_alphabetical_order(tournament_id)
                View.display_players(players)
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
        elif choice == '5':
            self.manage_report_choice_5()
        elif choice == '6':
            tournament_id = View.get_tournament_id()
            try:
                rounds = self.report_service.get_tournament_rounds(tournament_id)
                View.display_rounds(rounds)
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
        elif choice == '7':
            tournament_id = View.get_tournament_id()
            try:
                games = self.report_service.get_all_tournament_matches(tournament_id)
                View.display_all_games(games)
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)
        else:
            View.display_text('Invalid value, enter one of the menu numbers')

    def manage_report_choice_5(self):
        while True:
            tournament_id = View.get_tournament_id()
            try:
                players = self.report_service.get_tournament_players_sorted_by_rank(tournament_id)
                View.display_players(players)
                break
            except TournamentDoesNotExistError:
                View.display_invalid_tournament_id_message(tournament_id)