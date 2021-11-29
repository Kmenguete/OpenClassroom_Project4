from datetime import date
# 1 - Display information
# 2 - Collect information


class View:
    """ The view file is responsible to interact with the user and to collect data from the user and update them to the
    controller that will store this data in the database.
    """

    @staticmethod
    def display_initial_menu():
        print("Select which action you wish to perform")
        print('1 -> Start a new tournament\n'
              '2 -> Generate reports\n '
              )

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
        return "Match: " + match.player_a.firstname + " " + match.player_a.last_name + " vs " + \
               match.player_b.firstname + " " + match.player_b.last_name

    @staticmethod
    def display_opponents(player_a, player_b):
        print("Player A: " + player_a.firstname + " " + player_a.last_name)
        print("Player B: " + player_b.firstname + " " + player_b.last_name)

    @staticmethod
    def display_players(players_dict):
        print(players_dict)

    @staticmethod
    def display_report_menu():
        print('1 -> All players sorted alphabetically\n'
              '2 -> All players sorted by rank\n'
              '3 -> All tournaments\n'
              '4 -> All players sorted alphabetically for a specific tournament:\n'
              '5 -> All players sorted by rank for a specific tournament:\n'
              '6 -> All the rounds in a specific tournament:\n'
              '7 -> All the games in a specific tournament:\n'
              )

    @staticmethod
    def get_report_choice():
        return input("Choice: ")

    @staticmethod
    def display_tournaments(tournaments):
        print(tournaments)

    @staticmethod
    def get_tournament_id():
        return input("Enter the tournament ID: ")

    @staticmethod
    def display_invalid_tournament_id_message(tournament_id):
        print("No tournament found with ID: {}".format(tournament_id))

    @staticmethod
    def display_rounds(rounds):
        print(rounds)

    @staticmethod
    def display_all_games(games):
        print(games)