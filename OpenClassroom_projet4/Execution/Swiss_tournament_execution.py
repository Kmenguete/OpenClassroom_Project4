from tinydb import TinyDB, Query

from OpenClassroom_projet4.Execution.Swiss_tournament_system import sort_player_by_rank, split_total_number_of_players, \
    pairs_of_players, sort_players_by_score_round, generate_new_pairs_of_players

tournament_database = TinyDB('Tournament.json')
round_database = TinyDB('Round.json')
match_database = TinyDB('Match.json')
player_database = TinyDB('Player.json')
Player = Query()

player_1 = player_database.search(Player.surname == 'Menguete') + player_database.search(Player.firstname == 'Kevin') + \
           player_database.search(Player.rank == '1st')
player_2 = player_database.search(Player.surname == 'Sehili') + player_database.search(Player.firstname == 'Asma') + \
           player_database.search(Player.rank == '2nd')
player_3 = player_database.search(Player.surname == 'Mohamed Said Ali') + player_database.search(
    Player.firstname == 'Aymane') + \
           player_database.search(Player.rank == '3rd')
player_4 = player_database.search(Player.surname == 'Bourdon') + player_database.search(Player.firstname == 'Laurie'
                                                                                                            '-anne') \
           + \
           player_database.search(Player.rank == '4th')
player_5 = player_database.search(Player.surname == 'Robineau') + player_database.search(Player.firstname == 'Chloe') + \
           player_database.search(Player.rank == '5th')
player_6 = player_database.search(Player.surname == 'Boisvert') + player_database.search(Player.firstname == 'Guillaume') + \
           player_database.search(Player.rank == '6th')
player_7 = player_database.search(Player.surname == 'Ghazi') + player_database.search(Player.firstname == 'Imane') + \
           player_database.search(Player.rank == '7th')
player_8 = player_database.search(Player.surname == 'Dionne') + player_database.search(Player.firstname == 'Vanessa') + \
           player_database.search(Player.rank == '8th')

sort_player_by_rank(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)

split_total_number_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)

pairs_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)

sort_players_by_score_round(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)

generate_new_pairs_of_players(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)
