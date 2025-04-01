def cels_to_fahr(celsius):
    return (celsius * 9 / 5) + 32


def fahr_to_celsi(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("*"*39)
    print("\tTemperature Task_2")
    print("*" * 39)
    temp = float(input("\tEnter the temperature value: "))
    unit = input("\tEnter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    print("*" * 39)

    if unit == "C":
        converted = cels_to_fahr(temp)
        print(f"\t{temp}°C is equal to {converted:.2f}°F")
    elif unit == "F":
        converted = fahr_to_celsi(temp)
        print(f"\t{temp}°F is equal to {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")


if __name__ == "__main__":
    main()

