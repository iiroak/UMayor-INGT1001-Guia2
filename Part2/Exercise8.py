def main():
    while(True):
        try:
            print("------------------------------------")
            print("Ingresa alguna de estas opciones")
            print("1. Saludar")
            print("2. Mostrar versión")
            print("3. Salir")
            print("------------------------------------")
            option = int(input("Ingresar opción: "))
            if option == 1:
                print("Buenos dias.")
            elif option == 2:
                print("2026.03.30")
            elif option == 3:
                return
            else:
                print("Ingrese una opción valida.")
        except ValueError:
            print("Ingresa una opción valida.")

if __name__ == "__main__":
    main() 