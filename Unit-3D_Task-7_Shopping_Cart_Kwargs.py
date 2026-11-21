def shopping_cart(____):  # **products
    total = ____
    print("Items Purchased:")
    for item, price in ____.items():
        print(f"{item}: ₹{price}")
        total = ____
    print(f"Total: ₹{total}")

# multiple keyword arguments
shopping_cart(apple=____, orange=____, mango=____)  # 15, 12, 10