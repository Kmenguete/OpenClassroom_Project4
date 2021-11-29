from OpenClassroom_projet4.controller.game_controller import GameController
from OpenClassroom_projet4.controller.reports_controller import ReportsController
from OpenClassroom_projet4.view.view import View


class MainController:
    """ The Main controller ask the user whether he/she wants to play a tournament or request a report.
            """

    def __init__(self):
        """ The init method import the game controller and the reports controller. The game controller is used to play
        a tournament. The reports controller is used to request a report.
                    """
        self.game_controller = GameController()
        self.reports_controller = ReportsController()

    def start(self):
        """ The start method is the method that is called in the execution file of the application. When the application
        is executed, we ask the user whether he/she wants to play a tournament or to request a report. If the user
        choose 1, then a new tournament start. If he/she choose 2, the application will display the report menu.
                            """
        View.display_initial_menu()
        choice = View.get_choice("Choice: ")
        if choice == '1':
            self.game_controller.run_game()
        elif choice == '2':
            self.reports_controller.request_report()
        else:
            View.display_text("Invalid choice")
