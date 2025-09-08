# Rates in cents
rate_first_1000 = 7.633
rate_above_1000 = 9.259

# Test cases
test_kwh = [1500, 764, 1215, 812]

# Loop through each test case
for kwh in test_kwh:
    # Print the input prompt (like the assignment)
    print(f"Enter the KW hours used: {kwh}")

    # Calculate total in cents
    if kwh <= 1000:
        total_cents = kwh * rate_first_1000
    else:
        total_cents = (1000 * rate_first_1000) + ((kwh - 1000) * rate_above_1000)

    # Convert to dollars
    amount_owed = total_cents / 100

    # Print output
    print(f"Amount owed is ${amount_owed}\n")
