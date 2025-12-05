a = [x for x in input()]

m_s, m_c = 0, 0
for i in set(a):
    tmp = a.count(i)
    if tmp>m_c:
        m_s, m_c = i, tmp

print(m_s)