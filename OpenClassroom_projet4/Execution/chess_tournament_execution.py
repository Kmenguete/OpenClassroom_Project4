from OpenClassroom_projet4.Execution.Player_execution import Player
from OpenClassroom_projet4.Execution.Tournament_execution import Tournament

if __name__ == '__main__':
    name_of_tournament = input("enter the name of tournament: ")
    place_of_tournament = input("enter the place of tournament: ")
    date_of_tournament = input("enter the date of tournament: ")
    duration_of_tournament = input("enter the duration of tournament: ")
    number_of_round = input("enter the number of round: ")
    number_of_match = input("enter the number of match for each round: ")
    description_of_tournament = input("enter a description for this tournament: ")
    tournament = Tournament(name_of_tournament, place_of_tournament, date_of_tournament, duration_of_tournament,
                            number_of_round, number_of_match, description_of_tournament)
    print("You have successfully created the following tournament: " + str(tournament))

if __name__ == '__main__':
    player_1 = input("Enter the player 1: ")
    player_2 = input("Enter the player 2: ")
    player_3 = input("Enter the player 3: ")
    player_4 = input("Enter the player 4: ")
    player_5 = input("Enter the player 5: ")
    player_6 = input("Enter the player 6: ")
    player_7 = input("Enter the player 7: ")
    player_8 = input("Enter the player 8: ")
    player = Player(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)
    print("Here is your 8 players: " + str(player))
