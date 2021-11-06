size = input()
pepperoni = input()
cheese = input()
bill = 0

size, pepperoni, cheese = size[-2], pepperoni[-2], cheese[-2]
if size == 'L': 
    bill += 25
    if pepperoni == 'Y':
        bill += 3
elif size == 'M':
    bill += 20
    if pepperoni == 'Y':
        bill += 3
else:
    bill += 15
    if pepperoni == 'Y':
        bill += 2

if cheese == 'Y':
    bill += 1

print("Your finall bill is:", bill)