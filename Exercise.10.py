def main():
    coffe = 1200
    while(True):
        try:
            print(f"Cantidad faltante por pagar del Cafe: ${coffe}")
            amount = int(input("Ingresa el valor de la moneda: "))
            if amount <= 0:
                print("Ingresa una moneda valida (> 0)")
                continue
            if coffe - amount > 0:
                coffe -= amount
                continue
            else:
                excedent = amount - coffe
                print(f"Tu vuelto es de: ${excedent}")
                return
        except ValueError:
            print("Ingresa una cantidad valida.")

if __name__ == "__main__":
    main() 