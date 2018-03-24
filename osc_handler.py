from pythonosc import osc_message_builder
from pythonosc import udp_client
import logging


class OSCHandler:

    def __init__(self, port=50000, ip='192.168.0.50'):
        self.port = port
        self.ip = ip
        self.client = udp_client.UDPClient(self.ip, self.port)
        self.logger = logging.getLogger(__name__)

    def get_msg(self, args, address):
        msg = osc_message_builder.OscMessageBuilder(address=address)
        for arg in args:
            msg.add_arg(arg)
        return msg.build()

    def send_msg(self, args, address='/params'):
        msg = self.get_msg(args, address)
        self.logger.debug(
            'Send message args %s address %s to ip %s on port %s'
            % (args, address, self.ip, self.port))
        self.client.send(msg)
