def check_password():
    """Check if user enters correct password."""
    correct_password = "#A21"  # Master password
    password = input("\nEnter password to access Number Counter: ")
    return password == correct_password

def main():
    """Main program with password protection."""
    print("Number Counter (-1 to exit)")
    
    if not check_password():
        print("Incorrect password. Access denied.")
        return
        
    pos = neg = zero = 0  # Initialize counters

    try:
        while True:
            try:
                n = int(input("Enter number: "))
                if n == -1:
                    break
                elif n > 0:
                    pos += 1
                elif n < 0:
                    neg += 1
                else:
                    zero += 1
            except ValueError:
                print("Enter valid number")
                
        print(f"\nResults:\nPositive: {pos}\nNegative: {neg}\nZeros: {zero}")
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main()