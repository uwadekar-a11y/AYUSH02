"""Rectangle area calculator with password protection"""

def check_password() -> bool:
    """Check if user enters correct password."""
    correct_password = "#A21" \
    "1234"  # You can change this to your desired password
    password = input("Enter password to access calculator: ")
    return password == correct_password

def get_positive_number(prompt: str) -> float:
    """Get positive number from user."""
    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            print("Enter a positive number")
        except ValueError:
            print("Enter a valid number")

def main():
    """Calculate rectangle area."""
    print("Rectangle Area Calculator")
    try:
        if not check_password():
            print("Incorrect password. Access denied.")
            return
            
        length = get_positive_number('Length (cm): ')
        breadth = get_positive_number('Breadth (cm): ')
        area = length * breadth
        print(f'\nArea = {area:.2f} cm²')
                
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == '__main__':
    main()
