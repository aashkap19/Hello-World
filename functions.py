import math

# Function 1: Area of a Circle
def circle_area(pi, radius):
    return pi * (radius ** 2)

# Function 2: Total Due with Tax
def total_due(money, tax_rate):
    return money + (money * tax_rate)

# Function 3: Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


# --- Main Program ---

# 1. Area of a Circle Test Cases
circle_radii = [10, 6, 24, 2, 1]
print("=== Area of Circle ===")
for radius in circle_radii:
    area = circle_area(math.pi, radius)
    print(f"Radius: {radius} -> Area: {area:.2f}")

print("\n=== Total Due with Tax ===")
# 2. Total Due with Tax Test Cases
tax_cases = [
    (20, 6),  # money, tax%
    (54, 4),
    (68, 8)
]

for money, tax_percent in tax_cases:
    tax_rate = tax_percent / 100
    total = total_due(money, tax_rate)
    print(f"Money: {money}, Tax: {tax_percent}% -> Total Due: {total:.2f}")

print("\n=== Fahrenheit to Celsius ===")
# 3. Fahrenheit to Celsius Test Cases
fahrenheit_values = [32, 80, 73, 42]

for f in fahrenheit_values:
    celsius = fahrenheit_to_celsius(f)
    print(f"Fahrenheit: {f} -> Celsius: {celsius:.5f}")
