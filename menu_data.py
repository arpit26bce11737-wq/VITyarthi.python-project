MENU = {
    1: {"name": "Combo Shahi Thali", "price": 600},
    2: {"name": "Masala papad", "price": 15},
    3: {"name": "Dhokla", "price": 60},
    4: {"name": "Sweet Corn Chaat", "price": 90},
    5: {"name": "Masala Peanuts", "price": 70},
    6: {"name": "Steamed Momos", "price": 50},
    7: {"name": "Aloo Tikki", "price": 120},
    8: {"name": "Veg Soup", "price": 70},
    9: {"name": "Egg Bhurji", "price": 110},
    10: {"name": "Chicken Steam Momos", "price": 180},
    11: {"name": "Chicken Soup", "price": 120},
    12: {"name": "Veg Plain Rice", "price": 180},
    13: {"name": "Biryani", "price": 200},
    14: {"name": "Tandoor Roti", "price": 180},
    15: {"name": "Aloo Paratha", "price": 120},
    16: {"name": "Medu Vada", "price": 90},
    17: {"name": "Rava Dosa", "price": 150},
    18: {"name": "Jalebi", "price": 50},
    19: {"name": "Rasmalai", "price": 90},
    20: {"name": "Apple Juice", "price": 40},
    21: {"name": "Sweet Lassi", "price": 70},
    22: {"name": "Cold Coffee", "price": 100},
    23: {"name": "Masala Chai", "price": 50},
    24: {"name": "Fresh Lime Soda", "price": 80},
    25: {"name": "Mango Lassi", "price": 100},
    26: {"name": "Hara Bhara Kabab", "price": 180},
    27: {"name": "Paneer Tikka", "price": 280},
    28: {"name": "Veg Spring Roll", "price": 160},
    29: {"name": "French Fries", "price": 140},
    30: {"name": "Chilli Paneer", "price": 260},
    31: {"name": "Veg Manchurian", "price": 220},
    32: {"name": "Honey Chilli Potato", "price": 200},
    33: {"name": "Kadhai Paneer", "price": 280},
    34: {"name": "Shahi Paneer", "price": 300},
    35: {"name": "Mix Veg", "price": 220},
    36: {"name": "Butter Naan", "price": 70},
    37: {"name": "Garlic Naan", "price": 90},
    38: {"name": "Plain Naan", "price": 50},
    39: {"name": "Laccha Paratha", "price": 80},
    40: {"name": "Jeera Rice", "price": 180},
    41: {"name": "Dal Tadka", "price": 190},
    42: {"name": "Veg Pulao", "price": 200},
    43: {"name": "Hyderabadi Biryani", "price": 350},
    44: {"name": "Tandoori Platter", "price": 550},
    45: {"name": "Paneer Roll", "price": 180},
    46: {"name": "Veg Sandwich", "price": 150},
    47: {"name": "Veg Burger", "price": 180},
    48: {"name": "Pizza", "price": 350},
    49: {"name": "Ice Cream", "price": 100},
    50: {"name": "Brownie", "price": 180}
}

# Function to get food name
def food_name(n):
    if n in MENU:
        return MENU[n]["name"]
    return "NOT AVAILABLE"

# Function to get price
def price(n):
    if n in MENU:
        return MENU[n]["price"]
    return 0
