from datetime import date
 
import pymysql
 
from database import Database
from models.anggota import Anggota
from models.buku import Buku
from models.detail_peminjaman import DetailPeminjaman
from models.peminjaman import Peminjaman
from models.petugas import Petugas
from repository.anggota_repository import AnggotaRepository
from repository.buku_repository import BukuRepository
from repository.peminjaman_repository import PeminjamanRepository
from repository.petugas_repository import PetugasRepository
from validasi import (
    validasi_angka,
    validasi_tahun_terbit,
    validasi_tanggal,
    validasi_teks,
)
 
db = Database()
anggota_repo = AnggotaRepository(db)
buku_repo = BukuRepository(db)
petugas_repo = PetugasRepository(db)
peminjaman_repo = PeminjamanRepository(db)
 
 
# ---------- fungsi bantu input (mengulang sampai valid) ----------
def minta_teks(label, maksimal=None, wajib=True):
    while True:
        try:
            return validasi_teks(input(f"{label}: "), label, maksimal, wajib)
        except ValueError as error:
            print("Input tidak valid:", error)
 
 
def minta_angka(label, minimum=None, maksimum=None):
    while True:
        try:
            return validasi_angka(input(f"{label}: "), label, minimum, maksimum)
        except ValueError as error:
            print("Input tidak valid:", error)
 
 
def minta_tanggal(label, wajib=True):
    while True:
        try:
            return validasi_tanggal(input(f"{label}: "), label, wajib)
        except ValueError as error:
            print("Input tidak valid:", error)
 
 
def minta_tahun_terbit():
    while True:
        try:
            return validasi_tahun_terbit(input("Tahun terbit: "))
        except ValueError as error:
            print("Input tidak valid:", error)
 
 
def pesan_kesalahan(error):
    """Menerjemahkan kesalahan database menjadi pesan yang mudah dipahami."""
    if isinstance(error, pymysql.err.IntegrityError):
        kode = error.args[0]
        if kode == 1062:
            return "Data duplikat: nilai yang harus unik sudah digunakan."
        if kode == 1452:
            return "ID rujukan tidak ditemukan (pelanggaran Foreign Key)."
        if kode == 1451:
            return "Data tidak dapat dihapus karena masih dipakai data lain."
        return f"Pelanggaran aturan data: {error}"
    if isinstance(error, pymysql.err.OperationalError):
        kode = error.args[0]
        if kode in (4025, 3819):  # CHECK constraint (MariaDB, MySQL)
            return "Nilai tidak memenuhi aturan data (CHECK constraint)."
        if kode in (1045, 1049, 2002, 2003):
            return f"Tidak dapat terhubung ke database: {error}"
    return f"Operasi gagal: {error}"
 
 
def tampilkan(rows):
    if not rows:
        print("Data belum tersedia.")
        return
    for row in rows:
        print(row)
 
 
def cetak_riwayat(data):
    if not data:
        print("Riwayat peminjaman tidak ditemukan.")
        return
    print("\n=== RIWAYAT PEMINJAMAN ===")
    print("-" * 100)
    print(f"{'ID':<4} {'Anggota':<18} {'Petugas':<15} {'Pinjam':<11} "
          f"{'Kembali':<11} {'Status':<13} {'Buku (jumlah)'}")
    print("-" * 100)
    for row in data:
        kembali = str(row["tanggal_kembali"]) if row["tanggal_kembali"] else "-"
        print(f"{row['id_peminjaman']:<4} {row['nama_anggota']:<18} "
              f"{row['nama_petugas']:<15} {row['tanggal_pinjam']!s:<11} "
              f"{kembali:<11} {row['status']:<13} "
              f"{row['judul']} ({row['jumlah']})")
    print("-" * 100)
 
 
# ---------- sub menu ----------
def menu_anggota():
    print("1 Tambah | 2 Tampilkan | 3 Ubah | 4 Hapus")
    aksi = input("Pilih aksi: ").strip()
    if aksi == "1":
        obj = Anggota(minta_teks("Nomor anggota", 15), minta_teks("Nama", 100),
                      minta_teks("Alamat", 255, wajib=False),
                      minta_teks("Nomor telepon", 20, wajib=False))
        print("ID baru:", anggota_repo.tambah(obj))
    elif aksi == "2":
        tampilkan(anggota_repo.tampilkan_semua())
    elif aksi == "3":
        id_ = minta_angka("ID anggota", 1)
        obj = Anggota(minta_teks("Nomor anggota baru", 15),
                      minta_teks("Nama baru", 100),
                      minta_teks("Alamat baru", 255, wajib=False),
                      minta_teks("Nomor telepon baru", 20, wajib=False))
        print("Berhasil." if anggota_repo.ubah(id_, obj) else "Data tidak ditemukan.")
    elif aksi == "4":
        id_ = minta_angka("ID anggota", 1)
        print("Berhasil." if anggota_repo.hapus(id_) else "Data tidak ditemukan.")
    else:
        print("Aksi tidak valid.")
 
 
def menu_buku():
    print("1 Tambah | 2 Tampilkan | 3 Ubah | 4 Hapus | 5 Cari judul")
    aksi = input("Pilih aksi: ").strip()
    if aksi == "1":
        obj = Buku(minta_teks("Kode buku", 15), minta_teks("Judul", 150),
                   minta_teks("Penulis", 100), minta_tahun_terbit(),
                   minta_teks("Kategori", 50))
        print("ID baru:", buku_repo.tambah(obj))
    elif aksi == "2":
        tampilkan(buku_repo.tampilkan_semua())
    elif aksi == "3":
        id_ = minta_angka("ID buku", 1)
        obj = Buku(minta_teks("Kode buku baru", 15),
                   minta_teks("Judul baru", 150),
                   minta_teks("Penulis baru", 100), minta_tahun_terbit(),
                   minta_teks("Kategori baru", 50))
        print("Berhasil." if buku_repo.ubah(id_, obj) else "Data tidak ditemukan.")
    elif aksi == "4":
        id_ = minta_angka("ID buku", 1)
        print("Berhasil." if buku_repo.hapus(id_) else "Data tidak ditemukan.")
    elif aksi == "5":
        tampilkan(buku_repo.cari_judul(minta_teks("Kata kunci judul", 150)))
    else:
        print("Aksi tidak valid.")
 
 
def menu_petugas():
    print("1 Tambah | 2 Tampilkan | 3 Ubah | 4 Hapus")
    aksi = input("Pilih aksi: ").strip()
    if aksi == "1":
        obj = Petugas(minta_teks("Nama petugas", 100),
                      minta_teks("Username", 30))
        print("ID baru:", petugas_repo.tambah(obj))
    elif aksi == "2":
        tampilkan(petugas_repo.tampilkan_semua())
    elif aksi == "3":
        id_ = minta_angka("ID petugas", 1)
        obj = Petugas(minta_teks("Nama petugas baru", 100),
                      minta_teks("Username baru", 30))
        print("Berhasil." if petugas_repo.ubah(id_, obj) else "Data tidak ditemukan.")
    elif aksi == "4":
        id_ = minta_angka("ID petugas", 1)
        print("Berhasil." if petugas_repo.hapus(id_) else "Data tidak ditemukan.")
    else:
        print("Aksi tidak valid.")
 
 
def menu_peminjaman():
    print("1 Peminjaman baru | 2 Pengembalian")
    aksi = input("Pilih aksi: ").strip()
    if aksi == "1":
        id_anggota = minta_angka("ID anggota", 1)
        id_petugas = minta_angka("ID petugas", 1)
        tanggal = minta_tanggal("Tanggal pinjam (YYYY-MM-DD, kosong = hari ini)",
                                wajib=False) or date.today()
        peminjaman = Peminjaman(id_anggota, id_petugas, tanggal)
        while True:
            id_buku = minta_angka("ID buku", 1)
            jumlah = minta_angka("Jumlah", 1, 99)
            peminjaman.tambah_detail(DetailPeminjaman(id_buku, jumlah))
            if input("Tambah buku lain? (y/t): ").strip().lower() != "y":
                break
        id_baru = peminjaman_repo.tambah(peminjaman)
        print(f"Peminjaman tersimpan. ID: {id_baru}, "
              f"total buku: {peminjaman.total_buku()}")
    elif aksi == "2":
        id_ = minta_angka("ID peminjaman", 1)
        tanggal = minta_tanggal("Tanggal kembali (YYYY-MM-DD, kosong = hari ini)",
                                wajib=False) or date.today()
        if peminjaman_repo.kembalikan(id_, tanggal):
            print("Pengembalian tercatat.")
        else:
            print("Peminjaman tidak ditemukan atau sudah dikembalikan.")
    else:
        print("Aksi tidak valid.")
 
 
def menu_riwayat():
    print("1 Semua riwayat | 2 Berdasarkan nomor anggota")
    aksi = input("Pilih aksi: ").strip()
    if aksi == "1":
        cetak_riwayat(peminjaman_repo.riwayat_semua())
    elif aksi == "2":
        nomor = minta_teks("Nomor anggota", 15)
        cetak_riwayat(peminjaman_repo.riwayat_berdasarkan_nomor_anggota(nomor))
    else:
        print("Aksi tidak valid.")
 
 
MENU = {
    "1": menu_anggota,
    "2": menu_buku,
    "3": menu_petugas,
    "4": menu_peminjaman,
    "5": menu_riwayat,
}
 
 
def menu():
    while True:
        print("\n=== SISTEM INFORMASI PERPUSTAKAAN ===")
        print("1. Anggota")
        print("2. Buku")
        print("3. Petugas")
        print("4. Peminjaman")
        print("5. Riwayat Peminjaman (JOIN)")
        print("0. Keluar")
        pilihan = input("Pilih: ").strip()
 
        if pilihan == "0":
            print("Program selesai.")
            break
        if pilihan not in MENU:
            print("Pilihan tidak valid.")
            continue
        try:
            MENU[pilihan]()
        except Exception as error:  # noqa: BLE001 - batas terluar menu: jangan crash
            print(pesan_kesalahan(error))
 
 
if __name__ == "__main__":
    menu()