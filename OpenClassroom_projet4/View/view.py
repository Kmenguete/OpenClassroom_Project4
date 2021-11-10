from datetime import date
# 1 - Display information
# 2 - Collect information
from OpenClassroom_projet4.services.report_service import ReportService


class View:

    def __init__(self, player_list, round_list, tournaments_list):
        self.report_service = ReportService(player_list, round_list)
        self.tournaments_list = tournaments_list

    @staticmethod
    def display_text(text_to_display):
        print(text_to_display)

    @staticmethod
    def get_choice(input_text):
        return input(input_text)

    @staticmethod
    def get_tournament_information():
        print("************** Welcome to Kevin's Chess tournament ************* \n ")
        name_choice = input("enter the name of tournament: ")
        place_choice = input("enter the place of tournament: ")
        date_choice = date.today()
        description_choice = input("enter a description for this tournament: ")
        print("\n ************** Tournament created ************* ")
        return name_choice, place_choice, date_choice, description_choice

    @staticmethod
    def get_player_information():
        print("\n ***************** Register a new player *****************")
        first_name_choice = input("Please enter the player's first name: ")
        last_name_choice = input("Please enter the player's last name: ")
        return first_name_choice, last_name_choice

    @staticmethod
    def display_match_information(match):
        return "Match: " + match.player_a.firstname + " " + match.player_a.last_name + " vs " + match.player_b.firstname + \
               " " + match.player_b.last_name

    @staticmethod
    def display_opponents(player_a, player_b):
        print("Player A: " + player_a.firstname + " " + player_a.last_name)
        print("Player B: " + player_b.firstname + " " + player_b.last_name)

    @staticmethod
    def display_players(players_dict):
        print(players_dict)

    def suggest_report(self):
        report_suggestion = input("Do you want a report? Yes/No: ")
        if report_suggestion != 'Yes' and report_suggestion != 'No':
            print("Invalid value, you should answer the question by Yes or No.")
        else:
            if report_suggestion == 'No':
                print("Thank you for your answer, good bye.")
            elif report_suggestion == 'Yes':
                list_tournaments_suggestion = input("Do you want the list of tournaments? Yes/No: ")
                if list_tournaments_suggestion != 'Yes' and list_tournaments_suggestion != 'No':
                    print("Invalid value, you should answer the question by Yes or No.")
                else:
                    if list_tournaments_suggestion == 'Yes':
                        print(self.report_service.get_tournaments_list(self.tournaments_list))
