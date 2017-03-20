class Stack:

    def __init__(self):
        self.st = []

    def push(self,data):
        self.st.append(data)

    def pop(self):
        if len(self.st) <= 0:
            return
        return self.st.pop()

    def top(self):
        if not self.isEmpty():
            return self.st[-1]

    #
    # Checks whether stack is empty
    #
    def isEmpty(self):
        return len(self.st) == 0

    #
    # Prints the elements starting from the top of the stack
    #
    def printStack(self):
        if self.isEmpty():
            return
        data = self.pop()
        print data
        self.printStack()
        self.push(data)

    #
    # Inserts data at the bottom of the stack
    #
    def insertBottom(self, data):
        if self.isEmpty():
            self.push(data)
        else:
            d = self.pop()
            self.insertBottom(data)
            self.push(d)

    #
    # Reverses a stack recursively.
    # T(n)- O(n^2)
    #
    def reverseStack(self):
        if self.isEmpty():
            return
        data = self.pop()
        self.reverseStack()
        self.insertBottom(data)

    #
    # Insert an element at its correct position
    # in a sorted stack (The smallest element is at
    # the bottom of the stack).
    #
    def sortedInsert(self,data):
        if self.isEmpty() or data > self.top():
            self.push(data)
            return
        d = self.pop()
        self.sortedInsert(data)
        self.push(d)

    #
    # Sorts a stack in Ascending order using recursion.
    # The smallest element is at bottom, and
    # the largest element is at the top of the stack.
    # T(n)- O(n^2)
    #
    def sortStack(self):
        if self.isEmpty():
            return
        data = self.pop()
        self.sortStack()
        self.sortedInsert(data)


def main():
    s = Stack()
    l = list(map(int,raw_input().split()))
    for i in l:
        s.push(i)
    s.sortStack()
    s.printStack()


if __name__ == "__main__":
    main()