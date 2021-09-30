

class Player:
    def __init__(self, player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_3 = player_3
        self.player_4 = player_4
        self.player_5 = player_5
        self.player_6 = player_6
        self.player_7 = player_7
        self.player_8 = player_8

    def __str__(self):
        return self.player_1 + " " + self.player_2 + " " + self.player_3 + " " + self.player_4 + " " + self.player_5 + \
               " " + self.player_6 + " " + self.player_7 + " " + self.player_8


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
