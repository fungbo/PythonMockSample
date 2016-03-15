from unittest import TestCase

from mock import patch, Mock, MagicMock

from tw.eums.class_sample import ClassSample


class ClassSampleTest(TestCase):
    mock_get_class_name_2 = Mock(return_value='mock_class_name_2')
    mock_get_class_name_3 = Mock(return_value='mock_class_name_3')

    def test_should_get_instance_name(self):
        instance = ClassSample('New Instance')
        instance_name = instance.get_instance_name()

        self.assertEqual(instance_name, 'New Instance')

    def test_mock_get_instance_name(self):
        instance = ClassSample('New Instance')
        instance.get_instance_name = MagicMock(return_value='mock_instance_name')
        instance_name = instance.get_instance_name()

        self.assertEqual(instance_name, 'mock_instance_name')

    def test_should_get_class_name(self):
        class_name = ClassSample.get_class_name()

        self.assertEqual(class_name, 'ClassSample')

    @patch('tw.eums.class_sample.ClassSample.get_class_name')
    def test_mock_get_class_name_1(self, mock_get_class_name):
        mock_get_class_name.return_value = 'mock_class_name_1'
        class_name = ClassSample.get_class_name()

        self.assertEqual(class_name, 'mock_class_name_1')

    @patch('tw.eums.class_sample.ClassSample.get_class_name', mock_get_class_name_2)
    def test_mock_get_class_name_2(self):
        class_name = ClassSample.get_class_name()

        self.assertEqual(class_name, 'mock_class_name_2')

    @patch.object(ClassSample, 'get_class_name', mock_get_class_name_3)
    def test_mock_get_class_name_3(self):
        class_name = ClassSample.get_class_name()

        self.assertEqual(class_name, 'mock_class_name_3')

    def test_mock_get_class_name_4(self):
        mock_get_class_name_4 = Mock(return_value='mock_class_name_4')
        with patch('tw.eums.class_sample.ClassSample.get_class_name', mock_get_class_name_4):
            class_name = ClassSample.get_class_name()

            self.assertEqual(class_name, 'mock_class_name_4')

        class_name = ClassSample.get_class_name()
        self.assertEqual(class_name, 'ClassSample')

    def tearDown(self):
        self.test_should_get_instance_name()
        self.test_should_get_class_name()
