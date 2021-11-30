from datetime import datetime

from OpenClassroom_projet4.serializers.match_serializer import MatchSerializer
from OpenClassroom_projet4.model.round_model import Tour
from OpenClassroom_projet4.utils.config import Config


class RoundSerializer:
    """ The serialization is the way that let us to store our class object in the database. The package used to store
    data is called "TinyDB". During the development of the application, we found that this package was not very suitable
    for this project but this package was required by the customer. To store a round object, we should convert it into
    a dictionary. The serialization is the process of converting an object into a dictionary and to get this object back
    to the program (in particular when a report is requested), we deserialize it(meaning we convert our dictionary into
    an object). To serialize a round object, we should first serialize matches object because a round consist of a list
    of matches. This list of matches consist of serialized matches object and each serialized match object consist of
    serialized players object. As we can see, each object depend each other to be stored properly in the database.
    """

    def __init__(self):
        """ The init method import the Match Serializer object because to serialize a Round, you should first
                serialize matches object.
                    """
        self.match_serializer = MatchSerializer()

    def serialize(self, round: Tour):
        """ The serialize method serializes Round object and matches object.
                            """
        serialized_matches = []
        for match in round.matches:
            serialized_match = self.match_serializer.serialize(match)
            serialized_matches.append(serialized_match)

        date_time = round.start_date.strftime(Config.DATE_STRING_FORMAT)
        serialized_round = {'round_id': round.round_id, 'round_name': round.round_name, 'start_date': date_time,
                            'matches': serialized_matches}
        return serialized_round

    def deserialize(self, serialized_round: dict):
        """ The deserialize method deserializes Round object and matches object.
                                    """
        deserialized_matches = []
        for serialized_match in serialized_round['matches']:
            match = self.match_serializer.deserialize(serialized_match)
            deserialized_matches.append(match)

        date_time_obj = datetime.strptime(serialized_round['start_date'], Config.DATE_STRING_FORMAT)

        return Tour(round_id=serialized_round['round_id'], round_name=serialized_round['round_name'],
                    start_date=date_time_obj, matches=deserialized_matches)
