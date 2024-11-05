# Simple Calculator with Memory Functions

# Memory variable
memory = 0

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def store_memory(value):
    global memory
    memory = value
    print(f"Stored {value} in memory.")

def recall_memory():
    return memory

def clear_memory():
    global memory
    memory = 0
    print("Memory cleared.")

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Store in Memory")
        print("6. Recall Memory")
        print("7. Clear Memory")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")

        elif choice == '5':
            value = float(input("Enter a number to store in memory: "))
            store_memory(value)

        elif choice == '6':
            print(f"Recalled from memory: {recall_memory()}")

        elif choice == '7':
            clear_memory()

        elif choice == '8':
            print("Exiting the calculator.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the calculator
calculator()
