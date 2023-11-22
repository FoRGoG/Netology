class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.start = -1
        self.end = len(list_of_list)

    def __iter__(self):
        self.result = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.result)
        except StopIteration:
            self.start += 1
            if self.start == self.end:
                raise StopIteration
            self.result = iter(self.list_of_list[self.start])
            item = next(self.result)
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()