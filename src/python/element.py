from src.python.osc_handler import OSCHandler
from src.python.config import ids
import logging


class Element(object):
    """ Abstract class representing an element on the Whiteboard. """

    def __init__(self, id, rotation, x, y):
        self.id = id
        self.rotation = rotation
        self.x = x
        self.y = y
        self.color = ids[self.id]['color']
        self.type = ids[self.id]['type']
        self.osc = OSCHandler()

    def __str__(self):
        return 'Element %s' % self.id

    def update_parameters(self, threshold=0.3, **params):
        for parameter, value in params.items():
            if abs(self.__dict__[parameter] - value) >= threshold:
                self.__dict__[parameter] = value

    @staticmethod
    def factory(**kwargs):
        element_id = kwargs['id']
        element_type = ids[element_id]['type']
        if element_type == 'octagon':
            return Octagon(**kwargs)


class Octagon(Element):

    def __init__(self, id, rotation, x, y):
        super().__init__(id, rotation, x, y)
        self.logger = logging.getLogger(__name__)

    def __str__(self):
        return 'Octagon %s (%s): %.2f rotation  %.2f x  %.2f y' \
               % (self.id, self.color, self.rotation, self.x, self.y)

    def set_parameters(self, rotation, x, y):
        self.x = x
        self.y = y
        self.rotation = rotation

    def send_audio_parameters(self):
        args = [self.id, self.rotation, self.x, self.y]
        self.logger.info('Setting parameters: %s' % str(self))
        self.osc.send_msg(args)