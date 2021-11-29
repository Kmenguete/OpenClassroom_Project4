from OpenClassroom_projet4.controller.game_controller import GameController
from OpenClassroom_projet4.controller.reports_controller import ReportsController
from OpenClassroom_projet4.view.view import View


class MainController:

    def __init__(self):
        self.game_controller = GameController()
        self.reports_controller = ReportsController()

    def start(self):
        while True:
            View.display_initial_menu()
            choice = View.get_choice("Choice: ")
            if choice == '1':
                self.game_controller.run_game()
            elif choice == '2':
                self.reports_controller.request_report()
            else:
                View.display_text("Invalid choice")
