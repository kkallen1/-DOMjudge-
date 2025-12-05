def f(behind, middle):
    if len(behind) == 0:
        return []
    
    root = behind[0]
    root_idx = middle.index(root)

    m_l = middle[:root_idx:]
    m_r = middle[root_idx+1::]

    Len = len(m_l)
    b_l = behind[1:Len+1:]
    b_r = behind[Len+1::]

    return f(b_l, m_l) + f(b_r, m_r) + [root]

while True:
    try:
        behind, middle = map(str, input().split())
        behind = [x for x in behind]
        middle = [x for x in middle]

        print(*f(behind, middle), sep="")
    except EOFError:
        break