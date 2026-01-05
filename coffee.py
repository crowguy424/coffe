class Coffee:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    #intialize order
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Add {coffee.name} to your order")

    #Calculate total price
    def total(self):
        return sum(item.price for item in self.items)

    #show order summary
    def show_order(self):
        if not self.items:
            print("No items added to your order")
            return
        print("\nYour order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total()}\n")

        #handle checkout process
        def checkout(self):
            if not self.items:
                print("Your cart is empty.")
                return
            self.show_order()
            confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Order confirmed! Thank you for your order.")
                self.items.clear()
            else:
                print("Order cancelled.")

# display menu and handle user input

def main():
    menu = [
        Coffee(name="Black Coffee Small", price=1.5),
        Coffee(name="Black Coffee Medium", price=1.92),
        Coffee(name="Black Coffee Large", price=2.04),
        Coffee(name="Espresso Medium", price=2.04),
        Coffee(name="Espresso Large", price=3.12),
        Coffee(name="Latte Medium", price=2.12),
        Coffee(name="Latte Large", price=3.13),
        Coffee(name="Cappuccino Medium", price=3.00),
        Coffee(name="Cappuccino Large", price=4.00),
        Coffee(name="Americano Medium", price=3.00),
        Coffee(name="Cappuccino Large", price=4.00),

    ]
    order = Order()
    #User Interaction
    while True:
        print("\n--- Coffee Menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) - 1])
        elif choice == '5':
            order.show_order()
        elif choice == '6':
            order.checkout()
        elif choice == '7':
            print("Thank you for your order. Have a nice day :)!")
            break
        else:
            print("Invalid choice. Please try again.")
    if __name__ == "__main__":
        main()


