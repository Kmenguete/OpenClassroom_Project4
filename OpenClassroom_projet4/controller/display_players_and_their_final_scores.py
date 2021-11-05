

def display_players_and_their_final_scores(player_list):
    print("Here is the final score of each player at the end of the tournament: ")
    for player_index in range(0, len(player_list)):
        print(player_list[player_index].firstname + " " + player_list[player_index].last_name + ": " +
              str(player_list[player_index].total_score))
