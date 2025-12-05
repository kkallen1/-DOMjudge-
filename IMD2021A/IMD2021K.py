class Tree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def i(self, data):
        if data > self.data:
            if self.right:
                self.right.i(data)
            else:
                self.right = Tree(data)
        else:
            if self.left:
                self.left.i(data)
            else:
                self.left = Tree(data)
    def o(self):
        if self.left:
            self.left.o()
        ans.append(self.data)
        if self.right:
            self.right.o()

while True:
    try:
        data = list(int(x) for x in input().split(','))
        tree = Tree(data.pop(0))

        for node in data:
            tree.i(node)
        
        ans = []
        tree.o()
        print(*ans)
    except EOFError:
        break