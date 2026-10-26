FILE_MAHASISWA = "mahasiswa.txt"


def baca_mahasiswa():
    daftar = []
    try:
        with open(FILE_MAHASISWA, "r", encoding="utf-8-sig") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue
                bagian = baris.split(",")
                if len(bagian) != 4:
                    continue
                nim, nama, prodi, nilai = [b.strip() for b in bagian]
                daftar.append({
                    "NIM": nim,
                    "Nama": nama,
                    "Prodi": prodi,
                    "Nilai": int(nilai),
                })
    except FileNotFoundError:
        pass
    return daftar


def simpan_mahasiswa(daftar):
    with open(FILE_MAHASISWA, "w") as file:
        for m in daftar:
            file.write(f"{m['NIM']},{m['Nama']},{m['Prodi']},{m['Nilai']}\n")


def cari_indeks(daftar, nim):
    for i, m in enumerate(daftar):
        if m["NIM"].upper() == nim.upper():
            return i
    return -1


def input_nilai(pesan):
    try:
        nilai = int(input(pesan))
    except ValueError:
        print("Error: nilai harus berupa angka.")
        return None
    if nilai < 0 or nilai > 100:
        print("Error: nilai harus antara 0 dan 100.")
        return None
    return nilai


def tambah_mahasiswa():
    daftar = baca_mahasiswa()
    print("\n=== TAMBAH DATA MAHASISWA ===")
    nim = input("NIM: ").strip().upper()
    nama = input("Nama: ").strip()
    prodi = input("Prodi: ").strip()

    if not nim or not nama or not prodi:
        print("Error: NIM, nama, dan prodi tidak boleh kosong.")
        return
    if "," in nim or "," in nama or "," in prodi:
        print("Error: tanda koma (,) tidak boleh digunakan.")
        return
    if cari_indeks(daftar, nim) != -1:
        print("Error: NIM sudah terdaftar.")
        return

    nilai = input_nilai("Nilai: ")
    if nilai is None:
        return

    with open(FILE_MAHASISWA, "a") as file:
        file.write(f"{nim},{nama},{prodi},{nilai}\n")
    print("Data mahasiswa berhasil ditambahkan.")


def tampilkan_semua():
    daftar = baca_mahasiswa()
    if not daftar:
        print("Belum ada data mahasiswa.")
        return

    print("\n=== DATA MAHASISWA ===")
    print(f"{'NIM':<12}{'NAMA':<15}{'PRODI':<15}{'NILAI':>6}")
    print("-" * 48)
    for m in daftar:
        print(f"{m['NIM']:<12}{m['Nama']:<15}{m['Prodi']:<15}{m['Nilai']:>6}")


def cari_mahasiswa():
    daftar = baca_mahasiswa()
    nim = input("\nMasukkan NIM yang dicari: ").strip()
    indeks = cari_indeks(daftar, nim)
    if indeks == -1:
        print("Error: data mahasiswa tidak ditemukan.")
        return

    m = daftar[indeks]
    print("\n=== DATA DITEMUKAN ===")
    print(f"NIM   : {m['NIM']}")
    print(f"Nama  : {m['Nama']}")
    print(f"Prodi : {m['Prodi']}")
    print(f"Nilai : {m['Nilai']}")


def ubah_mahasiswa():
    daftar = baca_mahasiswa()
    nim = input("\nMasukkan NIM yang akan diubah: ").strip()
    indeks = cari_indeks(daftar, nim)
    if indeks == -1:
        print("Error: data mahasiswa tidak ditemukan.")
        return

    print("1. Ubah nilai")
    print("2. Ubah prodi")
    pilihan = input("Pilih (1/2): ").strip()

    if pilihan == "1":
        nilai_baru = input_nilai("Nilai baru: ")
        if nilai_baru is None:
            return
        daftar[indeks]["Nilai"] = nilai_baru
    elif pilihan == "2":
        prodi_baru = input("Prodi baru: ").strip()
        if not prodi_baru or "," in prodi_baru:
            print("Error: prodi tidak boleh kosong atau mengandung koma.")
            return
        daftar[indeks]["Prodi"] = prodi_baru
    else:
        print("Pilihan tidak valid.")
        return

    simpan_mahasiswa(daftar)
    print("Data mahasiswa berhasil diperbarui.")


def hapus_mahasiswa():
    daftar = baca_mahasiswa()
    nim = input("\nMasukkan NIM yang akan dihapus: ").strip()
    indeks = cari_indeks(daftar, nim)
    if indeks == -1:
        print("Error: data mahasiswa tidak ditemukan.")
        return

    konfirmasi = input(f"Yakin hapus {daftar[indeks]['Nama']}? (y/n): ").strip().lower()
    if konfirmasi != "y":
        print("Penghapusan dibatalkan.")
        return

    daftar.pop(indeks)
    simpan_mahasiswa(daftar)
    print("Data mahasiswa berhasil dihapus.")


def statistik():
    daftar = baca_mahasiswa()
    if not daftar:
        print("Belum ada data mahasiswa.")
        return

    jumlah = len(daftar)
    rata_rata = sum(m["Nilai"] for m in daftar) / jumlah
    tertinggi = max(daftar, key=lambda m: m["Nilai"])
    terendah = min(daftar, key=lambda m: m["Nilai"])

    print("\n=== STATISTIK DATA ===")
    print(f"Jumlah mahasiswa : {jumlah}")
    print(f"Nilai rata-rata  : {rata_rata:.2f}")
    print(f"Nilai tertinggi  : {tertinggi['Nilai']} ({tertinggi['Nama']})")
    print(f"Nilai terendah   : {terendah['Nilai']} ({terendah['Nama']})")


def main():
    while True:
        print("\n=== MANAJEMEN DATA MAHASISWA ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Seluruh Data")
        print("3. Cari Mahasiswa Berdasarkan NIM")
        print("4. Ubah Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Statistik Data")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            ubah_mahasiswa()
        elif pilihan == "5":
            hapus_mahasiswa()
        elif pilihan == "6":
            statistik()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()