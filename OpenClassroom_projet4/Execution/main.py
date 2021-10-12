from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.model.Tournament_model import Tournament
from datetime import date, datetime
import operator

DEFAULT_PLAYERS_NUMBER = 4

if __name__ == '__main__':
    # Step 1: create a new tournament
    print("***************************** First create a tournament ************************* \n ")
    name = input("enter the name of tournament: ")
    place = input("enter the place of tournament: ")
    date = date.today()  # This is the date of today
    description = input("enter a description for this tournament: ")
    tournament = Tournament(name=name, place=place, date=date, description=description)
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
    print("\n ****************************** We are generating the player pair... ****************************")
    sorted_player_list = sorted(tournament.players, key=operator.attrgetter("rank"))
    first_half = sorted_player_list[:len(sorted_player_list) // 2]
    second_half = sorted_player_list[len(sorted_player_list) // 2:]
    player_pairs = list(list(x) for x in zip(first_half, second_half))
    print(tuple(player_pairs))
    # And now we create matches from player pairs
    match_list = []
    for player_pair in player_pairs:
        print("creating match")
        match = Match(player_pair[0], player_pair[1])
        match_list.append(match)
    # Step 3 part 2: create a round attach the match list and attach the round to the tournament
    first_round = Tour("Round 1", datetime.now(), match_list)
    round_list = [first_round]
    tournament.rounds = round_list
    # End of step 3

    # Step 4: Enter the result of the first round
    print("\n *************************** Now we need the result of the first round **********************")
    for match in tournament.rounds[0].matches:
        print("Player A: " + match.player_a.last_name)
        print("Player B: " + match.player_b.last_name)
        while True:
            winner = input("Enter winner (A or B): ")
            if winner != 'A' and winner != 'B':
                print("Invalid value for player, please enter either A or B")
            else:
                if winner == 'A':
                    match.score_player_a = 1
                    match.score_player_b = 0
                elif winner == 'B':
                    match.score_player_b = 1
                    match.score_player_a = 0
                break
    # End of step 4

    for round in tournament.rounds:
        # Step 5: we generate new pairs of player for the next round and we play matches for the next round
        # for the next round player 1 meet player 2 and player 3 meet player 4 and so on.
        # If the player 1 have already met the player 2 then he meet the player 3. If the player 3 have already
        # met the player 4 then he meet the player 5 and so on.
        match_list = []
        odd_players = []
        even_players = []
        for player in range(0, len(tournament.players)):
            if player % 2 == 0:
                even_players.append(tournament.players[player])
            else:
                odd_players.append(tournament.players[player])
                new_player_pairs = list(list(x) for x in zip(odd_players, even_players))
                print(tuple(new_player_pairs))
                    
                for new_player_pair in new_player_pairs:
                    print("creating match")
                    match = Match(new_player_pair[0], new_player_pair[1])
                    match_list.append(match)
                    i = 0
                    if new_player_pair in tournament.rounds[i].matches:
                        print("A match with these players already exist. Please, promote the following match: ")
                        alternative_matches = [(player, (player + 1) % len(odd_players))
                                               for player in range(len(odd_players))]
                        alternative_matches_2 = [(player, (player + 1) % len(even_players))
                                                 for player in range(len(even_players))]
                        for match in alternative_matches:
                            print(match)
                        for match in alternative_matches_2:
                            print(match)
                        for alternative_match in alternative_matches:
                            print("creating match")
                            match = Match(alternative_match[0], alternative_match[1])
                            match_list.append(match)
                        for alternative_match_2 in alternative_matches_2:
                            print("creating match")
                            match = Match(alternative_match_2[0], alternative_match_2[1])
                            match_list.append(match)
                    else:
                        print("No previous match found with these players")
                        i += 1
        i = 1
        next_round = Tour("Round {}".format(i), datetime.now(), match_list)
        round_list = [first_round, next_round]
        tournament.rounds = round_list
        for match in tournament.rounds[i].matches:
            print("Player A: " + match.player_a.last_name)
            print("Player B: " + match.player_b.last_name)
            while True:
                winner = input("Enter winner (A or B): ")
                if winner != 'A' and winner != 'B':
                    print("Invalid value for player, please enter either A or B")
                else:
                    if winner == 'A':
                        match.score_player_a = 1
                        match.score_player_b = 0
                    elif winner == 'B':
                        match.score_player_b = 1
                        match.score_player_a = 0
                    break
            i += 1
