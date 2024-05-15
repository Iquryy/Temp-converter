def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32) * 5 / 9

def celsius_to_fahrenheit(c_temp):
    return (c_temp * 9 / 5) + 32

def main():
    print("Temperatūras Pārveidotājs")
    while True:
        choice = input("Pārveidot no Fārenheita (F) uz Celsiju (C) [F/C]: ")
        if choice.upper() == 'F':
            f_temp = float(input("Ievadiet temperatūru Fārenheita grādos: "))
            print(f"{f_temp}°F ir {fahrenheit_to_celsius(f_temp):.2f}°C")
            break
        elif choice.upper() == 'C':
            c_temp = float(input("Ievadiet temperatūru Celsija grādos: "))
            print(f"{c_temp}°C ir {celsius_to_fahrenheit(c_temp):.2f}°F")
            break
        else:
            print("Nederīga izvēle. Lūdzu izvēlieties 'F' vai 'C'.")

if __name__ == "__main__":
    main()
