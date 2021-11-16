def isPrime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

print('Enter starting number: ', end='')
s = int(input())
print('Enter ending number: ', end='')
e = int(input())
print(f'Prime numbers between {s} and {e} are:')
for i in range(s, e + 1):
    if isPrime(i):
        print(i)