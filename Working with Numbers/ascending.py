li = [ 4, 6, 8, 10]
for i in li:
    if i == li[-1]:
        continue
    for j in range(i, li[-1] + 1):
        print(j, end=' ')
    print()