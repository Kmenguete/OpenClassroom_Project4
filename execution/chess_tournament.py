""" The main file is used to run the application. Without this file, it is not possible to run one application.
"""
from controller.main_controller import MainController

if __name__ == "__main__":
    MainController().start()
    exit()
