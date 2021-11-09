from OpenClassroom_projet4.controller.add_final_score_to_players import add_final_score_to_players
from OpenClassroom_projet4.controller.controller import MainController
from OpenClassroom_projet4.controller.display_players_and_their_final_scores import \
    display_players_and_their_final_scores
from OpenClassroom_projet4.controller.generate_matches_first_round import generate_matches_first_round
from OpenClassroom_projet4.controller.generate_matches_next_round import generate_matches_next_round
from OpenClassroom_projet4.controller.seek_player_and_update_score import seek_player_and_update_score
from OpenClassroom_projet4.controller.sort_player_by_final_score import sort_player_by_final_score
from OpenClassroom_projet4.controller.sort_players_by_rank import sort_players_by_rank
from OpenClassroom_projet4.controller.sort_players_by_total_score import sort_players_by_total_score
from OpenClassroom_projet4.controller.update_rank_of_players import update_rank_of_players
from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.model.Tournament_model import Tournament, DEFAULT_ROUNDS_NUMBER, create_list_dict
from datetime import date, datetime

DEFAULT_PLAYERS_NUMBER = 8

if __name__ == '__main__':
    MainController().start()
    exit()
    # Step 1: create a new tournament
    print("***************************** First create a tournament ************************* \n ")
    name = input("enter the name of tournament: ")
    place = input("enter the place of tournament: ")
    date = date.today()  # This is the date of today
    description = input("enter a description for this tournament: ")
    tournament = Tournament(name=name, place=place, date=date, description=description,
                            number_of_rounds=DEFAULT_ROUNDS_NUMBER)
    # End of step 1

    # Step 2: add players (the number of players is defined in the DEFAULT_PLAYERS_NUMBER constant variable)
    print("\n ********************************* We now need you to provide players ************************")
    player_list = []
    for index in range(DEFAULT_PLAYERS_NUMBER):
        first_name = input("Please enter the player's first name: ")
        last_name = input("Please enter the player's last name: ")
        rank = index + 1
        player = Player(last_name, first_name, rank)
        player_list.append(player)
        print("\n *************************** Player number {} entered *******************".format(index))
    tournament.players = player_list  # Here we assign or update the tournament players
    # End of step 2

    # Step 3: Generate first round players pair
    player_pairs = generate_matches_first_round(tournament.players)
    sorted_player_list = sort_players_by_rank(tournament.players)
    # And now we create matches from player pairs
    match_list = []
    for player_pair in player_pairs:
        match = Match(player_pair[0], player_pair[1])
        match_list.append(match)
        match.display_match()
    # Step 3 part 2: create a round attach the match list and attach the round to the tournament
    first_round = Tour("Round 1", datetime.now(), match_list)
    round_list = [first_round]
    tournament.rounds = round_list
    tournament.players = sorted_player_list
    tournament.players_dict = create_list_dict(tournament.players)

    # Step 4: Enter the result of the first round
    print("\n *************************** Now we need the result of the first round **********************")
    for match in tournament.rounds[0].matches:
        print("Player A: " + match.player_a.firstname + " " + match.player_a.last_name)
        print("Player B: " + match.player_b.firstname + " " + match.player_b.last_name)
        while True:
            winner = input("Enter winner (A or B) If there is no winner then type None: ")
            if winner != 'A' and winner != 'B' and winner != 'None':
                print("Invalid value")
            else:
                if winner == 'A':
                    match.score_player_a = 1
                    match.score_player_b = 0
                elif winner == 'B':
                    match.score_player_b = 1
                    match.score_player_a = 0
                elif winner == 'None':
                    match.score_player_b = 0.5
                    match.score_player_a = 0.5
                seek_player_and_update_score(match.player_a, match.player_b, match.score_player_a,
                                             match.score_player_b, tournament)
                break

    # Step 5: we sort players by their score.

    sort_players_by_total_score(tournament)

    for index in range(1, tournament.number_of_rounds):
        match_list = generate_matches_next_round(tournament.players, tournament)

        next_round = Tour("Round {}".format(index + 1), datetime.now(), match_list)
        tournament.rounds.append(next_round)
        for match in tournament.rounds[index].matches:
            print("Player A: " + match.player_a.firstname + " " + match.player_a.last_name)
            print("Player B: " + match.player_b.firstname + " " + match.player_b.last_name)
            while True:
                winner = input("Enter winner (A or B) If there is no winner then type None: ")
                if winner != 'A' and winner != 'B' and winner != 'None':
                    print("Invalid value")
                else:
                    if winner == 'A':
                        match.score_player_a = 1
                        match.score_player_b = 0
                    elif winner == 'B':
                        match.score_player_b = 1
                        match.score_player_a = 0
                    elif winner == 'None':
                        match.score_player_b = 0.5
                        match.score_player_a = 0.5
                    seek_player_and_update_score(match.player_a, match.player_b, match.score_player_a,
                                                 match.score_player_b, tournament)
                    break
        sort_players_by_total_score(tournament)

    add_final_score_to_players(tournament.players, tournament.players_dict)

    tournament.players = sort_player_by_final_score(tournament.players)
    display_players_and_their_final_scores(tournament.players)

    update_rank_of_players(tournament.players)

    print("The tournament is finished. At the end of the tournament, each player are sorted by their score and"
          " the rank is updated according the final total score of each player. \n If several players have the same "
          "total score then the former rank is promoted.")
    print(tournament.players)
