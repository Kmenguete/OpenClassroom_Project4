from OpenClassroom_projet4.Execution.Match_execution import Match
from OpenClassroom_projet4.Execution.Player_execution import Player
from OpenClassroom_projet4.Execution.Round_execution import Round
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
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 1: " + str(player))

if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 2: " + str(player))

if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 3: " + str(player))

if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 4: " + str(player))

if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 5: " + str(player))

if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 6: " + str(player))

if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 7: " + str(player))

if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 8: " + str(player))

if __name__ == '__main__':
    name_of_tournament = input("enter the name of the tournament: ")
    round_number = input("enter the round number: ")
    match_list = input("enter the randomly generated matches: ")
    round = Round(name_of_tournament, round_number, match_list)
    print("Here are the matches for the current round: " + str(round))

if __name__ == '__main__':
    round_number = input("enter the round number: ")
    match_number = input("enter the match number: ")
    player_a = input("enter the firstname and surname of player a: ")
    score_player_a = input("enter the score of player a: ")
    player_b = input("enter the firstname and surname of player b: ")
    score_player_b = input("enter the score of player b: ")
    match = Match(round_number, match_number, player_a, player_b, score_player_a, score_player_b)
    print("Here is the result of the match: " + str(match))

if __name__ == '__main__':
    round_number = input("enter the round number: ")
    match_number = input("enter the match number: ")
    player_a = input("enter the firstname and surname of player a: ")
    score_player_a = input("enter the score of player a: ")
    player_b = input("enter the firstname and surname of player b: ")
    score_player_b = input("enter the score of player b: ")
    match = Match(round_number, match_number, player_a, player_b, score_player_a, score_player_b)
    print("Here is the result of the match: " + str(match))

if __name__ == '__main__':
    round_number = input("enter the round number: ")
    match_number = input("enter the match number: ")
    player_a = input("enter the firstname and surname of player a: ")
    score_player_a = input("enter the score of player a: ")
    player_b = input("enter the firstname and surname of player b: ")
    score_player_b = input("enter the score of player b: ")
    match = Match(round_number, match_number, player_a, player_b, score_player_a, score_player_b)
    print("Here is the result of the match: " + str(match))

if __name__ == '__main__':
    round_number = input("enter the round number: ")
    match_number = input("enter the match number: ")
    player_a = input("enter the firstname and surname of player a: ")
    score_player_a = input("enter the score of player a: ")
    player_b = input("enter the firstname and surname of player b: ")
    score_player_b = input("enter the score of player b: ")
    match = Match(round_number, match_number, player_a, player_b, score_player_a, score_player_b)
    print("Here is the result of the match: " + str(match))
