
'''SMARTSTOCK — Supermarket Inventory Management System'''

class Product:
    '''Each product stores its own information and stock quantities.'''

    def __init__(self, name, code, shelf, backstock):
        self.name = name
        self.code = code
        self.shelf = shelf
        self.backstock = backstock

    def total_stock(self):
        return self.shelf + self.backstock

    def quantity_sold(self, no_of_units):
        '''Selling products reduces shelf stock.'''
        if no_of_units <= 0:
            print("Enter a positive quantity.")
        elif no_of_units > self.shelf:
            print("Not enough shelf stock!")
        else:
            self.shelf -= no_of_units
            print(f"Sold {no_of_units} units of {self.name}")

    def replenish(self, quantity):
        '''Move products from backstock onto the shelf.'''
        if quantity <= 0:
            print("Enter a positive quantity.")
        elif quantity > self.backstock:
            print("Not enough backstock!")
        else:
            self.shelf += quantity
            self.backstock -= quantity
            print(f"Replenished {quantity} units of {self.name}")

    def delivery(self, quantity):
        '''New deliveries increase backstock.'''
        if quantity <= 0:
            print("Enter a positive quantity.")
        else:
            self.backstock += quantity
            print(f"Received {quantity} units of {self.name}")

    def check_stock(self):
        '''Display the latest stock information.'''
        print(
            f"Product Name: {self.name}",
            f"Product Code: {self.code}",
            f"Shelf Stock: {self.shelf}",
            f"Backstock: {self.backstock}",
            f"Total Stock: {self.total_stock()}",
            sep="\n"
        )

        if self.total_stock() < 10:
            print("WARNING: Low stock!")


'''Create product objects.'''

milk = Product("Whole Milk", 1001, 20, 40)
bread = Product("White Bread", 1002, 15, 25)
eggs = Product("Free Range Eggs", 1003, 10, 30)


'''Store all products together for searching.'''

inventory = {
    milk.code: milk,
    bread.code: bread,
    eggs.code: eggs
}


'''The menu lets supermarket staff manage inventory.'''

while True:
    print("\n===== SMARTSTOCK =====")
    print("1. View all products")
    print("2. Search product")
    print("3. Sell product")
    print("4. Replenish shelf")
    print("5. Receive delivery")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "6":
        print("Thank you for using SmartStock!")
        break

    if choice == "1":
        for product in inventory.values():
            print()
            product.check_stock()

    elif choice in ["2", "3", "4", "5"]:
        try:
            code = int(input("Enter product code: "))
        except ValueError:
            print("Invalid product code!")
            continue

        if code not in inventory:
            print("Product not found!")
            continue

        product = inventory[code]

        if choice == "2":
            product.check_stock()
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity!")
            continue

        if choice == "3":
            product.quantity_sold(quantity)

        elif choice == "4":
            product.replenish(quantity)

        elif choice == "5":
            product.delivery(quantity)

        product.check_stock()

    else:
        print("Invalid option. Try again.")
