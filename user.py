def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after discount if the discount is 20% or more; otherwise, the original price
    """
    if discount_percent >= 20:
        # Apply the discount
        final_price = price * (1 - discount_percent / 100)
    else:
        # Return the original price if the discount is less than 20%
        final_price = price
    
    return final_price

def main():
    # Prompt the user to enter the original price
    price = float(input("Enter the original price of the item: "))
    
    # Prompt the user to enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price
    print(f"The final price after applying the discount is: ${final_price:.2f}")

if _name_ == "_main_":
    main()