import unittest
from collections_1 import ids_func
from collections_2 import que
from collections_3 import stat

class TestEqual(unittest.TestCase):

    def test_max_key(self):
        result = stat()
        self.assertEqual(result, 'yandex')
    def test_que(self):
        data = que()
        self.assertEqual(data, 'Запросов из 2-х слов: 42.86%, Запросов из 3-х слов: 57.14%')

    def test_ids_strings(self):
        finish = ids_func()
        self.assertEqual(finish, {98, 35, 213, 54, 119, 15})

if __name__ == '__main__':
    unittest.main()



