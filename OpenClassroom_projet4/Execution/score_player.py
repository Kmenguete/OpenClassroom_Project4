

class ScorePlayer:
    def __init__(self, score_player_1, score_player_2, score_player_3, score_player_4, score_player_5, score_player_6,
                 score_player_7, score_player_8):
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2
        self.score_player_3 = score_player_3
        self.score_player_4 = score_player_4
        self.score_player_5 = score_player_5
        self.score_player_6 = score_player_6
        self.score_player_7 = score_player_7
        self.score_player_8 = score_player_8

    def __str__(self):
        return self.score_player_1 + " " + self.score_player_2 + " " + self.score_player_3 + " " + self.score_player_4 + \
               " " + self.score_player_5 + " " + self.score_player_6 + " " + self.score_player_7 + " " + \
               self.score_player_8


if __name__ == '__main__':
    score_player_1 = input("Enter the score of player 1: ")
    score_player_2 = input("Enter the score of player 2: ")
    score_player_3 = input("Enter the score of player 3: ")
    score_player_4 = input("Enter the score of player 4: ")
    score_player_5 = input("Enter the score of player 5: ")
    score_player_6 = input("Enter the score of player 6: ")
    score_player_7 = input("Enter the score of player 7: ")
    score_player_8 = input("Enter the score of player 8: ")
    score_player = ScorePlayer(score_player_1, score_player_2, score_player_3, score_player_4, score_player_5,
                               score_player_6, score_player_7, score_player_8)
    print("Here is the score of each player at the end of the round")
