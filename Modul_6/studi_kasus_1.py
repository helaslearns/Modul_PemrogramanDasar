def main():
    mahasiswa = []

    while True:
        temp_nama = input("Masukkan nama mahasiswa: ")
        temp_prodi = input("Masukkan prodi mahasiswa: ")
        temp_ipk = float(input("Masukkan IPK mahasiswa: "))

        mahasiswa.append([temp_nama, temp_prodi, temp_ipk])

        print("Lanjut input?")
        lanjut = input("Masukkan 'y' untuk lanjut, atau 'n' untuk berhenti: ")
        if lanjut.lower() == 'n':
            break

        print() 

    # Menampilkan tabel 
    print("\n===== DATA MAHASISWA =====")
    for i, mhs in enumerate(mahasiswa, start=1):
        print(f"{i}. {mhs[0]:<10} | {mhs[1]:<11} | {mhs[2]}")
    print() 

    tertinggi = max(mahasiswa, key=lambda x: x[2])
    terendah = min(mahasiswa, key=lambda x: x[2])
    
    # Rata-rata IPK setiap prodi yang sama
    prodi_dict = {}
    for mhs in mahasiswa:
        prodi = mhs[1] 
        ipk = mhs[2]
        if prodi in prodi_dict:
            prodi_dict[prodi].append(ipk)
        else:
            prodi_dict[prodi] = [ipk]
    
    for prodi, ipk_list in prodi_dict.items():
        rata_rata = sum(ipk_list) / len(ipk_list)
        print(f"Rata-rata IPK {prodi}: {rata_rata:.2f}")
        
    print(f"IPK Tertinggi: {tertinggi[0]} ({tertinggi[2]})")
    print(f"IPK Terendah : {terendah[0]} ({terendah[2]})")

if __name__ == "__main__":
    main()