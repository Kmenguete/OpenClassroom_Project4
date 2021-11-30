from datetime import datetime

from OpenClassroom_projet4.serializers.player_serializer import PlayerSerializer
from OpenClassroom_projet4.serializers.round_serializer import RoundSerializer
from OpenClassroom_projet4.model.tournament_model import Tournament
from OpenClassroom_projet4.utils.config import Config


class TournamentSerializer:
    """ The serialization is the way that let us to store our class object in the database. The package used to store
    data is called "TinyDB". During the development of the application, we found that this package was not very
    suitable for this project but this package was required by the customer. To store a tournament object,
    we should convert it into a dictionary. The serialization is the process of converting an object into a
    dictionary and to get this object back to the program(in particular when a report is requested), we deserialize
    it(meaning we convert our dictionary into an object). To serialize a tournament object, we should first serialize
    rounds object and players object because a tournament consist of rounds and players. To serialized rounds object,
    we should first serialize matches object because a round consist of a list of matches. And finally, to serialize
    a match object, we should first serialize players because a match object consist of two players and their score.
    Each object depends each other in order to be properly stored in the database.
    """

    def __init__(self):
        """ The init method import the Round Serializer object and the Player Serializer object because to serialize a
        Tournament, you should first serialize rounds object and players object.
                            """
        self.round_serializer = RoundSerializer()
        self.player_serializer = PlayerSerializer()

    def serialize_tournament_rounds(self, rounds):
        """ The serialize_tournament_rounds method serializes rounds object of Tournament object.
                                    """
        serialized_rounds = []
        for round in rounds:
            serialized_round = self.round_serializer.serialize(round)
            serialized_rounds.append(serialized_round)
        return serialized_rounds

    def serialize_tournament_players(self, players):
        """ The serialize_tournament_players method serializes players object of Tournament object.
                                            """
        if players is None:
            return

        serialized_players = []
        serialized_player_dict = {}
        for player in players:
            serialized_player = self.player_serializer.serialize(player)
            serialized_players.append(serialized_player)
            serialized_player_dict[player.player_id] = serialized_player

        return serialized_players, serialized_player_dict

    def serialize(self, tournament: Tournament):
        """ The serialize method serializes Tournament object.
                                                    """
        date_time = tournament.date.strftime(Config.DATE_STRING_FORMAT)
        serialized_rounds = None
        if tournament.rounds is not None:
            serialized_rounds = self.serialize_tournament_rounds(tournament.rounds)

        serialized_players, serialized_player_dict = None, None
        if tournament.players is not None:
            serialized_players, serialized_player_dict = self.serialize_tournament_players(tournament.players)

        serialized_tournament = {'name': tournament.name, 'place': tournament.place, 'date': date_time,
                                 'description': tournament.description, 'number_of_rounds': tournament.number_of_rounds,
                                 'tournament_id': tournament.tournament_id, 'rounds': serialized_rounds,
                                 'players': serialized_players, 'players_dict': serialized_player_dict}
        return serialized_tournament

    def deserialize(self, serialized_tournament: dict):
        """ The deserialize method deserializes Tournament object.
                                                            """
        date_time_obj = datetime.strptime(serialized_tournament['date'], Config.DATE_STRING_FORMAT)
        rounds = []
        if serialized_tournament['rounds'] is not None:
            for serialized_round in serialized_tournament['rounds']:
                round = self.round_serializer.deserialize(serialized_round)
                rounds.append(round)

        players = []
        player_dict = {}
        if serialized_tournament['players'] is not None:
            for serialized_player in serialized_tournament['players']:
                player = self.player_serializer.deserialize(serialized_player)
                players.append(player)
                player_dict[player.player_id] = player
        tournament = Tournament(name=serialized_tournament['name'], place=serialized_tournament['place'],
                                date=date_time_obj, description=serialized_tournament['description'],
                                number_of_rounds=serialized_tournament['number_of_rounds'],
                                tournament_id=serialized_tournament['tournament_id'], rounds=rounds,
                                players=players, players_dict=player_dict)
        return tournament
