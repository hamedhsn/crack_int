from ch2.linkedlist import LinkedList


class Stack(LinkedList):
    def __init__(self, data=None):
        super().__init__(data)

    @staticmethod
    def disabled_methods(func_name):
        raise Exception('Function `{}` Disabled'.format(func_name))

    def append(self):
        Stack.disabled_methods(self.append.__name__)

    def append_few(self):
        Stack.disabled_methods(self.append_few.__name__)

    def delete(self):
        Stack.disabled_methods(self.delete.__name__)

    def traverse(self):
        Stack.disabled_methods(self.traverse.__name__)

    def padding_after(self):
        Stack.disabled_methods(self.padding_after.__name__)

    def padding_before(self):
        Stack.disabled_methods(self.padding_before.__name__)

    def push(self, d):
        self.insert_before(d)

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            raise Exception('Empty Stack')

        tmp = self.head

        self.head = self.head.next
        return tmp.data

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
            raise Exception('Empty Stack')

        return self.head.data

if __name__ == '__main__':
    s = Stack(5)
    for i in range(4):
        s.push(i)

    s.print_all()

    print('popping item is : {}'.format(s.pop()))
    print('Peek item is : {}'.format(s.peek()))
