import re
def main():
    while(True):
        phrase = input("Ingresa la frase: ")
        if len(phrase) <= 0 or len(phrase.strip(" ")) <= 0:
            print("Debes ingresar una frase: ")
        else:
            counter = 0
            for word in phrase:
                if re.search("[aeiouAEIOU]", word):
                    counter += 1
            print(f"vocales: {counter}")
            return
if __name__ == "__main__":
    main()