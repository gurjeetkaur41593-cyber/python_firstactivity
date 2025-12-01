def convert_temperature(user_input):
    # Validation: input must be at least 2 characters (e.g., F51, C11)
    if len(user_input) < 2:
        return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

    prefix = user_input[0]        # First character (C or F)
    number_part = user_input[1:]  # Remaining part (should be a number)

    # Ensure temperature is numeric
    if not number_part.isdigit():
        return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

    temp_value = float(number_part)

    # Fahrenheit to Celsius
    if prefix == "F":
        celsius = (temp_value - 32) * 5/9
        return f"{user_input} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius"

    # Celsius to Fahrenheit
    elif prefix == "C":
        fahrenheit = (temp_value * 9/5) + 32
        return f"{user_input} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit"

    # Invalid prefix
    else:
        return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."


# -----------------------------
# Main program
# -----------------------------
user_input = input("Enter temperature (e.g., F51 or C20): ")
print(convert_temperature(user_input))
