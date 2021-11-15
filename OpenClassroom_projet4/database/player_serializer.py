from OpenClassroom_projet4.model.Player_model import Player


class PlayerSerializer:

    @staticmethod
    def serialize(player: Player):
        serialized_player = {'first_name': player.firstname, 'last_name': player.last_name, 'rank': player.rank,
                             'player_id': player.player_id, 'total_score': player.total_score, 'date_of_birth':
                             player.date_of_birth}
        return serialized_player

    @staticmethod
    def deserialize(serialized_player: dict):
        return Player(last_name=serialized_player['last_name'], firstname=serialized_player['first_name'],
                      rank=serialized_player['rank'], player_id=serialized_player['player_id'],
                      total_score=serialized_player['total_score'], date_of_birth=serialized_player['date_of_birth'])
