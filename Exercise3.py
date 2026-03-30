def main():
    while(True):
        try:
            value = float(input("Ingresa el monto: "))
            if value <= 0:
                print("Ingresa un numero positivo y mayor que 0")
            elif value > 100000:
                discount = value * 0.85
                print(f"Descuento aplicado del 15%, Precio final {discount}")
            elif value > 50000:
                discount = value * 0.95
                print(f"Descuento aplicado del 5%, Precio final {discount}")
            else:
                print(f"Descuento no aplicado, Precio: {value}")
            return
        except ValueError:
            print("Ingresa un monto valido")

if __name__ == "__main__":
    main() 