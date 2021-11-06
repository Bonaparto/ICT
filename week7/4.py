deposit = int(input())

deposit = deposit * 4 / 100 + deposit 
print("After one year:", "%.2f" % deposit)

deposit = deposit + deposit * 4 / 100
print("After two years:", "%.2f" % deposit)

deposit = deposit + deposit * 4 / 100
print("After three years:", "%.2f" % deposit)