r = 2
c = 3
matirx = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matirx.append(a)

for i in range(r):
    for j in range(c):
        print(matirx[i][j], end=' ')
    print()