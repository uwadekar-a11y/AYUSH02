
def check_password():
    """Check if user enters correct password."""
    correct_password = "#A21"  # Master password
    password = input("\nEnter password to access Divisibility Checker: ")
    return password == correct_password

def main():
    """Main program with password protection."""
    print("Divisibility Checker")
    
    if not check_password():
        print("Incorrect password. Access denied.")
        return
        
    try:
        num = int(input('Enter a number: '))
        # Check for both divisibility first
        if (num % 2 == 0) and (num % 3 == 0):
            print('{} is divisible by both 2 and 3'.format(num))
        # Then check individual cases
        elif num % 2 == 0:
            print('{} is divisible by 2'.format(num))
        elif num % 3 == 0:
            print('{} is divisible by 3'.format(num))
        else:
            print('{} is not divisible by either 2 or 3'.format(num))
    except ValueError:
        print("Please enter a valid integer")
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main()