

class Player:
    def __init__(self, surname, firstname, birthdate, sex):
        self.surname = surname
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex

    def __str__(self):
        return self.surname + " " + self.firstname + " " + self.birthdate + " " + self.sex


if __name__ == '__main__':
    surname = input("Enter the surname: ")
    firstname = input("Enter the firstname: ")
    birthdate = input("Enter the birthdate: ")
    sex = input("Enter the sex: ")
    player = Player(surname, firstname, birthdate, sex)
    print("You have successfully created a player: " + str(player))
