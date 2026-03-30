def main():
    for sector in range(1, 11):
        if sector % 3 == 0:
            continue
        print(f"procesando sector {sector}")

if __name__ == "__main__":
    main() 