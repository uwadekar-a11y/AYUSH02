def check_password() -> bool:
    """Check if user enters correct password."""
    correct_password = "1234"  # You can change this to your desired password
    password = input("Enter password to access calculator: ")
    return password == correct_password

def main():
    print("Even/Odd Checker")
    if not check_password():
        print("Incorrect password. Access denied.")
        return
        
    try:
        while True:
            try:
                n = int(input("Enter a number: "))
                print(f"{n} is even" if n % 2 == 0 else f"{n} is odd")
                break
            except ValueError:
                print("Enter a valid integer.")
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main()
