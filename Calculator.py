import math
class Calculator():
    def add(*args):
        total = 0
        for num in args:
            total += num
        return total

    def subtract(*args):
        if not args:
            return 0
        result = args[0]  # Initialize result with the first operand
        for num in args[1:]:  # Iterate over remaining operands
            result -= num  # Subtract each operand from the result
        return result

    def multiply(*args):
        total = 1
        for num in args:
            total *= num
        return total

    def divide(*args):
        if 0 in args[1:]:
            raise ValueError("Cannot divide by zero")
        result = args[0]
        for num in args[1:]:  # Iterate over remaining operands
            result /= num  # Divide the result by each operand
        return result

    def square_root(number):
        if number < 0:
            raise ValueError("Square root of a negative number is not defined")
        return math.sqrt(number)

    def power(args):
        result = args[0]  # Initialize result with the first operand
        for i in args[1:]:  # Iterate over remaining operands
            result = math.pow(result, i)  # Raise result to the power of each operand
        return result

    def startup(self):
            print("Welcome to Calculator!")
            while True:
                print("\nChoose an operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Square Root")
                print("6. Power")
                print("7. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    nums = list(map(float, input("Enter numbers to add (separated by space): ").split()))
                    print("Result:", Calculator.add(*nums))
                elif choice == 2:
                    nums = list(map(float, input("Enter numbers to subtract (separated by space): ").split()))
                    print("Result:", Calculator.subtract(*nums))
                elif choice == 3:
                    nums = list(map(float, input("Enter numbers to multiply (separated by space): ").split()))
                    print("Result:", Calculator.multiply(*nums))
                elif choice == 4:
                    nums = list(map(float, input("Enter numbers to divide (separated by space): ").split()))
                    print("Result:", Calculator.divide(*nums))
                elif choice == 5:
                    num = float(input("Enter a number to find its square root: "))
                    print("Result:", Calculator.square_root(num))
                elif choice == 6:
                    nums = list(map(float, input("Enter base and exponent (separated by space): ").split()))
                    print("Result:", Calculator.power(*nums))
                elif choice == 7:
                    print("Exiting Calculator. Goodbye!")
                    break
                else:
                    print("Invalid choice!")
    # Startup
c=Calculator()
c.startup()
