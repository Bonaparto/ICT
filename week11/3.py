print('Given: numbers = ', end='')
a = [int(i) for i in input().split(',')]
print('Output:')
for i in a:
    if i > 300:
        break
    elif (i > 120):
        continue
    elif(i % 3 == 0):
        print(i)