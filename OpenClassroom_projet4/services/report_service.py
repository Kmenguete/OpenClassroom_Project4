import pickle
import operator


class ReportService:
    def __init__(self):
        self.player_list = None
        self.round_list = None
        self.tournament = None

    def get_sorted_player_list_alphabetically(self, player_list):
        with open('players_database.pickle', 'rb') as file:
            pickle.load(file)
        self.player_list = player_list.sort()
        print(player_list)
        return player_list

    def get_sorted_player_list_by_rank(self):
        with open('players_database.pickle', 'rb') as file:
            pickle.load(file)
        sorted_player_list = sorted(self.player_list, key=operator.attrgetter("rank"))
        print(sorted_player_list)
        return sorted_player_list

    @staticmethod
    def get_tournaments_list():
        file = open('tournament_database.pickle', 'rb')
        output = pickle.load(file)
        print(output)
        return output

    def get_rounds_of_one_tournament(self):
        with open('rounds_database.pickle', 'rb') as file:
            pickle.load(file)
        print(self.round_list)
        return self.round_list

    def get_matches_of_one_tournament(self, tournament):
        with open('matches_database.pickle', 'rb') as file:
            pickle.load(file)
        for round_index in range(0, len(self.round_list)):
            print(tournament.rounds[round_index].matches)

    @staticmethod
    def select_one_tournament():
        with open('tournament_database.pickle', 'rb') as file:
            pickle.load(file)

    def get_tournament_data(self, player_list, tournament):
        self.select_one_tournament()
        self.get_sorted_player_list_alphabetically(player_list)
        self.get_sorted_player_list_by_rank()
        self.get_rounds_of_one_tournament()
        self.get_matches_of_one_tournament(tournament)

    def suggest_report(self, player_list, round_list):
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
                        self.get_tournaments_list()
                        exit()
                    elif list_tournaments_suggestion == 'No':
                        one_tournament_suggestion = input("Do you want to select a tournament? Yes/No: ")
                        if one_tournament_suggestion != 'Yes' and one_tournament_suggestion != 'No':
                            print("Invalid value, you should answer the question by Yes or No.")
                        else:
                            if one_tournament_suggestion == 'No':
                                print("Thank you for your answer, good bye.")
                                exit()
                            elif one_tournament_suggestion == 'Yes':
                                self.select_one_tournament()
                                tournament_selection = input("Please, select one tournament: ")
                                if tournament_selection != self.tournament:
                                    print("Invalid value, you should select a tournament that exist.")
                                else:
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
                                                        print(
                                                            "Invalid value, you should answer the "
                                                            "question by Yes or No.")
                                                    else:
                                                        if match_list_suggestion == 'Yes':
                                                            self.get_matches_of_one_tournament(round_list)
                                                        elif match_list_suggestion == 'No':
                                                            print("Thank you for your answer, good bye.")
                                                            exit()
