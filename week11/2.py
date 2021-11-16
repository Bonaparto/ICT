print('Enter number:', end=' ')
n, s, av = int(input()), 0, 0
for i in range(1, n + 1):
    s += i
print(f'Sum of first {n} numbers is: {s}')
print(f'Average of {n} numbers is: {s / n}')