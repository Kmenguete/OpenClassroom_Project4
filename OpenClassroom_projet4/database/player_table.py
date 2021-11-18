from tinydb import Query

from OpenClassroom_projet4.database.player_serializer import PlayerSerializer
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.utils.config import Config


class PlayerTable:

    def __init__(self):
        self.database = Config.DATABASE
        self.player_serializer = PlayerSerializer()
        self.player_table = self.database.table('Player_table')

    def save_player(self, player):
        serialized_player = self.player_serializer.serialize(player)
        self.player_table.insert(serialized_player)

    def get_player(self, player_id):
        player_query = Query()
        serialized_player = self.player_table.search(player_query.player_id == player_id)
        player = self.player_serializer.deserialize(serialized_player[0])
        return player

    def save_players(self, players: list):
        serialized_players = []
        for player in players:
            serialized_player = self.player_serializer.serialize(player)
            serialized_players.append(serialized_player)
        self.player_table.insert_multiple(serialized_players)

    def update_players(self, players: list):
        serialized_players = []
        for player in players:
            serialized_player = self.player_serializer.serialize(player)
            serialized_players.append(serialized_player)
        self.player_table.update_multiple(serialized_players)

    def get_players(self):
        serialized_players = self.player_table.all()
        players = []
        for serialized_player in serialized_players:
            player = self.player_serializer.deserialize(serialized_player)
            players.append(player)
        return players

    def update_first_name(self, player_id, first_name):
        player = Query()
        self.player_table.update({'first_name': first_name}, player.player_id == player_id)

    def clear_player_table(self):
        self.player_table.truncate()


if __name__ == '__main__':
    player_1 = Player(last_name='Darden', firstname='Mike', rank=5, player_id='46464646QSDFSD64', total_score=3)
    player_2 = Player(last_name='Mikaela', firstname='Arnold', rank=7, player_id='1234RF5456GH46TFD', total_score=1)
    PlayerTable().save_players([player_1, player_2])
    dsp = PlayerTable().get_players()
    print(dsp)
