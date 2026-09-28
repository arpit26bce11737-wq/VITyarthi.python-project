def generate_bill(name, bill, ordered_items):
    # If nothing was ordered
    if bill == 0:

        print("\nNo valid items were ordered.")
        print("Thank you for visiting!")

    else:

        # GST
        gst = bill * 0.05

        # Delivery charge
        delivery = 40

        # Final bill
        grand_total = bill + gst + delivery


        # BILL
        print("\n")
        print("════════════════════════════════════════════")
        print("              RESTAURANT BILL")
        print("════════════════════════════════════════════")

        print("Customer Name :", name)

        print("--------------------------------------------")

        print(
            "Food Name                 Qty     Price     Total"
        )

        print("--------------------------------------------")


        # Display ordered items
        for item in ordered_items:

            food = item[0]
            p = item[1]
            quantity = item[2]
            total = item[3]

            print(
                food,
                " " * max(1, 25 - len(food)),
                quantity,
                "     ₹",
                p,
                "    ₹",
                total
            )


        print("--------------------------------------------")

        print("Subtotal                         : ₹", bill)

        print("GST (5%)                         : ₹", round(gst, 2))

        print("Delivery Charge                  : ₹", delivery)

        print("--------------------------------------------")

        print(
            "GRAND TOTAL                      : ₹",
            round(grand_total, 2)
        )

        print("════════════════════════════════════════════")


        # Payment
        print("\nPAYMENT METHOD")
        print("1. Cash")
        print("2. UPI")
        print("3. Card")

        payment = input("Choose Payment Method : ")


        if payment == "1":
            
            method = "Cash"
            remaining = grand_total

            while remaining > 0:
                try:
                    amount = float(input(f"Enter Cash Amount (Remaining: ₹{round(remaining, 2)}): ₹"))
                    remaining -= amount
                    
                    if remaining > 0:
                        print(f"Payment incomplete. You still owe ₹{round(remaining, 2)}")
                        
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            
            change = abs(remaining)
            print("Change to Return : ₹", round(change, 2))


        elif payment == "2":

            method = "UPI"

            print("UPI Payment Selected.")
       
            print("              ***  ******* *****")
            print("              *** *****   ******")
            print("              ****   ****** ****")
            print("              *********   ******")
            print("              ***  *************")
            
            print("Please complete the payment.")

            print("Payment Successful!")


        elif payment == "3":

            method = "Card"

            print("Card Payment Selected.")
            print("Please complete the payment.")

            print("Payment Successful!")


        else:

            method = "Not Selected"

            print("Invalid Payment Method")


        # Final Receipt
        print("\n")
        print("════════════════════════════════════════════")
        print("               FINAL RECEIPT")
        print("════════════════════════════════════════════")

        print("Customer :", name)

        print("\nORDER DETAILS")

        for item in ordered_items:

            print(
                item[0],
                "x",
                item[2],
                "= ₹",
                item[3]
            )

        print("\nSubtotal       : ₹", bill)
        print("GST            : ₹", round(gst, 2))
        print("Delivery       : ₹", delivery)
        print("--------------------------------------------")
        print("TOTAL          : ₹", round(grand_total, 2))
        print("Payment Method :", method)

        print("════════════════════════════════════════════")
        print("       THANK YOU FOR YOUR ORDER!")
        print("       Your food will reach you soon.")
        print("════════════════════════════════════════════")
        input("\nPress Enter to exit...")
