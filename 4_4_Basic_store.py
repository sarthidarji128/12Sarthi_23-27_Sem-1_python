class Store:
  """
  Represents a store with products and the ability to generate bills.
  """

  def __init__(self):
    """
    Initializes a Store object with a dictionary of products.
    """

    self.products = {
      "101": {"name": "Pen", "price": 50},
      "102": {"name": "Notebook", "price": 22},
      "103": {"name": "Pencil", "price": 33},
      "104": {"name": "Eraser", "price": 22},
    }

  def display_menu(self):
    """
    Prints a list of available products with their codes and prices.
    """

    print("Product Menu:")
    for code, product in self.products.items():
      print(code, ":", product['name'], "$", product['price'])

  def generate_bill(self):
    """
    Generates a bill based on user-provided quantities for each product.
    """

    total_amount = 0  # Initialize the total bill amount

    print("\nEnter quantity for each item (or 0 to skip):")

    for code, product in self.products.items():
      quantity = int(input(f"{code} ({product['name']}): "))

      if quantity > 0:  # Only calculate if quantity is not zero
        item_amount = product["price"] * quantity  # Calculate item cost
        print(f"{product['name']} x {quantity}: ${item_amount:.2f}")
        total_amount += item_amount  # Add item cost to total bill

    print("\nTotal Amount: $", total_amount)  # Print the final bill amount

# Create a store object and run its methods
store = Store()
store.display_menu()
store.generate_bill()
