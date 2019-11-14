import unittest
import unittest.mock
from handler import UserHandler

class TestUserHandler(unittest.TestCase):
    def test_parse_user_data(self):
        test_user_data = {
            'additional_info': {
                'age':132,
                'work':'qwerfrhy',
                } 
                }

        u = UserHandler('name')
        r = u.parse(test_user_data)
        self.assertEqual(r, {'age':132, 'work': 'qwerfrhy'})


    @mock.patch('users_data')
    def test_get_user_data(mock_user_data):
        self.assertEqual()



if __name__ == '__main__':
    unittest.main()
