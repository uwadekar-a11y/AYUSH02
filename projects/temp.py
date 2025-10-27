def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def get_valid_temperature(prompt: str) -> float:
    """Get valid temperature input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")

def check_password() -> bool:
    """Check if user enters correct password."""
    correct_password = "#A21"  # You can change this to your desired password
    password = input("Enter password to access Temperature Converter: ")
    return password == correct_password

def main():
    """Temperature conversion program."""
    print("Temperature Converter\n1. C to F\n2. F to C")
    
    if not check_password():
        print("Incorrect password. Access denied.")
        return
        
    try:
        choice = input("Select (1/2): ")
        if choice == "1":
            c = get_valid_temperature('Celsius: ')
            f = celsius_to_fahrenheit(c)
            print(f'{c}°C = {f:.1f}°F')
        elif choice == "2":
            f = get_valid_temperature('Fahrenheit: ')
            c = fahrenheit_to_celsius(f)
            print(f'{f}°F = {c:.1f}°C')
        else:
            print("Invalid choice (1 or 2)")
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main()
