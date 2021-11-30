from datetime import date
# 1 - Display information
# 2 - Collect information


class View:
    """ The View object is responsible to interact with the user and to collect data from the user and update them to
    the controller that will store this data in the database.
    """

    @staticmethod
    def display_initial_menu():
        """ The display_initial_menu method displays the main menu when the user start the application.
            """
        print("Select which action you wish to perform")
        print('1 -> Start a new tournament\n'
              '2 -> Generate reports\n '
              )

    @staticmethod
    def display_text(text_to_display):
        """ The display_text method displays every text the user need to see in the application.
                    """
        print(text_to_display)

    @staticmethod
    def get_choice(input_text):
        """ The get_choice method takes input text from the user.
                            """
        return input(input_text)

    @staticmethod
    def get_tournament_information():
        """ The get_tournament_information method takes information about the tournament.
                                    """
        print("************** Welcome to the Chess tournament ************* \n ")
        name_choice = input("enter the name of tournament: ")
        place_choice = input("enter the place of tournament: ")
        date_choice = date.today()
        description_choice = input("enter a description for this tournament: ")
        print("\n ************** Tournament created ************* ")
        return name_choice, place_choice, date_choice, description_choice

    @staticmethod
    def get_player_information():
        """ The get_player_information method takes information about the players.
                                            """
        print("\n ***************** Register a new player *****************")
        first_name_choice = input("Please enter the player's first name: ")
        last_name_choice = input("Please enter the player's last name: ")
        return first_name_choice, last_name_choice

    @staticmethod
    def display_match_information(match):
        """ The display_match_information method displays match information.
                                                    """
        return "Match: " + match.player_a.firstname + " " + match.player_a.last_name + " vs " + \
               match.player_b.firstname + " " + match.player_b.last_name

    @staticmethod
    def display_opponents(player_a, player_b):
        """ The display_opponents method displays players that meet each other in a match.
                                                            """
        print("Player A: " + player_a.firstname + " " + player_a.last_name)
        print("Player B: " + player_b.firstname + " " + player_b.last_name)

    @staticmethod
    def display_players(players_dict):
        """ The display_players method displays the players dictionary.
                                                                    """
        print(players_dict)

    @staticmethod
    def display_report_menu():
        """ The display_report_menu method displays the report menu.
                                                                            """
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
        """ The get_report_choice method takes input from the user in the report menu.
                                                                                    """
        return input("Choice: ")

    @staticmethod
    def display_tournaments(tournaments):
        """ The display_tournaments method displays the list of tournaments when the user requests it in the
        report menu.
                                                                                            """
        print(tournaments)

    @staticmethod
    def get_tournament_id():
        """ The get_tournament_id method asks the user to select a tournament by it id in the report menu.
                                                                                                    """
        return input("Enter the tournament ID: ")

    @staticmethod
    def display_invalid_tournament_id_message(tournament_id):
        """ The display_invalid_tournament_id_message method tells the user that he/she typed an invalid tournament id
        when he/she types an invalid tournament id in the report menu.
                                                                                                            """
        print("No tournament found with ID: {}".format(tournament_id))

    @staticmethod
    def display_rounds(rounds):
        """ The display_rounds method displays the list of all rounds for a specific tournament selected by the user
        in the report menu.
                                                                                                                """
        print(rounds)

    @staticmethod
    def display_all_games(games):
        """ The display_rounds method displays the list of all matches for a specific tournament selected by the user
                in the report menu.
                                                                                                                 """
        print(games)
