from unittest import TestCase
from unittest.mock import MagicMock

from tw.eums.person import Person


# Run with Python 3.6
class PersonTest(TestCase):
    def setUp(self):
        self.mike = Person()

    def test_should_get_age(self):
        self.mike.get_age = MagicMock(return_value=10)

        self.mike.get_age.assert_not_called()
        self.assertEqual(self.mike.get_age(), 10)
        self.mike.get_age.assert_called_once()
        self.mike.get_age.assert_called_once_with()
        self.mike.get_age()
        self.mike.get_age.assert_called()

    def test_should_raise_exception(self):
        self.mike.get_age = MagicMock(side_effect=KeyError('got a error'))

        self.assertRaises(KeyError, self.mike.get_age)

    def test_should_return_age_in_sequence(self):
        self.mike.get_age = MagicMock(side_effect=[5, 4, 3, 2, 1])

        self.assertEqual(self.mike.get_age(), 5)
        self.assertEqual(self.mike.get_age(), 4)
        self.assertEqual(self.mike.get_age(), 3)
        self.assertEqual(self.mike.get_age(), 2)
        self.assertEqual(self.mike.get_age(), 1)

    def test_should_return_age_with_parameters(self):
        values = {(1, 2): 5, (2, 3): 4}
        self.mike.get_sum = MagicMock(side_effect=lambda x, y: values[(x, y)])

        self.assertEqual(self.mike.get_sum(1, 2), 5)
        self.assertEqual(self.mike.get_sum(2, 3), 4)
