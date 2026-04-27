def main():
    trys = 0
    while(True):
        pin = input("Ingresa tu pin: ")
        if pin != "9999":
            trys += 1
            print("Pin incorrecto.")
        else:
            print("INGRESO EXITOSO")
            return
        if trys == 3:
            print("Intentos excedidos.")
            print("SISTEMA BLOQUEADO")
            return
if __name__ == "__main__":
    main() 