from OpenClassroom_projet4.Execution.Match_execution import Match
from OpenClassroom_projet4.Execution.Player_execution import Player
from OpenClassroom_projet4.Execution.Tournament_execution import Tournament
from OpenClassroom_projet4.Execution.swiss_tournament_version_2 import pairs_of_players

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
    number_players = int(input("Enter the number of players: "))
    player_list = []
    for player in range(number_players):
        if number_players == 1:
            print("There is not enough players to play a tournament.")
        else:
            surname = input("Enter the surname: ")
            firstname = input("Enter the firstname: ")
            birthdate = input("Enter the birthdate: ")
            sex = input("Enter the sex: ")
            rank = input("enter the rank of the player: ")
            player = Player(surname, firstname, birthdate, sex, rank)
            print("You have successfully created a player: " + str(player))
        player_list.append(player)
    pairs_of_players(player_list)


number_rounds = int(input("Enter the number of rounds: "))
round_list = []
for round in range(number_rounds):
    if number_rounds == 1:
        print("This tournament has only one round.")
        number_matches = int(input("Please enter the number of matches: "))
        match_list = []
        for match in range(number_matches):
            if number_matches == 1:
                print("This round has only one match.")
                round_number = input("enter the round number: ")
                match_number = input("enter the match number: ")
                player_a = input(
                    "enter the firstname and surname of player a: ")
                score_player_a = input("enter the score of player a: ")
                player_b = input(
                    "enter the firstname and surname of player b: ")
                score_player_b = input("enter the score of player b: ")
                match = Match(round_number, match_number, player_a, player_b,
                              score_player_a,
                              score_player_b)
                print("Here is the result of the match: " + str(match))
            else:
                print("This round has more than one match. Please enter the results of the other matches.")
                round_number = input("enter the round number: ")
                match_number = input("enter the match number: ")
                player_a = input(
                    "enter the firstname and surname of player a: ")
                score_player_a = input("enter the score of player a: ")
                player_b = input(
                    "enter the firstname and surname of player b: ")
                score_player_b = input("enter the score of player b: ")
                match = Match(round_number, match_number, player_a, player_b,
                              score_player_a,
                              score_player_b)
                print("Here is the result of the match: " + str(match))
            match_list.append(match)
    else:
        print("This tournament has more than one round.")
        number_matches = int(input("Please enter the number of matches: "))
        match_list = []
        for match in range(number_matches):
            if number_matches == 1:
                print("This round has only one match.")
                round_number = input("enter the round number: ")
                match_number = input("enter the match number: ")
                player_a = input(
                    "enter the firstname and surname of player a: ")
                score_player_a = input("enter the score of player a: ")
                player_b = input(
                    "enter the firstname and surname of player b: ")
                score_player_b = input("enter the score of player b: ")
                match = Match(round_number, match_number, player_a, player_b,
                              score_player_a,
                              score_player_b)
                print("Here is the result of the match: " + str(match))
            else:
                print("This round has more than one match. Please enter the results of the other matches.")
                round_number = input("enter the round number: ")
                match_number = input("enter the match number: ")
                player_a = input(
                    "enter the firstname and surname of player a: ")
                score_player_a = input("enter the score of player a: ")
                player_b = input(
                    "enter the firstname and surname of player b: ")
                score_player_b = input("enter the score of player b: ")
                match = Match(round_number, match_number, player_a, player_b,
                              score_player_a,
                              score_player_b)
                print("Here is the result of the match: " + str(match))
            match_list.append(match)
    round_list.append(round)
