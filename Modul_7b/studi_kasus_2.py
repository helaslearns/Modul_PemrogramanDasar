def main():
    mahasiswa = [
        ("Andi", "PTIK", 80),
        ("Siti", "Informatika", 90),
        ("Budi", "PTIK", 75),
        ("Citra", "Informatika", 88)
    ]

    print("–––––––[Tabel Data Mahasiswa]–––––––")
    print(f'_'*41)
    print(f'{'|':<5}{"Nama":<15}{'|':<15}{"Jurusan":<10}{'|'}')
    print(f'_'*41)
    for items in mahasiswa:
        nama, jurusan, nilai = items
        print(f'{'|':<5}{nama:<15}{'|':<15}{jurusan:<10}{'|'}')
    print(f'_'*41)
    print(f'Jumlah mahasiswa: {len(mahasiswa)}')

    temp_mhs1 = input("Masukkan data mahasiswa baru (format: Nama,Jurusan,Nilai): ").split(",")
    temp_mhs2 = input("Masukkan data mahasiswa baru (format: Nama,Jurusan,Nilai): ").split(",")
    mahasiswa.append((temp_mhs1[0], temp_mhs1[1], int(temp_mhs1[2])))
    mahasiswa.append((temp_mhs2[0], temp_mhs2[1], int(temp_mhs2[2])))

    # Menghitung Jumlah Data Mahasiswa
    print()
    print(f'Jumlah mahasiswa: {len(mahasiswa)}')

    # Menghitung Rata-rata Nilai Mahasiswa
    total_nilai = sum(item[2] for item in mahasiswa)
    rata_rata = total_nilai / len(mahasiswa)
    print()
    print(f'Rata-rata nilai mahasiswa: {rata_rata:.2f}')

    # Menampilkan Mahasiswa dengan Nilai Tertinggi
    mahasiswa_tertinggi = max(mahasiswa, key=lambda x: x[2])
    print()
    print(f'Mahasiswa dengan nilai tertinggi: {mahasiswa_tertinggi[0]} ({mahasiswa_tertinggi[1]}) dengan nilai {mahasiswa_tertinggi[2]}')

    # Menampilkan Mahasiswa dengan Nilai Terendah
    mahasiswa_terendah = min(mahasiswa, key=lambda x: x[2])
    print()
    print(f'Mahasiswa dengan nilai terendah: {mahasiswa_terendah[0]} ({mahasiswa_terendah[1]}) dengan nilai {mahasiswa_terendah[2]}')

    # Menampilkan Tabel Mahasiswa ekslusif untuk nilai >= 80 (menggunakan tuple unpacking saat perulangan)
    print()
    print("–––––––[Tabel Mahasiswa dengan Nilai >= 80]–––––––")
    print(f'_'*41)
    print(f'{'|':<5}{"Nama":<15}{'|':<15}{"Jurusan":<10}{'|'}')
    print(f'_'*41)
    for items in mahasiswa:
        nama, jurusan, nilai = items
        if nilai >= 80:
            print(f'{'|':<5}{nama:<15}{'|':<15}{jurusan:<10}{'|'}')
    print(f'_'*41)



if __name__ == "__main__":
    main()