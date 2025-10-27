"""Celsius to Kelvin converter (K = C + 273.15)"""

def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def get_valid_temperature() -> float:
    """Get valid temperature input."""
    while True:
        try:
            temp = float(input('Celsius: '))
            if temp >= -273.15:  # Check for absolute zero
                return temp
            print("Error: Below absolute zero (-273.15°C)")
        except ValueError:
            print("Enter a valid number")

def check_password() -> bool:
    """Check if user enters correct password."""
    correct_password = "#A21"  # You can change this to your desired password
    password = input("Enter password to access Temperature Converter: ")
    return password == correct_password

def main():
    """Temperature conversion program."""
    print("Celsius to Kelvin Converter")
    
    if not check_password():
        print("Incorrect password. Access denied.")
        return
        
    try:
        celsius = get_valid_temperature()
        kelvin = celsius_to_kelvin(celsius)
        print(f'{celsius}°C = {kelvin:.2f}K')
        
        # Show reference points
        if celsius in [0, 100, -273.15]:
            points = {0: "water freezes", 100: "water boils", -273.15: "absolute zero"}
            print(f"Note: {celsius}°C is where {points[celsius]}")
            
    except KeyboardInterrupt:
        print("\nProgram terminated")

if __name__ == "__main__":
    main() 