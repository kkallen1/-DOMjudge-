ans = 0
for _ in range(int(input())):
    d = input()

    if d=='Tetrahedron':
        ans += 4
    elif d=='Cube':
        ans += 6
    elif d=='Octahedron':
        ans += 8
    elif d=='Dodecahedron':
        ans += 12
    elif d=='Icosahedron':
        ans += 20
print(ans)