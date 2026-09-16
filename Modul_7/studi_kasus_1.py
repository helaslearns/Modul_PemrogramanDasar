def struk(inventaris, nama_barang, jumlah_beli, total_harga):
    print(f'\n{"-"*30}\nSTRUK PEMBELIAN\n{"-"*30}')
    print(f'Nama Barang: {nama_barang}')
    print(f'Harga Satuan: Rp {inventaris[nama_barang]["harga"]}')
    print(f'Jumlah Beli: {jumlah_beli}')
    print(f'Total Harga: Rp {total_harga}')
    if total_harga > 5000000:
        diskon = total_harga * 0.1
        total_harga -= diskon
        print(f'Diskon 10% diterapkan. Total harga setelah diskon: Rp {total_harga}')
    print(f'{"-"*30}\nTerima kasih telah berbelanja!')

def pembelian(inventaris):
    nama_barang = input('Masukkan nama barang: ')
    if nama_barang in inventaris:
        jumlah_beli = int(input('Masukkan jumlah beli: '))
        if jumlah_beli <= inventaris[nama_barang]['stok']:
            total_harga = jumlah_beli * inventaris[nama_barang]['harga']
            inventaris[nama_barang]['stok'] -= jumlah_beli
            struk(inventaris, nama_barang, jumlah_beli, total_harga)
        else:
            print('Stok tidak mencukupi.')
    else:
        print('Barang tidak ditemukan.')

    if total_harga > 5000000:
        diskon = total_harga * 0.1
        total_harga -= diskon
        print(f'Diskon 10% diterapkan. Total harga setelah diskon: Rp {total_harga}')

    struk(inventaris, nama_barang, jumlah_beli, total_harga)
    
def main():
    inventaris = {
        "Laptop": {"harga": 7000000, "stok": 5},
        "Mouse": {"harga": 150000, "stok": 10},
        "Keyboard": {"harga": 250000, "stok": 7}
    }

    while True:
        print(f'SISTEM KASIR SEDERHANA\n{"-"*30}')
        for key, value in inventaris.items():
            print(f"{key:<15} | Rp {value['harga']:<12} | {value['stok']}")

        input(f'Tekan Enter untuk melanjutkan...')

        print(f'\n{"-"*30}\nMenu:\n1. Pembelian Barang \n2. Keluar')
        pilihan = input('Masukkan pilihan (1/2): ')

        match pilihan:
            case "1":
                pembelian(inventaris)
                input(f'Tekan Enter untuk melanjutkan...')
                continue
            case "2":
                print('Terima kasih telah menggunakan sistem kasir sederhana.')
                break
            case _:
                print('Pilihan tidak valid. Silakan coba lagi.')
                print()
                continue

if __name__ == "__main__":
    main()

