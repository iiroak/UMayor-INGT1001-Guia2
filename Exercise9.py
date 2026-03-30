def main():
    while(True):
        try:
            amount = int(input("Ingresa la cantidad de notas: "))
            if amount <= 0: 
                print("Ingresa un rango de nota validas > 0")
                continue
            note = 0
            for index in range(0, amount):
                while(True):
                    try:
                        note_input = float(input(f"Ingresa la nota {index+1}: "))
                        if note_input < 1.0 or note_input > 7.0:
                            print("Ingresa una nota valida entre 1.0 y 7.0")
                            continue
                        note += note_input
                        break
                    except ValueError: 
                        print("Ingresa una cantidad valida.")
            avg_note = note/amount
            print(f"Promedio de notas {avg_note}")
            return
        except ValueError:
            print("Ingresa una cantidad valida.")

if __name__ == "__main__":
    main() 