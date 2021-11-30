from datetime import datetime
from OpenClassroom_projet4.database.tournament_table import TournamentTable
from OpenClassroom_projet4.model.round_model import Tour
from OpenClassroom_projet4.model.tournament_model import Tournament


class TournamentService:
    """ The service package implement the business logic of the application. The tournament service is responsible to
    create rounds, and to make sure that two players never meet each other twice in a match during the tournament.
    the tournament service is also responsible to save the tournament when it is finished.
    """

    def __init__(self):
        """ The init method import the TournamentTable object(required to save each Tournament object created by the
        user) and give the attributes tournament to TournamentService object.
            """
        self.tournament_table = TournamentTable()
        self.tournament = None

    def update_tournament(self, name, place, date, description, number_of_rounds):
        """ The update_tournament method updates the tournament each time the user creates one.
                    """
        self.tournament = Tournament(name=name, place=place, date=date, description=description,
                                     number_of_rounds=number_of_rounds)

    def create_first_round(self, match_list, round_id):
        """ The create_first_round method creates the first round once the user created every players required to
        start the tournament.
                            """
        first_round = Tour(round_id, "Round 1", datetime.now(), match_list)
        round_list = [first_round]
        self.tournament.rounds = round_list

    def create_next_round(self, round_number, match_list, round_id):
        """ The create_next_round method creates the next rounds(from round 2 to the last round).
                                    """
        next_round = Tour(round_id, "Round {}".format(round_number), datetime.now(), match_list)
        self.tournament.rounds.append(next_round)
        return next_round

    def check_if_match_already_happened(self, player_a, player_b):
        already_happened = False
        for tour in self.tournament.rounds:
            for match in tour.matches:
                if (match.player_a == player_a and match.player_b == player_b) or (match.player_a == player_b and
                                                                                   match.player_b == player_a):
                    already_happened = True
        return already_happened

    def get_next_available_player(self, player_a, next_player_index, non_available_players):
        index = next_player_index
        while self.check_if_match_already_happened(player_a, self.tournament.players[index]) or \
                self.tournament.players[index] in non_available_players:
            index += 1
        player_b = self.tournament.players[index]
        return player_b

    def save(self):
        self.tournament_table.delete_and_save(self.tournament)
