print("What is your total quantity?")
q = int(input())
s = q * 100
print(f"Total cost for you is: {s - s * 0.1}" if q > 1000 else f"Total cost for you is: {s}")