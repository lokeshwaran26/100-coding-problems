n = 35
m = 96
li = []
for i in range(n,m+1):
    if i % 10 == 0:
        li.append(i)

if len(li) == 0:
    print('-1')
elif len(li) % 2 == 0:
    mid1 = li[ len(li) // 2 -1]
    mid2 = li[ len(li) // 2]
    print(mid1, mid2)
else:
    mid = li[len(li) // 2]
    print(min)