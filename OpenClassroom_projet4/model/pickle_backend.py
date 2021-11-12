import pickle


class DataBase:

    @staticmethod
    def save_tournament_data(tournament, filename):
        with open(filename, 'wb') as file:
            pickle.dump(tournament, file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def save_players_data(players, filename):
        with open(filename, 'wb') as file:
            pickle.dump(players, file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def save_matches_data(matches, filename):
        with open(filename, 'wb') as file:
            pickle.dump(matches, file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def save_rounds_data(rounds, filename):
        with open(filename, 'wb') as file:
            pickle.dump(rounds, file, pickle.HIGHEST_PROTOCOL)
