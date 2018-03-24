from pythonosc import osc_message_builder
from pythonosc import udp_client


class OSCHandler:

    def __init__(self, port=50000, ip='127.0.0.1'):
        self.port = port
        self.ip = ip
        self.client = udp_client.UDPClient(self.ip, self.port)

    def get_msg(self, address, args):
        msg = osc_message_builder.OscMessageBuilder(address=address)
        for arg in args:
            msg.add_arg(arg)
        return msg.build()

    def send_msg(self, address, args):
        msg = self.get_msg(address, args)
        self.client.send(msg)
        
