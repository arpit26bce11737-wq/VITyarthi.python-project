from menu_data import food_name, price

def take_order():
    # Taking order
    choice = input("\nWhat You Want! : ")

    items = choice.split()

    bill = 0

    ordered_items = []


    # Taking quantity
    for item in items:

        n = int(item)

        p = price(n)

        food = food_name(n)

        if p == 0:

            print(n, "is NOT AVAILABLE")

        else:

            quantity = int(
                input("Enter quantity for " + food + " : ")
            )

            total = p * quantity

            bill += total

            ordered_items.append(
                [food, p, quantity, total]
            )

            print(
                food,
                "Quantity:",
                quantity,
                "Total: ₹",
                total
            )
            
    return bill, ordered_items
