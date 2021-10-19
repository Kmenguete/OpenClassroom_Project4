from OpenClassroom_projet4.model.Match_model import Match
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.model.Round_model import Tour
from OpenClassroom_projet4.model.Tournament_model import Tournament, DEFAULT_ROUNDS_NUMBER
from datetime import date, datetime
import operator

DEFAULT_PLAYERS_NUMBER = 8

if __name__ == '__main__':
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
    winner_list = []
    loser_list = []
    new_player_list = []
    n = 0
    for h in range(0, len(tournament.rounds[0].matches)):
        if tournament.players[n] == tournament.rounds[0].matches[h].player_a and \
                tournament.rounds[0].matches[h].score_player_a == 1:
            winner_list.append(tournament.players[n])
        else:
            loser_list.append(tournament.players[n])
        n += 1

    for h in range(0, len(tournament.rounds[0].matches)):
        if tournament.players[n] == tournament.rounds[0].matches[h].player_b and \
                tournament.rounds[0].matches[h].score_player_b == 1:
            winner_list.append(tournament.players[n])
        else:
            loser_list.append(tournament.players[n])
        n += 1

    sorted_winner_list = sorted(winner_list, key=operator.attrgetter("rank"))
    sorted_loser_list = sorted(loser_list, key=operator.attrgetter("rank"))
    new_player_list = sorted_winner_list + sorted_loser_list
    print("Here the rank is updated according the score of each player.")
    tournament.players = new_player_list
    for i in range(0, len(tournament.players)):
        tournament.players[i].update_rank(tournament.players, i)

    print(tournament.players)
    next_winner_list = []
    next_loser_list = []
    next_player_list = []
    for f in range(1, tournament.number_of_rounds):
        non_available_players = []
        match_list = []
        for index in range(0, len(tournament.players)):
            player_a = tournament.players[index]
            if player_a in non_available_players:
                pass
            else:
                player_b = tournament.get_next_available_player(player_a, index + 1, non_available_players)
                non_available_players.append(player_a)
                non_available_players.append(player_b)
                print("creating match")
                match = Match(player_a, player_b)
                match_list.append(match)
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
        n = 0
        for h in range(0, len(tournament.rounds[f].matches)):
            if tournament.players[n] == tournament.rounds[f].matches[h].player_a and \
                    tournament.rounds[f].matches[h].score_player_a == 1:
                next_winner_list.append(tournament.players[n])
            else:
                next_loser_list.append(tournament.players[n])
            n += 1

        for h in range(0, len(tournament.rounds[f].matches)):
            if tournament.players[n] == tournament.rounds[f].matches[h].player_b and \
                    tournament.rounds[f].matches[h].score_player_b == 1:
                next_winner_list.append(tournament.players[n])
            else:
                next_loser_list.append(tournament.players[n])
            n += 1

        next_sorted_winner_list = sorted(next_winner_list, key=operator.attrgetter("rank"))
        next_sorted_loser_list = sorted(next_loser_list, key=operator.attrgetter("rank"))
        next_player_list = next_sorted_winner_list + next_sorted_loser_list
        print("Here the rank is updated according the score of each player.")
        tournament.players = next_player_list
        for i in range(0, len(tournament.players)):
            tournament.players[i].update_rank(tournament.players, i)

        print(tournament.players)
    else:
        print("The tournament is finished !!!")
