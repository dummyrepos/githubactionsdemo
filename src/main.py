""" This module will have calculator related functions"""

class Calculator:
    """_summary_

    Returns:
        _type_: _description_
    """
    # This method will add two numbers
    def add(self, a, b):
        """_summary_

        Args:
            a (_type_): _description_
            b (_type_): _description_

        Returns:
            _type_: _description_
        """
        return a + b

    # This method will subtract two numbers
    def subtract(self, a, b):
        """_summary_

        Args:
            a (_type_): _description_
            b (_type_): _description_

        Returns:
            _type_: _description_
        """
        return a - b

    # This method will multiply two numbers
    def multiply(self, a, b):
        """_summary_

        Args:
            a (_type_): _description_
            b (_type_): _description_

        Returns:
            _type_: _description_
        """
        return a * b

    # This method will divide two numbers
    def divide(self, a, b):
        """_summary_

        Args:
            a (_type_): _description_
            b (_type_): _description_

        Returns:
            _type_: _description_
        """
        return a / b


# This is the main function that will run the calculator
def main():
    """_summary_
    """
    # Create an instance of the Calculator class
    calc = Calculator()

    # Print the menu
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Loop until the user chooses to exit
    while choice != 5:
        # Get the two numbers from the user
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        # Perform the chosen operation
        if choice == 1:
            print("Result:", calc.add(a, b))
        elif choice == 2:
            print("Result:", calc.subtract(a, b))
        elif choice == 3:
            print("Result:", calc.multiply(a, b))
        elif choice == 4:
            print("Result:", calc.divide(a, b))
        else:
            print("Invalid choice")

        # Get the user's choice again
        choice = int(input("Enter your choice: "))

    # Print a goodbye message
    print("Goodbye!")


# This is the entry point of the program
if __name__ == "__main__":
    main()
