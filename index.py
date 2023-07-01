def displayInventories(itemsInventory):
    print("\nSnack Inventory:")
    for allSnacks, quantityOfSnack in itemsInventory.items():
        print(f"{allSnacks}: {quantityOfSnack}")


def record_sale(sales, snack):
    if snack in sales:
        sales[snack] += 1
    else:
        sales[snack] = 1


def mainSection():
    inventoryLists = {"Samosa": 10, "Biscuits": 15, "Dhosa": 5}
    saleData = {}

    while True:
        print("\nMenu:")
        print("1. Display Inventory")
        print("2. Sale Record")
        print("3. Exit")

        choices = input("Enter your choice (1-3): ")

        if choices == "1":
            displayInventories(inventoryLists)
        elif choices == "2":
            snack = input("Enter the snack name: ")
            if snack in inventoryLists:
                record_sale(saleData, snack)
                inventoryLists[snack] -= 1
                print("Sale recorded successfully!")
            else:
                print("Snack not available in the inventory.")
        elif choices == "3":
            break
        else:
            print("Invalid choice. Please try again.")
    print("Exiting the program.")


if __name__ == "__main__":
    mainSection()
