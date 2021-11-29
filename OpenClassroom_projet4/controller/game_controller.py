
from OpenClassroom_projet4.model.player_model import Player
from OpenClassroom_projet4.model.tournament_model import DEFAULT_ROUNDS_NUMBER
from OpenClassroom_projet4.services.match_service import MatchService
from OpenClassroom_projet4.services.player_service import PlayerService
from OpenClassroom_projet4.services.tournament_service import TournamentService
from OpenClassroom_projet4.utils.config import Config
import uuid

from OpenClassroom_projet4.utils.utils import transform_player_list_to_dictionary
from OpenClassroom_projet4.view.view import View


class GameController:
    """ The MainController class ensures a proper running of the tournament. To work, the MainController class uses
    different modules and packages. First of all, we ask the user to create a tournament. Once the tournament is
    created, we ask him/her to create players. When players are created, the application create automatically a first
    round. In our application, a round consist of a math list, a date, a round name and a round id. The first round
    is voluntarily separated from other rounds because the logic to which matches are generated in the firs round is
    very different from the logic to which matches are generated on other rounds. Once a first round is created with
    his matches, we then, ask the user to enter the result of each match. The result of the match is known only when
    a match(chess match) is finished. Once, the user entered results, every players are sorted by their total score.
    Next, the second round is generated and we ask the user to enter the result of matches. And then, we repeat the
    process until the end of the tournament. For each round, the user enter the results of matches, players are
    sorted by their total scores and the next round start. When the tournament is finished, the rank is updating
    according the total score of each players. When two players has the same total score then we promote the former
    rank of both players. And finally, when a tournament is finished, it is saved in a database named "db.json". At
    the end of the tournament, we suggest a report to the user. If the user does not want a report then the
    application stop running otherwise the user choose which information he/she wants from the database(list of
    tournaments, list of players of a tournament... .etc.). When the user have chosen which information he/she wants
    from the report, the application displays the information requested by the user and then stop running.
    """

    def __init__(self):
        self.player_service = PlayerService()
        self.match_service = MatchService()
        self.tournament_service = TournamentService()

        self.round_id = str(uuid.uuid4())

    def run_game(self):
        self.create_tournament()
        self.tournament_service.save()

        self.create_players()
        self.tournament_service.save()
        self.player_service.save()

        self.generate_first_round()
        self.get_initial_round_results_and_update()
        self.tournament_service.save()
        self.player_service.save()

        self.player_service.sort_players_by_total_score()
        self.tournament_service.tournament.players = self.player_service.player_list
        self.player_service.save()
        View.display_players(self.player_service.players_dict)

        self.create_remaining_rounds()
        self.tournament_service.save()
        self.player_service.save()

        self.player_service.update_rank_of_players()
        self.tournament_service.tournament.players = self.player_service.player_list
        self.tournament_service.save()
        View.display_players(self.player_service.players_dict)

    def create_tournament(self):
        name_choice, place_choice, date_choice, description_choice = View.get_tournament_information()
        self.tournament_service.update_tournament(name=name_choice, place=place_choice, date=date_choice,
                                                  description=description_choice,
                                                  number_of_rounds=DEFAULT_ROUNDS_NUMBER)
        # print("Tournament === " + str(self.tournament_service.tournament))

    def create_players(self):
        player_list = []
        for index in range(Config.DEFAULT_PLAYERS_NUMBER):
            first_name, last_name = View.get_player_information()
            rank = index + 1
            player = Player(last_name, first_name, rank)
            player_list.append(player)
            View.display_text("\n *************** Player number {} created *****************".format(index))
        self.tournament_service.tournament.players = player_list
        self.player_service.player_list = player_list
        print("Tournament === " + str(self.tournament_service.tournament))
        # self.tournament_service.update_players(player_list)
        # self.player_service.update_player_list(player_list)

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

        # Step 3 part 2: create a round attach the match list and attach the round to the tournament
        self.tournament_service.create_first_round(self.match_service.match_list, self.round_id)
        self.tournament_service.tournament.players = sorted_player_list
        self.player_service.update_player_list(sorted_player_list)
        # self.tournament_service.update_players(sorted_player_list)
        self.tournament_service.tournament.players_dict = \
            transform_player_list_to_dictionary(self.tournament_service.tournament.players)
        self.player_service.update_players_dict(self.tournament_service.tournament.players_dict)
        print("Tournament === " + str(self.tournament_service.tournament))

    def get_initial_round_results_and_update(self, round_name="Round 1"):
        View.display_text("\n *************** Enter the results for {} **************".format(round_name))
        self.get_round_results(self.tournament_service.tournament.rounds[0])
        # self.tournament_service.update_round_matches(self.tournament_service.tournament.rounds[0], updated_match_list)

    def get_round_results(self, current_round):
        """
        :param current_round: the round that should have its matches updated
        :return: the updated match list for the current round
        """
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
        print("Tournament === " + str(self.tournament_service.tournament))
        return updated_match_list

    def create_remaining_rounds(self):
        for index in range(1, self.tournament_service.tournament.number_of_rounds):
            View.display_text("\n *************** Enter the results for Round {} **************".format(index + 1))
            new_match_list = self.match_service.generate_matches_for_next_round(self.player_service.player_list,
                                                                                self.tournament_service)
            current_round = self.tournament_service.create_next_round(index + 1, new_match_list, self.round_id)
            self.get_round_results(current_round)
            self.player_service.sort_players_by_total_score()
            self.tournament_service.tournament.players = self.player_service.player_list
            View.display_players(self.player_service.players_dict)