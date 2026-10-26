from datetime import date

FILE_BARANG = "barang.txt"
FILE_TRANSAKSI = "transaksi.txt"
FILE_LAPORAN = "laporan_penjualan.txt"


def rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")


# ---------- Fungsi file ----------
def baca_barang():
    """Baca barang.txt -> dict {kode: {Nama, Harga, Stok}}"""
    inventaris = {}
    try:
        with open(FILE_BARANG, "r") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue
                kode, nama, harga, stok = baris.split(",")
                inventaris[kode] = {
                    "Nama": nama,
                    "Harga": int(harga),
                    "Stok": int(stok),
                }
    except FileNotFoundError:
        print("File barang.txt tidak ditemukan.")
    return inventaris


def simpan_barang(inventaris):
    with open(FILE_BARANG, "w") as file:
        for kode, data in inventaris.items():
            file.write(f"{kode},{data['Nama']},{data['Harga']},{data['Stok']}\n")


def baca_transaksi():
    """Baca transaksi.txt -> list of list [tanggal, kode, nama, jumlah, total]"""
    daftar = []
    try:
        with open(FILE_TRANSAKSI, "r") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue
                tanggal, kode, nama, jumlah, total = baris.split(",")
                daftar.append([tanggal, kode, nama, int(jumlah), int(total)])
    except FileNotFoundError:
        pass  # belum ada transaksi
    return daftar


# ---------- Fitur 1 ----------
def tampilkan_barang():
    inventaris = baca_barang()
    if not inventaris:
        print("Belum ada data barang.")
        return

    print("\n=== DAFTAR BARANG ===")
    print(f"{'Kode':<10}{'Nama':<15}{'Harga':>12}{'Stok':>8}")
    print("-" * 45)
    for kode, data in inventaris.items():
        print(f"{kode:<10}{data['Nama']:<15}{rupiah(data['Harga']):>12}{data['Stok']:>8}")


# ---------- Fitur 2 ----------
def transaksi_pembelian():
    inventaris = baca_barang()
    if not inventaris:
        return

    tampilkan_barang()
    kode = input("\nMasukkan kode barang: ").strip().upper()
    if kode not in inventaris:
        print("Error: kode barang tidak ditemukan.")
        return

    try:
        jumlah = int(input("Masukkan jumlah beli: "))
    except ValueError:
        print("Error: jumlah harus berupa angka.")
        return

    if jumlah <= 0:
        print("Error: jumlah harus lebih dari 0.")
        return

    barang = inventaris[kode]
    if jumlah > barang["Stok"]:
        print(f"Error: stok tidak cukup. Stok {barang['Nama']} tersisa {barang['Stok']}.")
        return

    total = jumlah * barang["Harga"]
    barang["Stok"] -= jumlah
    simpan_barang(inventaris)

    tanggal = date.today().isoformat()
    with open(FILE_TRANSAKSI, "a") as file:
        file.write(f"{tanggal},{kode},{barang['Nama']},{jumlah},{total}\n")

    print(f"\nTransaksi berhasil: {jumlah} x {barang['Nama']} = {rupiah(total)}")


# ---------- Fitur 3 ----------
def lihat_riwayat():
    daftar = baca_transaksi()
    if not daftar:
        print("Belum ada transaksi.")
        return

    print("\n=== RIWAYAT TRANSAKSI ===")
    print(f"{'Tanggal':<12}{'Kode':<10}{'Nama':<15}{'Jml':>5}{'Total':>14}")
    print("-" * 56)
    omzet = 0
    for tanggal, kode, nama, jumlah, total in daftar:
        print(f"{tanggal:<12}{kode:<10}{nama:<15}{jumlah:>5}{rupiah(total):>14}")
        omzet += total
    print("-" * 56)
    print(f"Total omzet: {rupiah(omzet)}")


# ---------- Fitur 4 ----------
def update_barang():
    inventaris = baca_barang()
    if not inventaris:
        return

    tampilkan_barang()
    kode = input("\nMasukkan kode barang yang diupdate: ").strip().upper()
    if kode not in inventaris:
        print("Error: kode barang tidak ditemukan.")
        return

    print("1. Update harga")
    print("2. Update stok")
    pilihan = input("Pilih (1/2): ").strip()

    try:
        if pilihan == "1":
            harga_baru = int(input("Harga baru: "))
            if harga_baru < 0:
                print("Error: harga tidak boleh negatif.")
                return
            inventaris[kode]["Harga"] = harga_baru
        elif pilihan == "2":
            stok_baru = int(input("Stok baru: "))
            if stok_baru < 0:
                print("Error: stok tidak boleh negatif.")
                return
            inventaris[kode]["Stok"] = stok_baru
        else:
            print("Pilihan tidak valid.")
            return
    except ValueError:
        print("Error: input harus berupa angka.")
        return

    simpan_barang(inventaris)
    print("Data barang berhasil diperbarui.")


# ---------- Fitur 5 ----------
def laporan_harian():
    daftar = baca_transaksi()
    if not daftar:
        print("Belum ada transaksi, laporan tidak dibuat.")
        return

    total_transaksi = len(daftar)
    total_omzet = sum(t[4] for t in daftar)

    terjual: dict[str, int] = {}  # nama -> total jumlah terjual
    for _, _, nama, jumlah, _ in daftar:
        terjual[nama] = terjual.get(nama, 0) + jumlah
    terlaris = max(terjual, key=lambda nama: terjual[nama])

    with open(FILE_LAPORAN, "w") as file:
        file.write(f"Total Transaksi: {total_transaksi}\n")
        file.write(f"Total Omzet: {rupiah(total_omzet)}\n")
        file.write(f"Barang Terlaris: {terlaris}\n")

    print(f"Laporan berhasil ditulis ke {FILE_LAPORAN}:")
    print(f"  Total Transaksi : {total_transaksi}")
    print(f"  Total Omzet     : {rupiah(total_omzet)}")
    print(f"  Barang Terlaris : {terlaris}")


# ---------- Menu ----------
def main():
    while True:
        print("\n=== APLIKASI KASIR ===")
        print("1. Tampilkan Daftar Barang")
        print("2. Transaksi Pembelian")
        print("3. Lihat Riwayat Transaksi")
        print("4. Update Data Barang")
        print("5. Laporan Harian")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            transaksi_pembelian()
        elif pilihan == "3":
            lihat_riwayat()
        elif pilihan == "4":
            update_barang()
        elif pilihan == "5":
            laporan_harian()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()