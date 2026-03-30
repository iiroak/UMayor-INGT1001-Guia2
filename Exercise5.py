def main():
    while(True):
        try:
            value = int(input("Ingrese un numero para la factorial: "))
            if value <= 0:
                print("La factorial no puede iniciar por 0 o menor a este.")
                continue
            factor = 1
            for index in range(1, value + 1):
                factor *= index
            print(f"Factorial: {factor}")
            return
        except ValueError:
            print("Ingresa un monto valido (esto puede ocurrir si el numero desborda el limite maximo de python)")

if __name__ == "__main__":
    main() 