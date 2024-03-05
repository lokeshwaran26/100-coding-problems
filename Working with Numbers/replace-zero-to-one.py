def replace_0(num):
    temp = ''
    for i in str(num):
        i = str(i)
        if i == '0':
            temp += '1'
        else:
            temp += i
    return int(temp)
a = replace_0(910050670)
print(a)