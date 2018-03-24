import unittest
from osc_handler import OSCHandler


class TestOSCHandler(unittest.TestCase):

    def setUp(self):
        self.osc = OSCHandler()
        self.address = '/params'
        self.args = ['1', '0.1', '0.3', '0.9']

    def test_get_msg(self):
        msg = self.osc.get_msg(self.args, self.address)
        self.assertEqual(msg.address, self.address)
        self.assertEqual(msg.params, self.args)

    def test_send_msg(self):
        self.osc.send_msg(self.args, self.address)


if __name__ == '__main__':
    unittest.main()
