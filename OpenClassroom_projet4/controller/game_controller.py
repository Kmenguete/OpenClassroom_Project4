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
    """The Game controller aim to make sure that the tournament runs properly."""

    def __init__(self):
        """The init method import every required modules to save and update the tournament during its progress."""

        self.player_service = PlayerService()
        self.match_service = MatchService()
        self.tournament_service = TournamentService()

        self.round_id = str(uuid.uuid4())

    def run_game(self):
        """The run game method call every method that let to run, save and update the tournament."""
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
        """The create tournament method let the user create a tournament."""
        (
            name_choice,
            place_choice,
            date_choice,
            description_choice,
        ) = View.get_tournament_information()
        self.tournament_service.update_tournament(
            name=name_choice,
            place=place_choice,
            date=date_choice,
            description=description_choice,
            number_of_rounds=DEFAULT_ROUNDS_NUMBER,
        )
        # print("Tournament === " + str(self.tournament_service.tournament))

    def create_players(self):
        """The create players method let the user create players."""
        player_list = []
        for index in range(Config.DEFAULT_PLAYERS_NUMBER):
            first_name, last_name = View.get_player_information()
            rank = index + 1
            player = Player(last_name, first_name, rank)
            player_list.append(player)
            View.display_text(
                "\n *************** Player number {} created *****************".format(
                    index
                )
            )
        self.tournament_service.tournament.players = player_list
        self.player_service.player_list = player_list
        print("Tournament === " + str(self.tournament_service.tournament))
        # self.tournament_service.update_players(player_list)
        # self.player_service.update_player_list(player_list)

    def render_all_matches(self):
        """The render all matches method is called everywhere we need to display matches in order to know which
        players have to meet each other in a given round.
        """
        for match in self.match_service.match_list:
            View.display_match_information(match)

    def generate_first_round(self):
        """Once, the user have registered the 8 players, the application generate the first round with its matches."""
        # Step 3: Generate first round players pair
        self.player_service.player_list = self.tournament_service.tournament.players
        player_pairs = self.player_service.generate_initial_player_pair()
        sorted_player_list = self.player_service.sort_players_by_rank()

        # And now we create matches from player pairs
        self.match_service.create_matches_from_player_pairs(player_pairs)
        self.render_all_matches()

        # Step 3 part 2: create a round attach the match list and attach the round to the tournament
        self.tournament_service.create_first_round(
            self.match_service.match_list, self.round_id
        )
        self.tournament_service.tournament.players = sorted_player_list
        self.player_service.update_player_list(sorted_player_list)
        # self.tournament_service.update_players(sorted_player_list)
        self.tournament_service.tournament.players_dict = (
            transform_player_list_to_dictionary(
                self.tournament_service.tournament.players
            )
        )
        self.player_service.update_players_dict(
            self.tournament_service.tournament.players_dict
        )
        print("Tournament === " + str(self.tournament_service.tournament))

    def get_initial_round_results_and_update(self, round_name="Round 1"):
        """When a match is finished, the user enter the result. the user repeat the process for every match
        of the round 1. We voluntarily separated the round 1 from other rounds because the logic to which matches
        are generated in the first round is very different from the logic to which matches are generated on the
        other rounds.
        """
        View.display_text(
            "\n *************** Enter the results for {} **************".format(
                round_name
            )
        )
        self.get_round_results(self.tournament_service.tournament.rounds[0])

    def get_round_results(self, current_round):
        """
        This method let the user enter matches results for every round. Further, this method is called in the
        get_initial_round_results_and_update method in order to enter the results of the first round. This method
        is also called in the create_remaining_rounds method that deal with the other rounds of the tournament.
        """
        updated_match_list = []
        for match in current_round.matches:
            View.display_opponents(match.player_a, match.player_b)
            while True:
                winner = View.get_choice(
                    "Enter winner (A or B) If there is no winner then type None: "
                )
                if (
                    winner != Config.PLAYER_A_EXPECTED_INPUT
                    and winner != Config.PLAYER_B_EXPECTED_INPUT
                    and winner != Config.NO_WINNER_EXPECTED_INPUT
                ):
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
                    self.player_service.seek_player_and_update_score(
                        match.player_a, match.score_player_a
                    )
                    self.player_service.seek_player_and_update_score(
                        match.player_b, match.score_player_b
                    )
                    updated_match_list.append(match)
                    break
        print("Tournament === " + str(self.tournament_service.tournament))
        return updated_match_list

    def create_remaining_rounds(self):
        """
        This method let the user enter matches results for every round from round 2 to the last round. In this
        method, we especially call get_round_results method(as in the get_initial_round_results_and_update method).
        """
        for index in range(1, self.tournament_service.tournament.number_of_rounds):
            View.display_text(
                "\n *************** Enter the results for Round {} **************".format(
                    index + 1
                )
            )
            new_match_list = self.match_service.generate_matches_for_next_round(
                self.player_service.player_list, self.tournament_service
            )
            current_round = self.tournament_service.create_next_round(
                index + 1, new_match_list, self.round_id
            )
            self.get_round_results(current_round)
            self.player_service.sort_players_by_total_score()
            self.tournament_service.tournament.players = self.player_service.player_list
            View.display_players(self.player_service.players_dict)
