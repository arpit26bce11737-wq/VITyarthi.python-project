from menu_display import show_menu
from order_processing import take_order
from billing_and_payment import generate_bill

# Get user input first, just like the original script
name = input("Name Please : ")

# Display the menu
show_menu()

# Process the order
bill, ordered_items = take_order()

# Process billing and payments
generate_bill(name, bill, ordered_items)