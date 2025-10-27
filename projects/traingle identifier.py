
def check_password():
    """Check if user enters correct password."""
    correct_password = "#A21"  # Master password
    password = input("\nEnter password to access Triangle Identifier: ")
    return password == correct_password

def is_valid_triangle(a, b, c):
    """Check if three sides can form a valid triangle."""
    # Triangle inequality theorem: sum of any two sides must be greater than third side
    return (a + b > c) and (b + c > a) and (a + c > b)

def get_positive_number(prompt):
    """Get a positive number from user with validation."""
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("Please enter a positive number")
                continue
            return num
        except ValueError:
            print("Please enter a valid number")

def main():
    """Main program with password protection."""
    print("Triangle Type Identifier")
    
    if not check_password():
        print("Incorrect password. Access denied.")
        return
    
    try:
        # Get triangle sides with validation
        side_1 = get_positive_number("Enter length of side 1 of triangle: ")
        side_2 = get_positive_number("Enter length of side 2 of triangle: ")
        side_3 = get_positive_number("Enter length of side 3 of triangle: ")
        
        # Check if triangle is valid
        if not is_valid_triangle(side_1, side_2, side_3):
            print("These sides cannot form a valid triangle!")
            return
            
        # Identify triangle type
        if side_1 == side_2 == side_3:
            print("The triangle is equilateral.")
        elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
            print("The triangle is isosceles.")
        # Check for right triangle using Pythagorean theorem
        elif any([
            abs(side_1**2 - (side_2**2 + side_3**2)) < 0.01,
            abs(side_2**2 - (side_1**2 + side_3**2)) < 0.01,
            abs(side_3**2 - (side_1**2 + side_2**2)) < 0.01
        ]):
            print("The triangle is right-angled.")
        else:
            print("The triangle is scalene.")
            
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main()