hours = int(input("Enter the KW hours used:"))

if hours <= 1000:
    amount = hours * 0.07633
else:
    amount = (1000 * 0.07633) + ((hours - 1000) * 0.09259)

print("Amount owed is $", amount, sep="")
