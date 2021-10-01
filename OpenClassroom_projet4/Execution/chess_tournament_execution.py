from OpenClassroom_projet4.Execution.Match_execution import Match
from OpenClassroom_projet4.Execution.Player_execution import Player
from OpenClassroom_projet4.Execution.Round_execution import Round
from OpenClassroom_projet4.Execution.Swiss_tournament_system import pairs_of_players, sort_players_by_score_round
from OpenClassroom_projet4.Execution.Tournament_execution import Tournament
from OpenClassroom_projet4.Execution.score_player import ScorePlayer

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
    player_a = Player(surname, firstname, birthdate, sex)
    print("You have successfully created the player 1: " + str(player_a))
    if __name__ == '__main__':
        surname = input("Enter the surname: ")
        firstname = input("Enter the firstname: ")
        birthdate = input("Enter the birthdate: ")
        sex = input("Enter the sex: ")
        player_b = Player(surname, firstname, birthdate, sex)
        print("You have successfully created the player 2: " + str(player_b))
        if __name__ == '__main__':
            surname = input("Enter the surname: ")
            firstname = input("Enter the firstname: ")
            birthdate = input("Enter the birthdate: ")
            sex = input("Enter the sex: ")
            player_c = Player(surname, firstname, birthdate, sex)
            print("You have successfully created the player 3: " + str(player_c))
            if __name__ == '__main__':
                surname = input("Enter the surname: ")
                firstname = input("Enter the firstname: ")
                birthdate = input("Enter the birthdate: ")
                sex = input("Enter the sex: ")
                player_d = Player(surname, firstname, birthdate, sex)
                print("You have successfully created the player 4: " + str(player_d))
                if __name__ == '__main__':
                    surname = input("Enter the surname: ")
                    firstname = input("Enter the firstname: ")
                    birthdate = input("Enter the birthdate: ")
                    sex = input("Enter the sex: ")
                    player_e = Player(surname, firstname, birthdate, sex)
                    print("You have successfully created the player 5: " + str(player_e))
                    if __name__ == '__main__':
                        surname = input("Enter the surname: ")
                        firstname = input("Enter the firstname: ")
                        birthdate = input("Enter the birthdate: ")
                        sex = input("Enter the sex: ")
                        player_f = Player(surname, firstname, birthdate, sex)
                        print("You have successfully created the player 6: " + str(player_f))
                        if __name__ == '__main__':
                            surname = input("Enter the surname: ")
                            firstname = input("Enter the firstname: ")
                            birthdate = input("Enter the birthdate: ")
                            sex = input("Enter the sex: ")
                            player_g = Player(surname, firstname, birthdate, sex)
                            print("You have successfully created the player 7: " + str(player_g))
                            if __name__ == '__main__':
                                surname = input("Enter the surname: ")
                                firstname = input("Enter the firstname: ")
                                birthdate = input("Enter the birthdate: ")
                                sex = input("Enter the sex: ")
                                player_h = Player(surname, firstname, birthdate, sex)
                                print("You have successfully created the player 8: " + str(player_h))
                                player_1 = player_a.firstname + " " + player_a.surname
                                player_2 = player_b.firstname + " " + player_b.surname
                                player_3 = player_c.firstname + " " + player_c.surname
                                player_4 = player_d.firstname + " " + player_d.surname
                                player_5 = player_e.firstname + " " + player_e.surname
                                player_6 = player_f.firstname + " " + player_f.surname
                                player_7 = player_g.firstname + " " + player_g.surname
                                player_8 = player_h.firstname + " " + player_h.surname
                                pairs_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7,
                                                 player_8)
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
                                        match = Match(round_number, match_number, player_a, player_b, score_player_a,
                                                      score_player_b)
                                        print("Here is the result of the match: " + str(match))
                                        if __name__ == '__main__':
                                            round_number = input("enter the round number: ")
                                            match_number = input("enter the match number: ")
                                            player_a = input("enter the firstname and surname of player a: ")
                                            score_player_a = input("enter the score of player a: ")
                                            player_b = input("enter the firstname and surname of player b: ")
                                            score_player_b = input("enter the score of player b: ")
                                            match = Match(round_number, match_number, player_a, player_b,
                                                          score_player_a, score_player_b)
                                            print("Here is the result of the match: " + str(match))
                                            if __name__ == '__main__':
                                                round_number = input("enter the round number: ")
                                                match_number = input("enter the match number: ")
                                                player_a = input("enter the firstname and surname of player a: ")
                                                score_player_a = input("enter the score of player a: ")
                                                player_b = input("enter the firstname and surname of player b: ")
                                                score_player_b = input("enter the score of player b: ")
                                                match = Match(round_number, match_number, player_a, player_b,
                                                              score_player_a, score_player_b)
                                                print("Here is the result of the match: " + str(match))
                                                if __name__ == '__main__':
                                                    round_number = input("enter the round number: ")
                                                    match_number = input("enter the match number: ")
                                                    player_a = input("enter the firstname and surname of player a: ")
                                                    score_player_a = input("enter the score of player a: ")
                                                    player_b = input("enter the firstname and surname of player b: ")
                                                    score_player_b = input("enter the score of player b: ")
                                                    match = Match(round_number, match_number, player_a, player_b,
                                                                  score_player_a, score_player_b)
                                                    print("Here is the result of the match: " + str(match))
                                                    if __name__ == '__main__':
                                                        score_player_1 = input("Enter the score of player 1: ")
                                                        score_player_2 = input("Enter the score of player 2: ")
                                                        score_player_3 = input("Enter the score of player 3: ")
                                                        score_player_4 = input("Enter the score of player 4: ")
                                                        score_player_5 = input("Enter the score of player 5: ")
                                                        score_player_6 = input("Enter the score of player 6: ")
                                                        score_player_7 = input("Enter the score of player 7: ")
                                                        score_player_8 = input("Enter the score of player 8: ")
                                                        score_player = ScorePlayer(score_player_1, score_player_2,
                                                                                   score_player_3, score_player_4,
                                                                                   score_player_5,
                                                                                   score_player_6, score_player_7,
                                                                                   score_player_8)
                                                        print("Here is the score of each player at the end of the round"
                                                              )
                                                        sort_players_by_score_round(player_1, score_player_1, player_2,
                                                                                    score_player_2, player_3,
                                                                                    score_player_3, player_4,
                                                                                    score_player_4, player_5,
                                                                                    score_player_5, player_6,
                                                                                    score_player_6, player_7,
                                                                                    score_player_7, player_8,
                                                                                    score_player_8)
