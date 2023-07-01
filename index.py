def display_inventory(items_inventory):
    print("\nSnack Inventory:")
    for snack, quantity in items_inventory.items():
        print(f"{snack}: {quantity}")


def add_snack(inventory):
    snack = input("\nEnter the snack name: ")
    quantity = input("Enter the quantity: ")
    try:
        quantity = int(quantity)
        inventory[snack] = quantity
        print(f"{snack} added successfully!")
    except ValueError:
        print("Invalid quantity. Please enter a valid integer.")


def update_snack(inventory):
    snack = input("\nEnter the snack name to update: ")
    if snack in inventory:
        quantity = input("Enter the new quantity: ")
        try:
            quantity = int(quantity)
            inventory[snack] = quantity
            print(f"{snack} quantity updated successfully!")
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")
    else:
        print("Snack not found in the inventory.")


def delete_snack(inventory):
    snack = input("\nEnter the snack name to delete: ")
    if snack in inventory:
        del inventory[snack]
        print(f"{snack} deleted successfully!")
    else:
        print("Snack not found in the inventory.")


def record_sale(sales, snack, inventory):
    if snack in inventory:
        if inventory[snack] > 0:
            sales[snack] = sales.get(snack, 0) + 1
            inventory[snack] -= 1
            print("Sale recorded successfully!")
        else:
            print("Snack is not available.")
    else:
        print("Snack not found in the inventory.")


def main_section():
    inventory_lists = {"Samosa": 10, "Biscuits": 15, "Dhosa": 5}
    sale_data = {}

    while True:
        print("\nMenu:")
        print("1. Display Inventory")
        print("2. Add Snack")
        print("3. Update Snack Quantity")
        print("4. Delete Snack")
        print("5. Sale Record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_inventory(inventory_lists)
        elif choice == "2":
            add_snack(inventory_lists)
        elif choice == "3":
            update_snack(inventory_lists)
        elif choice == "4":
            delete_snack(inventory_lists)
        elif choice == "5":
            snack = input("\nEnter the snack name: ")
            record_sale(sale_data, snack, inventory_lists)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting the program.")


if __name__ == "__main__":
    main_section()
