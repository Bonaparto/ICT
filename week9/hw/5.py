from abc import ABCMeta
from typing import Mapping


s = input().split()
cnt = 0

for word in s:
    cnt += word.count('.')
    word = word.replace('.', ',')
    print(word, end=' ')

print('\nNumber of commas is', cnt)