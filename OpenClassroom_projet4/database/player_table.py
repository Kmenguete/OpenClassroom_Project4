from tinydb import Query, TinyDB

from OpenClassroom_projet4.database.player_serializer import PlayerSerializer
from OpenClassroom_projet4.model.Player_model import Player
from OpenClassroom_projet4.utils.config import Config


class PlayerTable:

    def __init__(self):
        self.database = TinyDB('db.json')
        self.player_table = self.database.table(Config.PLAYER_TABLE_NAME)
        self.player_serializer = PlayerSerializer()

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

    def get_players(self):
        serialized_players = self.player_table.all()
        players = []
        for serialized_player in serialized_players:
            player = self.player_serializer.deserialize(serialized_player)
            players.append(player)
        return players

    def update_first_name(self, player_id, first_name):
        Player = Query()
        self.player_table.update({'first_name': first_name}, Player.player_id == player_id)

    def update_player_total_score(self, player_id, total_score):
        Player = Query()
        self.player_table.update({'total_score': total_score}, Player.player_id == player_id)

    def clear_database(self):
        self.player_table.truncate()


if __name__ == '__main__':
    player_1 = Player(last_name='Darden', firstname='Mike', rank=5, player_id='46464646QSDFSD64', total_score=3)
    player_2 = Player(last_name='Mikaela', firstname='Arnold', rank=7, player_id='1234RF5456GH46TFD', total_score=1)
    PlayerTable().save_players([player_1, player_2])
    dsp = PlayerTable().get_players()
    print(dsp)
