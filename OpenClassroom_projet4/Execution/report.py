from tinydb import TinyDB, Query

tournament_database = TinyDB('Tournament.json')
round_database = TinyDB('Round.json')
match_database = TinyDB('Match.json')
player_database = TinyDB('Player.json')
Player = Query()


def sort_player_by_alphabetical_order():
    player_1 = player_database.search(Player.surname == 'Boisvert') + player_database.search(Player.firstname == 'Guillaume')
    player_2 = player_database.search(Player.surname == 'Bourdon') + player_database.search(Player.firstname == 'Laurie-anne')
    player_3 = player_database.search(Player.surname == 'Dionne') + player_database.search(Player.firstname == 'Vanessa')
    player_4 = player_database.search(Player.surname == 'Ghazi') + player_database.search(Player.firstname == 'Imane')
    player_5 = player_database.search(Player.surname == 'Menguete') + player_database.search(Player.firstname == 'Kevin')
    player_6 = player_database.search(Player.surname == 'Mohamed Said Ali') + player_database.search(Player.firstname == 'Aymane')
    player_7 = player_database.search(Player.surname == 'Robineau') + player_database.search(Player.firstname == 'Chloe')
    player_8 = player_database.search(Player.surname == 'Sehili') + player_database.search(Player.firstname == 'Asma')
    print(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)


def sort_player_by_rank():
    player_1 = player_database.search(Player.surname == 'Ghazi') + player_database.search(Player.firstname == 'Imane')
    player_2 = player_database.search(Player.surname == 'Menguete') + player_database.search(Player.firstname == 'Kevin')
    player_3 = player_database.search(Player.surname == 'Sehili') + player_database.search(Player.firstname == 'Asma')
    player_4 = player_database.search(Player.surname == 'Boisvert') + player_database.search(Player.firstname == 'Guillaume')
    player_5 = player_database.search(Player.surname == 'Robineau') + player_database.search(Player.firstname == 'Chloe')
    player_6 = player_database.search(Player.surname == 'Dionne') + player_database.search(Player.firstname == 'Vanessa')
    player_7 = player_database.search(Player.surname == 'Mohamed Said Ali') + player_database.search(Player.firstname == 'Aymane')
    player_8 = player_database.search(Player.surname == 'Bourdon') + player_database.search(Player.firstname == 'Laurie-anne')
    print(player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8)


def display_all_tournament():
    print(tournament_database.all())


def display_all_round_of_a_tournament():
    print(round_database.all())


def display_all_match_of_a_tournament():
    print(match_database.all())


sort_player_by_alphabetical_order()
sort_player_by_rank()
display_all_tournament()
display_all_round_of_a_tournament()
display_all_match_of_a_tournament()
