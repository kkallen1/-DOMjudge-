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
    
    def o(self, kk):
        if not self.left and not self.right:
            ans[self.data] = len(kk)
            return
        
        if self.left:
            self.left.o(kk+['0'])
        if self.right:
            self.right.o(kk+['1'])

for _ in range(int(input())):
    d = list(map(int, input().split(',')))
    ans = {x:0 for x in d}

    while len(d)>1:
        d.sort(key=lambda x: x.data if isinstance(x, Node) else x, reverse=True)

        b = d.pop()
        a = d.pop()

        if isinstance(a, Node) and isinstance(b, Node):
            tmp = a.data + b.data
        elif isinstance(a, Node):
            tmp = a.data + b
        elif isinstance(b, Node):
            tmp = a + b.data
        else:
            tmp = a + b
        
        tmp = Node(tmp)
        tmp.i_l(b)
        tmp.i_r(a)

        d.append(tmp)
    
    d[0].o([])
    print(*ans.values(), sep=",")
    # print(ans)