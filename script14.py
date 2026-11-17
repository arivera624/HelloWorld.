def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area


def calculate_tax(money, tax):
    total = money + (money * tax)
    return total


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


radius = float(input("Enter radius: "))
money = float(input("Enter money: "))
tax = float(input("Enter tax rate (decimal): "))
fahrenheit = float(input("Enter Fahrenheit: "))

print("Area of circle:", round(circle_area(radius), 2))
print("Total with tax:", f"{calculate_tax(money, tax):.2f}")
print("Celsius:", round(fahrenheit_to_celsius(fahrenheit), 4))
