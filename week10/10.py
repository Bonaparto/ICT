number = int(input())
print("Last digit is divisible by 3." if (number % 10) % 3 == 0 else "Last digit is NOT divisible by 3.")