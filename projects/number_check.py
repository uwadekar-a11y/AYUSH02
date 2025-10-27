def check_password() -> bool:
    """Check if user enters correct password."""
    correct_password = "#A21"  # You can change this to your desired password
    password = input("Enter password to access Number Analyzer: ")
    return password == correct_password

def main():
    print("Number Analyzer")
    
    if not check_password():
        print("Incorrect password. Access denied.")
        return
        
    try:
        while True:
            try:
                n = float(input("Enter a number: "))
                t = "positive" if n > 0 else "negative" if n < 0 else "zero"
                print(f"Type: {t}")
                print(f"Absolute value: {abs(n)}")
                print("Category: integer" if n.is_integer() else f"Category: decimal (rounded to {round(n,2)})")
                break
            except ValueError:
                print("Enter a valid number.")
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main()
