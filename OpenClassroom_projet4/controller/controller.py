from OpenClassroom_projet4.View.view import View
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Tournament_model import DEFAULT_ROUNDS_NUMBER
from OpenClassroom_projet4.model.tinydb_backend import DataBase
from OpenClassroom_projet4.services.match_service import MatchService
from OpenClassroom_projet4.services.player_service import PlayerService
from OpenClassroom_projet4.services.report_service import ReportService
from OpenClassroom_projet4.services.tournament_service import TournamentService
from OpenClassroom_projet4.utils.config import Config
from OpenClassroom_projet4.utils.utils import transform_player_list_to_dictionary


class MainController:

    def __init__(self):
        self.player_service = PlayerService()
        self.match_service = MatchService()
        self.tournament_service = TournamentService()
        self.database = DataBase()
        self.report_service = ReportService(player_list=self.tournament_service.tournament.players,
                                            round_list=self.tournament_service.tournament.rounds,
                                            tournament=self.tournament_service.tournament)

    def start(self):
        self.create_tournament()
        self.create_players()
        self.generate_first_round()
        self.get_initial_round_results_and_update()
        self.player_service.sort_players_by_total_score()
        View.display_players(self.player_service.players_dict)
        self.create_remaining_rounds()
        self.player_service.update_rank_of_players()
        View.display_players(self.player_service.players_dict)

    def create_tournament(self):
        name_choice, place_choice, date_choice, description_choice = View.get_tournament_information()
        self.tournament_service.update_tournament(name=name_choice, place=place_choice, date=date_choice,
                                                  description=description_choice,
                                                  number_of_rounds=DEFAULT_ROUNDS_NUMBER)
        self.database.save_tournament_data()

    def create_players(self):
        player_list = []
        for index in range(Config.DEFAULT_PLAYERS_NUMBER):
            first_name, last_name = View.get_player_information()
            rank = index + 1
            player = Player(last_name, first_name, rank)
            player_list.append(player)
            View.display_text("\n *************** Player number {} created *****************".format(index))
        self.tournament_service.tournament.players = player_list
        self.database.save_players_data()

    def render_all_matches(self):
        for match in self.match_service.match_list:
            View.display_match_information(match)

    def generate_first_round(self):
        # Step 3: Generate first round players pair
        self.player_service.player_list = self.tournament_service.tournament.players
        player_pairs = self.player_service.generate_initial_player_pair()
        sorted_player_list = self.player_service.sort_players_by_rank()

        # And now we create matches from player pairs
        self.match_service.create_matches_from_player_pairs(player_pairs)
        self.render_all_matches()
        self.database.save_matches_data()

        # Step 3 part 2: create a round attach the match list and attach the round to the tournament
        self.tournament_service.create_first_round(self.match_service.match_list)
        self.tournament_service.tournament.players = sorted_player_list
        self.player_service.update_player_list(sorted_player_list)
        self.tournament_service.tournament.players_dict = \
            transform_player_list_to_dictionary(self.tournament_service.tournament.players)
        self.player_service.update_players_dict(self.tournament_service.tournament.players_dict)
        self.database.save_fist_rounds_data()

    def get_initial_round_results_and_update(self, round_name="Round 1"):
        View.display_text("\n *************** Enter the results for {} **************".format(round_name))
        self.get_round_results(self.tournament_service.tournament.rounds[0])

    def get_round_results(self, current_round):
        updated_match_list = []
        for match in current_round.matches:
            View.display_opponents(match.player_a, match.player_b)
            while True:
                winner = View.get_choice("Enter winner (A or B) If there is no winner then type None: ")
                if winner != Config.PLAYER_A_EXPECTED_INPUT \
                        and winner != Config.PLAYER_B_EXPECTED_INPUT \
                        and winner != Config.NO_WINNER_EXPECTED_INPUT:
                    View.display_text("Invalid value")
                else:
                    if winner == Config.PLAYER_A_EXPECTED_INPUT:
                        match.score_player_a = 1
                        match.score_player_b = 0
                    elif winner == Config.PLAYER_B_EXPECTED_INPUT:
                        match.score_player_b = 1
                        match.score_player_a = 0
                    elif winner == Config.NO_WINNER_EXPECTED_INPUT:
                        match.score_player_b = 0.5
                        match.score_player_a = 0.5
                    self.player_service.seek_player_and_update_score(match.player_a, match.score_player_a)
                    self.player_service.seek_player_and_update_score(match.player_b, match.score_player_b)
                    updated_match_list.append(match)
                    break
        return updated_match_list

    def create_remaining_rounds(self):
        for index in range(1, self.tournament_service.tournament.number_of_rounds):
            View.display_text("\n *************** Enter the results for Round {} **************".format(index + 1))
            new_match_list = self.match_service.generate_matches_for_next_round(self.player_service.player_list,
                                                                                self.tournament_service)
            current_round = self.tournament_service.create_next_round(index + 1, new_match_list)
            self.get_round_results(current_round)
            self.player_service.sort_players_by_total_score()
            View.display_players(self.player_service.players_dict)
            self.database.save_next_rounds_data(index, new_match_list)

    def request_report(self):
        self.report_service.suggest_report(self.tournament_service.tournament.players,
                                           self.tournament_service.tournament.rounds,
                                           self.tournament_service.tournament)
