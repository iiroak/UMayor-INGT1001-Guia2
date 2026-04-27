def main():
    while(True):
        try:
            age = int(input("Ingresa tu edad: "))
            print(f"Tu edad es {age}")
            return
        except ValueError:
            print("Ingresa un numero valido.")

if __name__ == "__main__":
    main()