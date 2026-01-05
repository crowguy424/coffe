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
