# Discount Calculator

This Python script calculates the final price of an item after applying a discount. The discount is only applied if it is 20% or higher.

## How to Use

1.  **Save the code:** Save the Python code (provided in the previous response) as a `.py` file (e.g., `discount_calculator.py`).

2.  **Open a terminal or command prompt:** Navigate to the directory where you saved the file.

3.  **Run the script:** Execute the script using the Python interpreter:

    ```bash
    python discount_calculator.py
    ```

4.  **Enter input:** The script will prompt you to enter the following:
    * **Original price of the item:** Enter the initial price of the product and press Enter.
    * **Discount percentage:** Enter the discount percentage you want to apply (as a number, e.g., 25 for 25%) and press Enter.

5.  **View the result:** The script will then output the final price.
    * If the discount percentage is 20% or higher, it will display the calculated final price after the discount.
    * If the discount percentage is less than 20%, it will indicate that no discount was applied and show the original price.

## Functionality

The script uses a function called `calculate_discount(price, discount_percent)` which performs the following:

* Takes the original `price` and the `discount_percent` as input.
* Checks if the `discount_percent` is greater than or equal to 20.
* If the discount is 20% or higher:
    * Calculates the discount amount.
    * Subtracts the discount amount from the original price to get the final price.
    * Returns the final price.
* If the discount is less than 20%:
    * Returns the original price without applying any discount.

The main part of the script:

* Prompts the user for the original price and discount percentage.
* Calls the `calculate_discount()` function with the user's input.
* Prints the final price to the console, indicating whether a discount was applied or not.
* Includes basic error handling to catch `ValueError` if the user enters non-numeric input.

## Example Usage

Enter the original price of the item: 100
Enter the discount percentage: 25
The final price after applying the discount is: R75.00


Enter the original price of the item: 50
Enter the discount percentage: 10
No discount applied. The final price is: R50.00


Enter the original price of the item: abc
Invalid input. Please enter numeric values for price and discount percentage.
