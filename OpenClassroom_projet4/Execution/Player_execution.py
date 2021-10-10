
class Player:
    def __init__(self, surname, firstname, birthdate, sex, rank):
        self.surname = surname
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.rank = rank

    def __repr__(self):
        return "Player(" + repr(self.rank) + ")"

    def __str__(self):
        return self.surname + " " + self.firstname + " " + self.birthdate + " " + self.sex + " " + self.rank


if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    rank = input("enter the rank of the player: ")
    player = Player(surname, firstname, birthdate, sex, rank)
    print("You have successfully created a player: " + str(player))
