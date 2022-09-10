import unittest
from main import UserDataGenerator

SAMPLE_DATA = {
    'user_id': 1,
    'user_name': 'Test',
    'user_last_name': 'Testowicz',
    'user_age': 18
}

class UserDataGeneratorTest(unittest.TestCase):

    def test_generate_data(self):
        sample_data = UserDataGenerator().generate_data(number_of_users=1)
        self.assertIsInstance(sample_data, list)
        self.assertIsInstance(sample_data[0], dict)
        self.assertTrue(len(sample_data) == 1)
        self.assertIsInstance(sample_data[0]['user_age'], int)

    def test_if_data_is_returned_as_correct_instance(self):
        sample_data = UserDataGenerator().generate_data(number_of_users=1)
        self.assertIsInstance(sample_data, list)

    def test_if_user_data_is_returned_as_correct_instance(self):
        sample_data = UserDataGenerator().generate_data(number_of_users=1)
        self.assertIsInstance(sample_data[0], dict)


if __name__ == '__main__':
    unittest.main()
