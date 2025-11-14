# Beverage class
class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

# VendingMachine class
class VendingMachine:
    def __init__(self):
        # Initialize 6 beverages
        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Pepsi", 1.50),
            Beverage("Sprite", 1.25),
            Beverage("Fanta", 1.25),
            Beverage("Water", 1.00),
            Beverage("Juice", 2.00)
        ]

    def display_beverages(self):
        print("\nAvailable Beverages:")
        for i, bev in enumerate(self.beverages, start=1):
            print(f"{i}. {bev}")

    def vend(self, choice, money):
        if choice < 1 or choice > len(self.beverages):
            print("Invalid selection. Please choose a valid beverage number.")
            return False

        beverage = self.beverages[choice - 1]

        if money < beverage.price:
            print(f"Insufficient money. {beverage.name} costs ${beverage.price:.2f}. Please insert more money.")
            return False
        else:
            change = money - beverage.price
            print(f"Vending {beverage.name}... Enjoy!")
            if change > 0:
                print(f"Returning change: ${change:.2f}")
            return True

    def simulate_run(self, actions):
        print("Welcome to the Python Vending Machine!")
        for choice, money in actions:
            self.display_beverages()
            print(f"\nSelect a beverage (1-6): {choice}")
            print(f"Insert money: ${money:.2f}")
            self.vend(choice, money)

# Simulated user actions: (choice, money)
simulated_actions = [
    (3, 1.25),   # Exact money
    (1, 1.00),   # Not enough money
    (6, 5.00),   # More than needed
    (9, 2.00),   # Invalid selection
]

# Run simulation
if __name__ == "__main__":
    machine = VendingMachine()
    machine.simulate_run(simulated_actions)