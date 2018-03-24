import unittest
from element import Element, Octagon


class TestElement(unittest.TestCase):

    def setUp(self):
        self.element = Element(0, 0.1, 0.2, 0.9)

    def test_update_parameters(self):
        new_parameters = {'rotation': 0.5, 'x': 0.3, 'y': 0.5}
        self.element.update_parameters(**new_parameters)
        self.assertEqual(self.element.rotation, 0.5)
        self.assertEqual(self.element.x, 0.2)
        self.assertEqual(self.element.y, 0.5)
        new_parameters = {'rotation': 0.6, 'x': 0.4, 'y': 0.6}
        self.element.update_parameters(threshold=0.0, **new_parameters)
        self.assertEqual(self.element.rotation, 0.6)
        self.assertEqual(self.element.x, 0.4)
        self.assertEqual(self.element.y, 0.6)
        self.element.update_parameters(threshold=0.5, x=1.0)
        self.assertEqual(self.element.x, 1.0)

    def test_factory_octagon(self):
        kwargs = {'id': 0, 'rotation': 0.1, 'x': 0.2, 'y': 0.9}
        element = Element.factory(**kwargs)
        self.assertEqual(element.id, 0)
        self.assertEqual(element.rotation, 0.1)
        self.assertEqual(element.x, 0.2)
        self.assertEqual(element.y, 0.9)
        self.assertIsInstance(element, Octagon)


if __name__ == '__main__':
    unittest.main()
