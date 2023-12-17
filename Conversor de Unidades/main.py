def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        print("\nConversor de Unidades")
        print("1. Quilometros para Milhas")
        print("2. Celsius para Fahrenheit")
        print("3. Sair")
        
        escolha = input("Escolha a conversao (1/2/3): ")

        if escolha == '1':
            km = float(input("Entre com a distancia em quilometros: "))
            miles = km_to_miles(km)
            print(f"{km} km e igual a {miles} milhas.")
        
        elif escolha == '2':
            celsius = float(input("Entre com a temperatura em Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C e igual a {fahrenheit}°F.")
        
        elif escolha == '3':
            print("A Sair do programa.")
            break

        else:
            print("Escolha invalida. Por favor, selecione 1, 2 ou 3.")

if __name__ == "__main__":
    main()
