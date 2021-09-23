
class Player:
    def __init__(self, surname, firstname, date_of_birth, sex, rank):
        self.surname = surname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.rank = rank

    def __str__(self):
        return self.surname + " " + self.firstname + " " + self.date_of_birth + " " + self.sex + " " + self.rank


if __name__ == '__main__':
    surname = input("enter the surname: ")
    firstname = input("enter the firstname: ")
    date_of_birth = input("enter the date of birth: ")
    sex = input("enter the sex: ")
    rank = input("enter the rank: ")
    player = Player(surname, firstname, date_of_birth, sex, rank)
    print("Here is your player: " + str(player))
