
def add(data: list):
    temp = {}
    temp_nip = str(input("Masukkan NIP: "))
    temp_nama = str(input("Masukkan Nama: "))
    temp_nama = str(input("Masukkan Jabatan: "))
    temp_gaji = float(input("Masukkan Gaji: "))

    data.append(temp)
    print(f'Data Pegawai Berhasil Ditambahkan!')

def show(data: list):
    print(f"{'NIP':<15} | {'NAMA':<15} | {'JABATAN':<15} | {'GAJI':<15}")
    for item in data:
        for key, value in item.items():
            print(f'{value}', end="\t"*2)
        print()

def modify(data: list, NIP):
    nip = input(f'Masukkan NIP: ')
    for item in data:
        for key, value in item.items():
            if key == NIP and value == nip:
                pass
    
def main():
    pegawai = [
        {"nip": "PG001", "nama": "Rina", "jabatan": "Staf Administrasi", "gaji": 4500000},
        {"nip": "PG002", "nama": "Budi", "jabatan": "Manajer", "gaji": 8500000}
    ]

    while True:
        print(f'––––––––––[MENU]––––––––––')
        print(f'1. Tambah Data Pegawai')
        print(f'2. Tampilkan Seluruh Data')
        print(f'3. Modifikasi Data berdasarkan NIP')
        print(f'4. Hapus Data Pegawai')
        print(f'5. Hitung Rata-rata Gaji')
        print(f'0. Exit')

        opsi = int(input(f'Masukkan pilihan: '))

        match opsi:
            case 1:
                add(pegawai)
                continue
            case 2:
                show(pegawai)
                continue
            case 3:
                continue
            case 4:
                continue
            case 5:
                continue
            case 0:
                break
            case _:
                print(f'Pilihan Tidak Valid!')

if __name__ == "__main__":
    main()
