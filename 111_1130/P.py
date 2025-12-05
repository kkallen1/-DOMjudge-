def f(behind, middle):
    if not behind:
        return []

    r_i = middle.index(behind[0])
    m_l = middle[:r_i:]
    m_r = middle[r_i+1::]

    L = len(m_l)
    b_l = behind[1:L+1:]
    b_r = behind[L+1::]

    return f(b_l, m_l) + f(b_r, m_r) + [behind[0]]

import sys

for l in sys.stdin:
    behind, middle = map(str, l.strip().split())

    print(*f(behind, middle), sep="")