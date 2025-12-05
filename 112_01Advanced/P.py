class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def i_l(self, data):
        if self.left:
            self.left.i_l(data)
        else:
            if isinstance(data, Node):
                self.left = data
            else:
                self.left = Node(data)
    
    def i_r(self, data):
        if self.right:
            self.right.i_l(data)
        else:
            if isinstance(data, Node):
                self.right = data
            else:
                self.right = Node(data)
    
    def o(self, kk=0):
        global ans
        if not self.left and not self.right:
            ans += kk

        if self.left:
            self.left.o(kk+1)
        if self.right:
            self.right.o(kk+1)

n = int(input())
d = list(map(int, input().split()))

while len(d)>1:
    d.sort(key=lambda x: x.data if isinstance(x, Node) else x, reverse=True)

    b = d.pop()
    a = d.pop()

    fa = isinstance(a, Node)
    fb = isinstance(b, Node)

    if fa and fb:
        tmp = a.data + b.data
    elif fa:
        tmp = a.data + b
    elif fb:
        tmp = a + b.data
    else:
        tmp = a + b

    tmp = Node(tmp)
    tmp.i_l(b)
    tmp.i_r(a)
    
    d.append(tmp)

ans = 0
d[-1].o()
print(ans)