def main():
    mahasiswa = {
        "Andi": {"prodi": "PTIK", "ipk": 3.8},
        "Siti": {"prodi": "Informatika", "ipk": 3.9},
        "Budi": {"prodi": "PTIK", "ipk": 3.6}
    }

    print("\n===== DATA MAHASISWA =====")
    print(f"{'Nama':<10} | {'Prodi':<11} | {'IPK'}")
    for key, value in mahasiswa.items():
        print(f"{key:<10} | {value['prodi']:<11} | {value['ipk']}")

    print("\n===== DATA TERTINGGI DAN TERENDAH =====")
    tertinggi = max(mahasiswa.items(), key=lambda x: x[1]['ipk'])
    terendah = min(mahasiswa.items(), key=lambda x: x[1]['ipk'])
    print(f"Mahasiswa dengan IPK tertinggi: {tertinggi[0]} ({tertinggi[1]['ipk']})")
    print(f"Mahasiswa dengan IPK terendah: {terendah[0]} ({terendah[1]['ipk']})")

    prodi_dict = {}
    for key, value in mahasiswa.items():
        prodi = value['prodi']
        ipk = value['ipk']
        if prodi in prodi_dict:
            prodi_dict[prodi].append(ipk)
        else:
            prodi_dict[prodi] = [ipk]

    print("\n===== RATA-RATA IPK PER PRODI =====")
    for prodi, ipk_list in prodi_dict.items():
        rata_rata = sum(ipk_list) / len(ipk_list)
        print(f"{prodi:<11} | {rata_rata:.2f}")

if __name__ == "__main__":
    main()