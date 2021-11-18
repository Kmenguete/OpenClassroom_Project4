from datetime import datetime

from OpenClassroom_projet4.model.Tournament_model import Tournament


class TournamentSerializer:

    @staticmethod
    def serialize(tournament: Tournament):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        serialized_tournament = {'name': tournament.name, 'place': tournament.place, 'date': date_time,
                                 'description': tournament.description, 'number_of_rounds': tournament.number_of_rounds,
                                 'tournament_id': tournament.tournament_id, 'rounds': tournament.rounds,
                                 'players': tournament.players, 'players_dict': tournament.players_dict}
        return serialized_tournament

    @staticmethod
    def deserialize(serialized_tournament: dict):
        return Tournament(name=serialized_tournament['name'], place=serialized_tournament['place'],
                          date=serialized_tournament['date'], description=serialized_tournament['description'],
                          number_of_rounds=serialized_tournament['number_of_rounds'],
                          tournament_id=serialized_tournament['tournament_id'], rounds=serialized_tournament['rounds'],
                          players=serialized_tournament['players'], players_dict=serialized_tournament['players_dict'])
        