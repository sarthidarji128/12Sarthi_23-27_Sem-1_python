class Store:
    def __init__(self):
       self.products = {
            "101": {"name": "Pen", "price": 50},
            "102": {"name": "Notebook", "price":22},
            "103": {"name": "Pencil", "price": 33},
            "104": {"name": "Eraser", "price": 22},
        }

    def display_menu(self):
        print("Product Menu:")
        for code, product in self.products.items():
            print(code ,":",product['name'],"$",product['price'])

    def generate_bill(self):
        total_amount = 0
        print("\nEnter quantity for each item (or 0 to skip):")
        for code, product in self.products.items():
            quantity = int(input(f"{code} ({product['name']}): "))
            if quantity > 0:
                item_amount = product["price"] * quantity
                print(f"{product['name']} x {quantity}: ${item_amount:.2f}")
                total_amount += item_amount

        print("\nTotal Amount: $",total_amount)

store = Store()
store.display_menu()
store.generate_bill()
