held = int(input())
att = int(input())
perc = round((att / held) * 100)

print(f"Percent of attended classes is {perc}.")
print("You are allowed to take the exam." if perc >= 75 else "You are NOT allowed to take the exam.")