"""Konstanta bersama (modul biasa, bukan kelas) agar tidak ada 'string ajaib' tersebar di kode."""

# --- format file ---
PEMISAH = "|"
TANDA_KOSONG = "-"
FORMAT_TANGGAL = "%Y-%m-%d"

# --- nama file (di folder data/) ---
FILE_MAHASISWA = "mahasiswa.txt"
FILE_ALAT = "alat.txt"
FILE_TRANSAKSI = "transaksi.txt"
FILE_DETAIL = "detail_transaksi.txt"
FILE_LOG = "log.txt"

# --- jumlah kolom per file (dipakai from_line untuk validasi baris) ---
KOLOM_MAHASISWA = 4      # nim|nama|no_hp|status_aktif
KOLOM_ALAT = 5           # kode|nama|kategori|kondisi|status
KOLOM_TRANSAKSI = 5      # id|nim|tgl_pinjam|batas_kembali|status
KOLOM_DETAIL = 5         # id|kode|status|kondisi|tgl_kembali

# --- status mahasiswa ---
STATUS_MHS_AKTIF = "aktif"
STATUS_MHS_TIDAK_AKTIF = "tidak aktif"

# --- kondisi alat ---
KONDISI_BAIK = "baik"
KONDISI_RUSAK_RINGAN = "rusak ringan"
KONDISI_RUSAK_BERAT = "rusak berat"
DAFTAR_KONDISI = (KONDISI_BAIK, KONDISI_RUSAK_RINGAN, KONDISI_RUSAK_BERAT)

# --- status alat ---
STATUS_ALAT_TERSEDIA = "tersedia"
STATUS_ALAT_DIPINJAM = "dipinjam"
STATUS_ALAT_TIDAK_TERSEDIA = "tidak tersedia"

# --- status detail transaksi ---
STATUS_DETAIL_DIPINJAM = "dipinjam"
STATUS_DETAIL_DIKEMBALIKAN = "dikembalikan"

# --- status transaksi ---
STATUS_TRX_DIPINJAM = "dipinjam"
STATUS_TRX_SEBAGIAN = "sebagian dikembalikan"
STATUS_TRX_SELESAI = "selesai"

# --- aturan bisnis ---
MAKS_TRANSAKSI_AKTIF = 2     # Aturan 2
MAKS_HARI_PINJAM = 7         # batas waktu pengembalian
