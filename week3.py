def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100) if discount_percent >= 20 else price

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

print(f"Final price: {calculate_discount(price, discount_percent):.2f}")
