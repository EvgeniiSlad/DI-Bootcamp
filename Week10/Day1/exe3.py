class Simplestack():

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(int(data))

    def pop(self):
        return self.stack.pop()

    def inc(self, n, inc_by):
        n, inc_by = int(n), int(inc_by)
        self.stack[n-1] += inc_by

    def run(self, operations: list):
        funcs = {
            'push': self.push,
            'pop': self.pop,
            'inc': self.inc
        }

        for operation in operations:
            op, *args = operation.split(' ')
            if (op == 'push'):
                self.push(*args)
            elif (op == 'pop'):
                self.pop()
            elif op=='inc':
                self.inc(*args)

            funcs[op](*args)

            print(self.stack[-1] if self.stack else "EMPTY")


super_stuck = Simplestack()
super_stuck.run(['push 4', 'push 5', 'push 6',
                'inc 2 1', 'inc 1 3', 'pop', 'pop'])