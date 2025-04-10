def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to be applied.

  Returns:
    The final price after applying the discount, or the original price if
    the discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get user input
try:
  original_price = float(input("Enter the original price of the item: "))
  discount_percentage = float(input("Enter the discount percentage: "))

  # Calculate and print the final price
  final_price = calculate_discount(original_price, discount_percentage)
  if final_price == original_price:
    print(f"No discount applied. The final price is: R{final_price:.2f}")
  else:
    print(f"The final price after applying the discount is: R{final_price:.2f}")

except ValueError:
  print("Invalid input. Please enter numeric values for price and discount percentage.")