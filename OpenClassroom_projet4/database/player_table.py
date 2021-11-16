from tinydb import TinyDB, Query

from OpenClassroom_projet4.database.player_serializer import PlayerSerializer
from OpenClassroom_projet4.model.Player_model import Player


class PlayerTable:

    def __init__(self):
        self.player_database = TinyDB('players_database.json')
        self.player_serializer = PlayerSerializer()

    def save_player(self, player):
        serialized_player = self.player_serializer.serialize(player)
        self.player_database.insert(serialized_player)

    def get_player(self, player_id):
        player_query = Query()
        serialized_player = self.player_database.search(player_query.player_id == player_id)
        player = self.player_serializer.deserialize(serialized_player[0])
        return player

    def save_players(self, players: list):
        serialized_players = []
        for player in players:
            serialized_player = self.player_serializer.serialize(player)
            serialized_players.append(serialized_player)
        self.player_database.insert_multiple(serialized_players)

    def get_players(self):
        serialized_players = self.player_database.all()
        players = []
        for serialized_player in serialized_players:
            player = self.player_serializer.deserialize(serialized_player)
            players.append(player)
        return players

    def update_first_name(self, player_id, first_name):
        player = Query()
        self.player_database.update({'first_name': first_name}, player.player_id == player_id)

    def clear_database(self):
        self.player_database.truncate()


if __name__ == '__main__':
    player_1 = Player(last_name='Darden', firstname='Mike', rank=5, player_id='46464646QSDFSD64', total_score=3)
    player_2 = Player(last_name='Mikaela', firstname='Arnold', rank=7, player_id='1234RF5456GH46TFD', total_score=1)
    PlayerTable().save_players([player_1, player_2])
    dsp = PlayerTable().get_players()
    print(dsp)
