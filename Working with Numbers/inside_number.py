n = [[5,6,7,4],
     [8,9,1,3],
     [2,3,4,5],
     [9,4,5,7]]

for i in range(len(n)):
    for j in range(len(n)):
        if i == 0 or i == len(n) -1 or j == 0 or j == len(n) -1:
            continue
        else:
            print(n[i][j])
