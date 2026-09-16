from predikat import get_predikat

def main():
    nilai = float(input("Masukkan nilai: "))
    predikat = get_predikat(nilai)
    print(f"Predikat: {predikat}")

if __name__ == "__main__":
    main()