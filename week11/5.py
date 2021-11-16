print('Enter the number of terms: ', end='')
n = int(input())
fib = []
fib.append(0)
fib.append(1)
print('Fibbonaci sequence:')
for i in range(n): 
    if i > 1: 
        temp = fib[i-1] + fib[i-2]
        print(temp, end=' ')
        fib.append(temp)
    else:
        print(fib[i], end=' ')