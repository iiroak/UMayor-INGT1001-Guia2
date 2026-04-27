import re

def main():
    password = input("Ingresa tu contraseña: ")
    haveNumber = re.search("[0-9]", password)
    haveLetter = re.search("[a-zA-Z]", password)
    if len(password) <= 8 or not haveLetter or not haveNumber:
        print("Contraseña Debil")
    else:
        print("Contraseña Segura")

if __name__ == "__main__":
    main() 