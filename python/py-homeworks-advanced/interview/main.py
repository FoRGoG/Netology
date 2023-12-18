class Stack:
    def __init__(self):
        self.x = []

    def is_empty(self):
        return len(self.x) == 0


    def push(self, item):
        self.x.append(item)


    def pop(self):
        if not self.is_empty():
            return self.x.pop()


    def peek(self):
        if not self.is_empty():
            return self.x[-1]


    def size(self):
        return len(self.x)


def checking_the_string(data):
    s = Stack()
    for item in data:
        if item in '([{':
            s.push(item)
        elif item in ')]}':
            if item == ')' and s.pop() != '(' or \
                item == ']' and s.pop() != '[' or \
                item == '}' and s.pop() != '{':
                return 'Строка несбалансирована'
    return 'Строка сбалансирована' if s.is_empty() \
        else 'В остались открывающиеся скобки'


if __name__ == '__main__':
    input_data = input('Введите последовательность строк со скобками: ')
    print(checking_the_string(input_data))
