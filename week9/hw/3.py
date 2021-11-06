s = input().split()
cnt = 0

for word in s:
    word += ' '
    for char in word:
        if char == ' ':
            break
        cnt += 1

print(cnt)