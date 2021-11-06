print("What is your salary?")
salary = int(input())
print("What is you year of service?")
year = int(input())

if year > 5:
   print(f"Your net bonus amount is: {(salary * 5) / 100}")
else:
    print("You have no net bonus:(")