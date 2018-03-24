import unittest
from src.python.whiteboard import Whiteboard
from src.python.element import Element


class TestWhiteboard(unittest.TestCase):

    def setUp(self):
        self.whiteboard = Whiteboard()
        self.element1 = Element.factory(id=0, rotation=0.1, x=0.2, y=0.3)
        self.element2 = Element.factory(id=1, rotation=0.4, x=0.5, y=0.6)
        self.param_list1 = [{'id': 1, 'x': 0.1, 'y': 0.3, 'rotation': 0.5},
                            {'id': 2, 'x': 0.0, 'y': 0.4, 'rotation': 0.9},
                            {'id': 3, 'x': 0.2, 'y': 0.3, 'rotation': 0.4}]
        self.param_list2 = [{'id': 0, 'x': 0.1, 'y': 0.3, 'rotation': 0.5},
                            {'id': 2, 'x': 0.0, 'y': 0.5, 'rotation': 0.9},
                            {'id': 3, 'x': 0.7, 'y': 0.3, 'rotation': 0.3}]

    def test_add_element(self):
        self.assertEqual(len(self.whiteboard.elements), 0)
        self.whiteboard.add_element(self.element1)
        self.assertEqual(len(self.whiteboard.elements), 1)

    def test_delete_element(self):
        self.whiteboard.add_element(self.element1)
        self.whiteboard.add_element(self.element2)
        self.whiteboard.delete_element(self.element1)
        self.assertEqual(len(self.whiteboard.elements), 1)
        self.assertEqual(self.whiteboard.elements[0], self.element2)

    def test_update(self):
        self.whiteboard.update(self.param_list1)
        self.assertEqual(len(self.whiteboard.elements), 3)
        self.assertEqual(self.whiteboard.get_element_ids(), [1, 2, 3])
        self.whiteboard.update(self.param_list2)
        self.assertEqual(self.whiteboard.get_element_ids(), [2, 3, 0])
        element2 = self.whiteboard.elements[0]
        element3 = self.whiteboard.elements[1]
        self.assertEqual(element2.x, 0.0)  # stayed same
        self.assertEqual(element2.y, 0.4)  # no change because under threshold
        self.assertEqual(element3.x, 0.7)  # changed

    def test_get_removed_element_ids(self):
        removed = self.whiteboard.get_removed_elements(self.param_list1)
        self.assertEqual(removed, [])
        self.whiteboard.update(self.param_list1)
        removed_ids = [element.id for element in
                       self.whiteboard.get_removed_elements(self.param_list2)]
        self.assertEqual(removed_ids, [1])


if __name__ == '__main__':
    unittest.main(warnings='ignore')
