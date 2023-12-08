from main import check_status, folder, name
import unittest
class TestSummarize(unittest.TestCase):

    def test_status_positive(self):
        expected = 200
        result = check_status()
        self.assertEqual(result.status_code, expected)

    def test_status_negative(self):
        expected = 400
        result = check_status()
        self.assertNotEqual(result.status_code, expected)
    def test_create_folder_positive(self):
        expected = 409
        result = folder(name)
        self.assertEqual(result, expected)

    def test_create_folder_negative(self):
        expected = 404
        result = folder(name)
        self.assertNotEqual(result, expected)