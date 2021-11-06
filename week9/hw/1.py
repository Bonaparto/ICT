s = input()
print('Please inter i-th element in string to remove it.')
i = int(input())
s = s[:i] + s[i+1:]

print(s)