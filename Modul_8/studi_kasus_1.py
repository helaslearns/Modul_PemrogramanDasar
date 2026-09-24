
def add(data: list):
    temp_nip = str(input("Masukkan NIP: "))
    temp_nama = str(input("Masukkan Nama: "))
    temp_jabatan = str(input("Masukkan Jabatan: "))
    temp_gaji = float(input("Masukkan Gaji: "))

    data.append(dict(nip=temp_nip, nama=temp_nama, jabatan=temp_jabatan, gaji=temp_gaji))
    print(f'Data Pegawai Berhasil Ditambahkan!')

def show(data: list):
    print(f'––––––––––[TABEL DATA PEGAWAI]––––––––––')
    print(f"{'NIP':<15} | {'NAMA':<15} | {'JABATAN':<20} | {'GAJI':<15}")
    for item in data:
        print(f"{item['nip']:<15} | {item['nama']:<15} | {item['jabatan']:<20} | {item['gaji']:<15}")

def modify(data: list, nip: str):
    print(f'––––––––––[MODIFIKASI DATA PEGAWAI]––––––––––')
    '''
    print(f'1. Modifikasi Nama Pegawai')
    print(f'2. Tampilkan Seluruh Data')
    print(f'3. Modifikasi Data berdasarkan NIP')        #Fitur nanti, modifikasi secukupnya!
    print(f'4. Hapus Data Pegawai')
    print(f'5. Hitung Rata-rata Gaji')
    print(f'0. Exit')
    '''

    for item in data:
        if item['nip'] == nip:
            print(f'Pegawai dengan NIP {nip} ditemukan!')
            item['nama'] = input(f'Masukkan Nama Baru: ')
            item['jabatan'] = input(f'Masukkan Jabatan Baru: ')
            item['gaji'] = float(input(f'Masukkan Gaji Baru: '))
            print(f'Data Pegawai Berhasil Dimodifikasi!')
            return
    print(f'Pegawai dengan NIP {nip} tidak ditemukan!')

def delete(data: list, nip: str):
    for i, item in enumerate(data):
        if item['nip'] == nip:
            del data[i]
            print(f'Data Pegawai dengan NIP {nip} berhasil dihapus!')
            return
    print(f'Pegawai dengan NIP {nip} tidak ditemukan!')

def main():
    pegawai = [
        {"nip": "PG001", "nama": "Rina", "jabatan": "Staf Administrasi", "gaji": 4500000},
        {"nip": "PG002", "nama": "Budi", "jabatan": "Manajer", "gaji": 8500000}
    ]

    while True:
        print(f'––––––––––[MENU]––––––––––')
        print(f'1. Tambah Data Pegawai')    # Fitur tambahan untuk entry data pegawai
        print(f'2. Tampilkan Seluruh Data') # Fitur tambahan untuk format tabel pegawai
        print(f'3. Modifikasi Data berdasarkan NIP')    # Fitur optimasi search, binary dengan catatan: SELURUH DATA HARUS SORTED
        print(f'4. Hapus Data Pegawai')     # Fitur tambahan untuk optimasi search, binary dengan catatan: SELURUH DATA HARUS SORTED
        print(f'5. Hitung Rata-rata Gaji')  # Fitur tambahan untuk format rupiah
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
                nip = input(f'Masukkan NIP: ')
                modify(pegawai, nip)
                continue
            case 4:
                nip = input(f'Masukkan NIP: ')
                delete(pegawai, nip)
                continue
            case 5:
                total_gaji = sum(item['gaji'] for item in pegawai)
                rata_rata = total_gaji / len(pegawai) if pegawai else 0
                print(f'Rata-rata Gaji: {rata_rata}')
                continue
            case 0:
                print(f'Terima kasih telah menggunakan program ini!')
                break
            case _:
                print(f'Pilihan Tidak Valid!')
        print(f'–––––––––––––––––––––––––––––––––––––––')

if __name__ == "__main__":
    main()
