from unittest import TestCase
from unittest.mock import Mock, create_autospec, patch

from tw.eums.guy import Guy


class Test(TestCase):
    def test_should(self):
        p = Guy()
        #
        # self.assertEqual(p.get_fullname('123', '789'), '123 789')
        # self.assertEqual(p.get_age(), 10)
        # self.assertEqual(Guy.get_class_name(), 'Guy')

        # p.get_age = Mock(return_value=20)
        # self.assertEqual(p.get_age(), 20)
        #
        # p.get_fullname = Mock(return_value='James Harden')
        # self.assertEqual(p.get_fullname(), 'James Harden')

        # p.get_fullname = create_autospec(p.get_fullname, return_value='James Harden')
        # p.get_fullname('1')

        # p.get_age = Mock(side_effect=[10, 11, 12])
        #
        # self.assertEqual(p.get_age(), 10)
        # self.assertEqual(p.get_age(), 11)
        # self.assertEqual(p.get_age(), 12)

        # values = {('James', 'Harden'): 'James Harden', ('Tracy', 'Grady'): 'Tracy Grady'}
        #
        # p.get_fullname = Mock(side_effect=lambda x, y: values[(x, y)])
        # self.assertEqual(p.get_fullname('James', 'Harden'), 'James Harden')
        # self.assertEqual(p.get_fullname('Tracy', 'Grady'), 'Tracy Grady')

        # p.get_age = Mock(side_effect=TypeError('integer type'))
        # self.assertRaises(TypeError, p.get_age)

        # p.get_fullname = Mock(return_value='James Harden')
        #
        # p.get_fullname.assert_not_called()
        #
        # p.get_fullname('1', '2')
        #
        # p.get_fullname.assert_called()
        # p.get_fullname.assert_called_once()
        # p.get_fullname.assert_called_once_with('1', '2')
        #
        # p.get_fullname('3', '4')
        # p.get_fullname.assert_any_call('1', '2')
        #
        # p.get_fullname.reset_mock()
        # p.get_fullname.assert_not_called()
        #
        # self.assertEqual(p.get_fullname.called, False)
        # self.assertEqual(p.get_fullname.call_count, 0)
        #
        # p.get_fullname('1', '2')
        # p.get_fullname('3', '4')
        # self.assertEqual(p.get_fullname.called, True)
        # self.assertEqual(p.get_fullname.call_count, 2)

        # self.assertEqual(Guy.get_class_name(), 'Guy')
    #
    # @patch('tw.eums.guy.Guy.get_class_name')
    # def test_should_get_class_name(self, mock_get_class_name):
    #     mock_get_class_name.return_value = 'Guy'
    #
    #     self.assertEqual(Guy.get_class_name(), 'Guy')
    #
    # mock_get_class_name = Mock(return_value='Guy')
    #
    # @patch('tw.eums.guy.Guy.get_class_name', mock_get_class_name)
    # def test_should_get_class_name(self, ):
    #
    #     self.assertEqual(Guy.get_class_name(), 'Guy')

    # @patch.object(Guy, 'get_class_name', mock_get_class_name)
    # def test_should_get_class_name(self, ):
    #     self.assertEqual(Guy.get_class_name(), 'Guy')

    def test_should_get_class_name(self):
        mock_get_class_name = Mock(return_value='Person')

        with patch('tw.eums.guy.Guy.get_class_name', mock_get_class_name):
            self.assertEqual(Guy.get_class_name(), 'Person')

        self.assertEqual(Guy.get_class_name(), 'Guy')






























