class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def i(self, data):
        if data<self.data:
            if self.left:
                self.left.i(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.i(data)
            else:
                self.right = Node(data)
    
    def o(self):
        if self.left:
            self.left.o()
        if self.right:
            self.right.o()
        ans.append(self.data)

for _ in range(int(input())):
    n = int(input())
    d=  list(map(int, input().split(',')))

    tree = Node(d[0])
    for now in d[1::]:
        tree.i(now)

    ans = []
    tree.o()
    print(*ans, sep=',')