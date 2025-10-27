def check_password() -> bool:
    """Check if user enters correct password."""
    correct_password = "#A21"  # You can change this to your desired password
    password = input("Enter password to access Month Analyzer: ")
    return password == correct_password

def get_month_name(month_number: int) -> str:
    """Return the name of the month for a given number."""
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months.get(month_number, "Invalid month number")

def main():
    """Main program function."""
    print("Month Analyzer")
    
    if not check_password():
        print("Incorrect password. Access denied.")
        return
        
    try:
        month_num = int(input("Enter a number to print the name of the month: "))
        print(get_month_name(month_num))
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main()