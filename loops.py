# Taco Palace Automated Test Program

# Function to display menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $3.75")
    print("3. Nachos - $4.25")
    print("4. Soft Drink - $1.20")
    print("5. Quit")


# Function to get the price of an item
def get_price(choice):
    prices = {
        1: 2.50,
        2: 3.75,
        3: 4.25,
        4: 1.20
    }
    return prices.get(choice, 0)


# Function to get the item name
def get_item_name(choice):
    items = {
        1: "Taco",
        2: "Burrito",
        3: "Nachos",
        4: "Soft Drink"
    }
    return items.get(choice, "Unknown Item")


# Function to run a single test scenario
def run_test(inputs):
    print("Welcome to Taco Palace! Please view the menu below and make a selection.")

    ordered_items = []
    total_price = 0.0
    index = 0

    while True:
        print_menu()
        choice = inputs[index]
        print(f"Enter your choice: {choice}")
        index += 1

        if choice == 5:
            break
        elif choice in [1, 2, 3, 4]:
            item = get_item_name(choice)
            price = get_price(choice)
            ordered_items.append(item)
            total_price += price
            print(f"You selected a {item}.")
        else:
            print("Invalid choice, please try again.")

    if ordered_items:
        if len(ordered_items) == 1:
            items_str = ordered_items[0]
        else:
            items_str = ", ".join(ordered_items[:-1]) + " and a " + ordered_items[-1]
        print(f"\nYou ordered {items_str}. Your total is ${total_price:.2f}")
    else:
        print("You did not order anything. Goodbye!")
    print("-" * 60)


# Main program to run all scenarios
def main():
    print("\n===== Test Case 1: Pick 1 item =====")
    run_test([1, 5])  # Taco, Quit

    print("\n===== Test Case 2: Pick 2 items =====")
    run_test([2, 4, 5])  # Burrito, Soft Drink, Quit

    print("\n===== Test Case 3: Pick 3 items =====")
    run_test([1, 3, 4, 5])  # Taco, Nachos, Soft Drink, Quit


if __name__ == "__main__":
    main()
