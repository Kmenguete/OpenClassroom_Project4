from datetime import datetime

from OpenClassroom_projet4.database.round_table import RoundTable
from OpenClassroom_projet4.database.tournament_table import TournamentTable
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.model.Tournament_model import Tournament


class TournamentService:

    def __init__(self):
        self.tournament = None
        self.tournament_table = TournamentTable()
        self.round_table = RoundTable()

    def update_tournament(self, name, place, date, description, number_of_rounds):
        self.tournament = Tournament(name=name, place=place, date=date, description=description,
                                     number_of_rounds=number_of_rounds)
        self.tournament_table.update_tournament(self.tournament)

    def create_first_round(self, match_list, round_id):
        first_round = Tour(round_id, "Round 1", datetime.now(), match_list)
        round_list = [first_round]
        self.tournament.rounds = round_list
        self.round_table.update_round(first_round)
        self.round_table.update_rounds(self.tournament.rounds)

    def create_next_round(self, round_number, match_list, round_id):
        next_round = Tour(round_id, "Round {}".format(round_number), datetime.now(), match_list)
        self.tournament.rounds.append(next_round)
        self.round_table.update_round(next_round)
        self.round_table.update_rounds(self.tournament.rounds)
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
