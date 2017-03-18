from unittest import TestCase
from unittest.mock import Mock, MagicMock

from tw.eums.person import Person


class MagicMethodTest(TestCase):

    def setUp(self):
        self.jay = Person()

    def test_use_mock(self):
        m = Mock()
        m.__str__ = Mock(return_value='mock')
        m.__iter__ = Mock(return_value=iter([]))

        self.assertEqual(str(m), 'mock')
        self.assertEqual(list(m), [])

    def test_use_magic_mock(self):
        m = MagicMock()
        m.__str__.return_value = 'magic mock'
        m.__iter__.returen_value = [1,2]

        self.assertEqual(str(m), 'magic mock')
        self.assertEqual(list(m), [])
        self.assertEqual(int(m), 1)
        self.assertEqual(len(m), 0)

