from tinydb import Query
import operator

from OpenClassroom_projet4.model.tinydb_backend import DATABASE


class ReportService:
    def __init__(self, player_list, round_list):
        self.player_list = player_list
        self.tournaments_list = None
        self.round_list = round_list
        self.database = DATABASE

    def get_sorted_player_list_alphabetically(self, player_list):
        players = Query()
        self.database.search(players.type == player_list)
        self.player_list = player_list.sort()
        print(player_list)
        return player_list

    def get_sorted_player_list_by_rank(self):
        players = Query()
        self.database.search(players.type == self.player_list)
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        print(sorted_player_list)
        return sorted_player_list

    def get_tournaments_list(self, tournaments_list):
        self.tournaments_list = tournaments_list
        print(tournaments_list)
        return tournaments_list

    def get_rounds_of_one_tournament(self):
        print(self.round_list)
        return self.round_list

    @staticmethod
    def get_matches_of_one_tournament(round_list, tournament):
        for round_index in range(0, len(round_list)):
            print(tournament.rounds[round_index].matches)

    def select_one_tournament(self, tournament_index):
        return self.tournaments_list[tournament_index]

    def get_tournament_data(self, tournament_index, player_list, round_list, tournament):
        self.select_one_tournament(tournament_index)
        self.get_sorted_player_list_alphabetically(player_list)
        self.get_sorted_player_list_by_rank()
        self.get_rounds_of_one_tournament()
        self.get_matches_of_one_tournament(round_list, tournament)

    def suggest_report(self, player_list, round_list, tournament):
        report_suggestion = input("Do you want a report? Yes/No: ")
        if report_suggestion != 'Yes' and report_suggestion != 'No':
            print("Invalid value, you should answer the question by Yes or No.")
        else:
            if report_suggestion == 'No':
                print("Thank you for your answer, good bye.")
                exit()
            elif report_suggestion == 'Yes':
                list_tournaments_suggestion = input("Do you want the list of tournaments? Yes/No: ")
                if list_tournaments_suggestion != 'Yes' and list_tournaments_suggestion != 'No':
                    print("Invalid value, you should answer the question by Yes or No.")
                else:
                    if list_tournaments_suggestion == 'Yes':
                        self.get_tournaments_list(self.tournaments_list)
                    elif list_tournaments_suggestion == 'No':
                        one_tournament_suggestion = input("Do you want to select a tournament? Yes/No: ")
                        if one_tournament_suggestion != 'Yes' and one_tournament_suggestion != 'No':
                            print("Invalid value, you should answer the question by Yes or No.")
                        else:
                            if one_tournament_suggestion == 'No':
                                print("Thank you for your answer, good bye.")
                                exit()
                            elif one_tournament_suggestion == 'Yes':
                                player_list_suggestion = input("Do you want the list of players? Yes/No: ")
                                if player_list_suggestion != 'Yes' and player_list_suggestion != 'No':
                                    print("Invalid value, you should answer the question by Yes or No.")
                                else:
                                    if player_list_suggestion == 'Yes':
                                        way_of_displaying_players = \
                                            input("Do you want players sorted alphabetically or by rank? "
                                                  "If you want players sorted alphabetically, type A, if "
                                                  "you want players "
                                                  "sorted by rank then, type B: ")
                                        if way_of_displaying_players != 'A' and way_of_displaying_players != 'B':
                                            print("Invalid value, you should answer the question by A or B.")
                                        else:
                                            if way_of_displaying_players == 'A':
                                                self.get_sorted_player_list_alphabetically(player_list)
                                            elif way_of_displaying_players == 'B':
                                                self.get_sorted_player_list_by_rank()
                                    elif player_list_suggestion == 'No':
                                        round_list_suggestion = input("Do you want the list of rounds? Yes/No: ")
                                        if round_list_suggestion != 'Yes' and round_list_suggestion != 'No':
                                            print("Invalid value, you should answer the question by Yes or No.")
                                        else:
                                            if round_list_suggestion == 'Yes':
                                                self.get_rounds_of_one_tournament()
                                            elif round_list_suggestion == 'No':
                                                match_list_suggestion = input(
                                                    "Do you want the list of every matches for the "
                                                    "tournament? Yes/No: ")
                                                if match_list_suggestion != 'Yes' and match_list_suggestion != 'No':
                                                    print("Invalid value, you should answer the question by Yes or No.")
                                                else:
                                                    if match_list_suggestion == 'Yes':
                                                        self.get_matches_of_one_tournament(round_list, tournament)
                                                    elif match_list_suggestion == 'No':
                                                        print("Thank you for your answer, good bye.")
                                                        exit()
