meal_cost = int(input())

tax = meal_cost * 10 / 100
tip = meal_cost * 18 / 100

print("Tax: ", "%.2f" % tax, "\nTip: ", "%.2f" % tip, "\n", "Total cost: ", "%.2f" % (meal_cost + tax + tip), sep='')