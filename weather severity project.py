# Weather Severity Project
# Version with test data already included (no manual input)

# Test case data (rain, wind)
data_list = [
    (0.2, 25),
    (1.0, 35),
    (4.5, 45)
]

# Initialize totals and count
total_rain = 0.0
total_wind = 0.0
count = 0

# Process each tuple in the list
for rain, wind in data_list:
    total_rain += rain
    total_wind += wind
    count += 1

# Calculate averages and severity
if count > 0:
    avg_rain = total_rain / count
    avg_wind = total_wind / count
    severity = (avg_rain * 10) + avg_wind

    # Output results
    print(f"The average rain is {avg_rain:.1f} inches")
    print(f"The average wind is {avg_wind:.1f} mph")
    print(f"The weather severity for these {count} readings is: {severity:.1f}")
else:
    print("No data entered.")

