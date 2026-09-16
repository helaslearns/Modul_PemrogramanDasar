def main():
    item = []

    while True:
        temp_nama = input("Masukkan nama item: ")
        temp_harga = float(input("Masukkan harga item: "))

        item.append([temp_nama, temp_harga])

        print("Lanjut input?")
        lanjut = input("Masukkan 'y' untuk lanjut, atau 'n' untuk berhenti: ")
        if lanjut.lower() == 'n':
            break

        print()

    total = sum([i[1] for i in item])
    diskon = total * 0.1 if total > 500000 else 0
    total_setelah_diskon = total - diskon

    print(f"Total: {total}")
    print(f"Diskon: {diskon} (10%)")
    print(f"Total setelah diskon: {total_setelah_diskon}")

if __name__ == "__main__":
    main()

