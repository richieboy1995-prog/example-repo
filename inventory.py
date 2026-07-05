
# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        # The below code initialise's
        # the attributes in the def __init__ function.

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass

    def get_cost(self):
        # code to return the cost of the shoe
        return self.cost

    def get_quantity(self):
        # code to return the quantity of the shoes
        return self.quantity
        pass

    def __str__(self):
        # returns a string representation of the class
        return (
            f"{self.country} | {self.code} | {self.product} | "
            f"Cost: {self.cost} | Qty: {self.quantity}"
        )


# =============Shoe list===========

shoe_list = []
# this shoe_list will store the list of shoes

# ==========Functions outside the class==============


def read_shoes_data():
    # this opens the txt file and reads it
    # It will skip the header as requested
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip header line
            for line_number, line in enumerate(file, start=2):
                line = line.strip()
                if not line:
                    continue

                parts = [part.strip() for part in line.split(",")]
                if len(parts) != 5:
                    print(f"Skipping invalid line {line_number}: {line}")
                    continue

                country, code, product, cost, quantity = parts
                try:
                    # appending the options into shoe list
                    shoe_list.append(
                        Shoe(country, code, product, int(cost), int(quantity))
                    )
                # Below I'll use a couple except concepts to
                # Make sure there aren't any errors
                except ValueError as error:
                    print(f"Error parsing line {line_number}: {error}")
    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as error:
        print(f"Unexpected error reading inventory.txt: {error}")


def capture_shoes():
    # This function will allow a user to capture data
    # about a shoe and use this data to create a shoe object
    # and append this object inside the shoe list.
    country = input("Enter country: ").strip()
    code = input("Enter shoe code: ").strip()
    product = input("Enter product name: ").strip()

    while True:
        cost_input = input("Enter cost: ").strip()
        try:
            cost = int(cost_input)
            break
        except ValueError:
            print("Please enter a valid integer cost.")

    while True:
        quantity_input = input("Enter quantity: ").strip()
        try:
            quantity = int(quantity_input)
            break
        except ValueError:
            print("Please enter a valid integer quantity.")

    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print("Shoe added successfully.")


def view_all():
    # This function will iterate over the shoes list and
    # print the details of the shoes returned from the __str__
    # function
    if not shoe_list:
        print("No shoes available.")
        return

    print("All shoes:")
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    # This function will find the shoe object with the lowest quantity,
    # which is the shoes that need to be re-stocked. Ask the user if they
    # want to add this quantity of shoes and then update it.
    # This quantity should be updated on the file for this shoe.
    # There will also be except functions in place for any errors.
    if not shoe_list:
        print("No shoes available to restock.")
        return

    lowest_stock_shoe = min(shoe_list, key=lambda s: s.quantity)
    print("Shoe with lowest quantity:")
    print(lowest_stock_shoe)

    answer = input("Add more stock? (y/n): ").strip().lower()
    if answer != "y":
        return

    while True:
        addition = input("Enter quantity to add: ").strip()
        try:
            addition_value = int(addition)
            if addition_value < 0:
                raise ValueError("Quantity must be non-negative.")
            break
        except ValueError:
            print("Please enter a valid non-negative integer.")

    lowest_stock_shoe.quantity += addition_value
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost},{shoe.quantity}\n"
                )
        print("Stock updated successfully.")
    except Exception as error:
        print(f"Failed to update inventory file: {error}")


def search_shoe():
    # This function will search for a shoe from the list
    # using the shoe code and return this object so that it will be printed.
    code = input("Enter shoe code to search: ").strip()
    for shoe in shoe_list:
        if shoe.code.lower() == code.lower():
            print(shoe)
            return shoe

    print(f"Shoe with code '{code}' not found.")
    return None


def value_per_item():
    # This function will calculate the total value for each item
    # i added a if not shoe_list in case there is a issue.
    if not shoe_list:
        print("No shoes available.")
        return

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: {shoe.quantity} x {shoe.cost} = {value}")


def highest_qty():
    # Write code to determine the product with the highest quantity and
    # print this shoe as being for sale.
    if not shoe_list:
        print("No shoes available.")
        return

    highest_stock_shoe = max(shoe_list, key=lambda s: s.quantity)
    # using key=lambda to customize how the highest_stock_shoe
    # get evaluated and sorted (loved reading up on this function)
    print("Shoe with highest quantity (for sale):")
    print(highest_stock_shoe)

# ==========Main Menu=============


def main():
    # This will be the main menu for the user
    # I thought of using a almost super mario intro
    # with ("\n" + "="*50)
    # I created a menu that uses all the above code
    # to create a easy reading and user friendly menu
    read_shoes_data()  # Load existing shoes from file

    while True:
        print("\n" + "="*50)
        print("       SHOE INVENTORY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. View All Shoes")
        print("2. Add New Shoe")
        print("3. Search Shoe by Code")
        print("4. Restock Shoes")
        print("5. View Total Value per Item")
        print("6. View Shoe with Highest Quantity (For Sale)")
        print("7. Exit")
        print("="*50)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- ALL SHOES ---")
            view_all()
        elif choice == "2":
            print("\n--- ADD NEW SHOE ---")
            capture_shoes()
        elif choice == "3":
            print("\n--- SEARCH SHOE ---")
            search_shoe()
        elif choice == "4":
            print("\n--- RESTOCK SHOES ---")
            re_stock()
        elif choice == "5":
            print("\n--- TOTAL VALUE PER ITEM ---")
            value_per_item()
        elif choice == "6":
            print("\n--- HIGHEST QUANTITY FOR SALE ---")
            highest_qty()
        elif choice == "7":
            print("\nThank you for using the Shoe Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


# Run the main menu
if __name__ == "__main__":
    main()
