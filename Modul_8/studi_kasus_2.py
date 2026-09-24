
def add(inventaris: list):
    temp_kode = str(input("Masukkan Kode: "))
    temp_nama = str(input("Masukkan Nama: "))
    temp_harga = float(input("Masukkan Harga: "))
    temp_stok = int(input("Masukkan Stok: "))

    inventaris.append(dict(kode=temp_kode, nama=temp_nama, harga=temp_harga, stok=temp_stok))
    print(f'Data Inventaris Berhasil Ditambahkan!')

def show(inventaris: list):
    print(f'––––––––––[TABEL DATA INVENTARIS]––––––––––')
    print(f"{'KODE':<15} | {'NAMA':<15} | {'HARGA':<15} | {'STOK':<10}")
    for item in inventaris:
        print(f"{item['kode']:<15} | {item['nama']:<15} | {item['harga']:<15} | {item['stok']:<10}")
    print()

def modify(inventaris: list, kode: str):
    print(f'––––––––––[MODIFIKASI DATA INVENTARIS]––––––––––')
    for item in inventaris:
        if item['kode'] == kode:
            print(f'Barang dengan Kode {kode} ditemukan!')
            item['nama'] = input(f'Masukkan Nama Baru: ')
            item['harga'] = float(input(f'Masukkan Harga Baru: '))
            item['stok'] = int(input(f'Masukkan Stok Baru: '))
            print(f'Data Inventaris Berhasil Dimodifikasi!')
            return
    print(f'Barang dengan Kode {kode} tidak ditemukan!')

def delete(inventaris: list, kode: str):
    print(f'––––––––––[HAPUS DATA INVENTARIS]––––––––––')
    for i, item in enumerate(inventaris):
        if item['kode'] == kode:
            print(f'Barang dengan Kode {kode} ditemukan!')
            inventaris.pop(i)
            print(f'Data Inventaris Berhasil Dihapus!')
            return
    print(f'Barang dengan Kode {kode} tidak ditemukan!')

def transaksi(inventaris: list, kode: str):
    print(f'––––––––––[TRANSAKSI INVENTARIS]––––––––––')
    show(inventaris)

    while True:
        pembelian = []

        # Menambahkan Item ke Daftar Pembelian
        while True:
            item = input(f'Masukkan Kode/Nama Barang: ')
            for item in inventaris:
                    if item['kode'] == kode or item['nama'] == item:
                        print(f'Barang dengan Kode/Nama {item} ditemukan!')
                        jumlah_beli = int(input(f'Masukkan Jumlah Beli: '))
                        if jumlah_beli <= item['stok']:
                            total_harga = jumlah_beli * item['harga']
                            item['stok'] -= jumlah_beli
                            pembelian.append(dict(kode=item['kode'], nama=item['nama'], harga=item['harga'], jumlah=jumlah_beli, total=total_harga))
                            continue
                        else:
                            print(f'Stok tidak mencukupi! Stok tersedia: {item["stok"]}')
                            return

            tambah = input(f'Apakah ingin menambahkan item lain? (y/n): ')
            if tambah.lower() != 'y':
                continue
            else:
                struk(pembelian, inventaris)
                break

def struk(pembelian: list, inventaris: list):

    sub_total = sum(item['total'] for item in pembelian)
    diskon = 0 if sub_total < 200000 else 0.1
    total = sub_total * (1 - diskon)

    print(f'––––––––––[STRUK PEMBELIAN]––––––––––')
    print(f"{'KODE':<15} | {'NAMA':<15} | {'HARGA':<15} | {'JUMLAH':<10} | {'TOTAL':<15}")
    for item in pembelian:
        print(f"{item['kode']:<15} | {item['nama']:<15} | {item['harga']:<15} | {item['jumlah']:<10} | {item['total']:<15}")
    print(f'–––––––––––––––––––––––––––––––––––––––')
    print(f'TOTAL PEMBAYARAN: {total}')
    print(f'DISKON: {diskon * 100}% | {sub_total * diskon}')
    print()

    

def main():
    inventaris = [
        {"kode": "BRG001", "nama": "Beras", "harga": 12000, "stok": 50},
        {"kode": "BRG002", "nama": "Gula", "harga": 14000, "stok": 30},
        {"kode": "BRG003", "nama": "Minyak", "harga": 18000, "stok": 20}
    ]


    while True:
        print(f'––––––––––[MENU INVENTARISASI]––––––––––')
        print(f'1. Tambah Inventaris')    # Fitur tambahan untuk entry inventaris
        print(f'2. Tampilkan Seluruh Inventaris') # Fitur tambahan untuk format tabel inventaris
        print(f'3. Modifikasi Inventaris')    # Fitur optimasi search, binary dengan catatan: SELURUH DATA HARUS SORTED
        print(f'4. Hapus Inventaris')     # Fitur tambahan untuk optimasi search, binary dengan catatan: SELURUH DATA HARUS SORTED
        print(f'5. Transaksi Pembelian')  # Fitur tambahan untuk format rupiah
        print(f'0. Exit')

        opsi = int(input(f'Masukkan pilihan: '))

        match opsi:
            case 1:
                add(inventaris)
                continue
            case 2:
                show(inventaris)
                continue
            case 3:
                kode_barang = input(f'Masukkan Kode Barang: ')
                modify(inventaris, kode_barang)
                continue
            case 4:
                kode_barang = input(f'Masukkan Kode Barang: ')
                delete(inventaris, kode_barang)
                continue
            case 5:
                kode_barang = input(f'Masukkan Kode Barang: ')
                transaksi(inventaris, kode_barang)
                continue
            case 0:
                print(f'Terima kasih telah menggunakan program ini!')
                break

if __name__ == "__main__":
    main()