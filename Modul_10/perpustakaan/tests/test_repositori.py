import pytest

from models.anggota import Anggota
from models.buku import Buku
from models.detail_peminjaman import DetailPeminjaman
from models.peminjaman import Peminjaman
from models.petugas import Petugas
from repository.anggota_repository import AnggotaRepository
from repository.buku_repository import BukuRepository
from repository.peminjaman_repository import PeminjamanRepository
from repository.petugas_repository import PetugasRepository


# ---------- Anggota ----------
def test_anggota_tambah_commit_dan_kembalikan_id(buat_db):
    db, conn = buat_db(lastrowid=7)
    obj = Anggota("A010", "Budi", None, None)
    assert AnggotaRepository(db).tambah(obj) == 7
    assert conn.committed and conn.closed and not conn.rolled_back
    sql, params = conn.executed[0]
    assert "INSERT INTO anggota" in sql
    assert params == ("A010", "Budi", None, None)


def test_anggota_tambah_gagal_rollback(buat_db):
    db, conn = buat_db(fail_on=1, error=RuntimeError("boom"))
    with pytest.raises(RuntimeError):
        AnggotaRepository(db).tambah(Anggota("A010", "Budi", None, None))
    assert conn.rolled_back and conn.closed and not conn.committed


def test_anggota_tampilkan_semua(buat_db):
    db, conn = buat_db(rows=[{"id_anggota": 1}])
    assert AnggotaRepository(db).tampilkan_semua() == [{"id_anggota": 1}]
    assert conn.closed


def test_anggota_cari_berdasarkan_nomor(buat_db):
    db, conn = buat_db(rows=[{"nomor_anggota": "A001"}])
    hasil = AnggotaRepository(db).cari_berdasarkan_nomor("A001")
    assert hasil == {"nomor_anggota": "A001"}
    assert conn.executed[0][1] == ("A001",)


def test_anggota_cari_tidak_ada(buat_db):
    db, _ = buat_db(rows=[])
    assert AnggotaRepository(db).cari_berdasarkan_nomor("X") is None


def test_anggota_ubah_dan_hapus_berhasil(buat_db):
    db, _ = buat_db(rowcount=1)
    repo = AnggotaRepository(db)
    assert repo.ubah(1, Anggota("A001", "Rina", "x", "08")) is True
    assert repo.hapus(1) is True


def test_anggota_ubah_dan_hapus_tidak_ditemukan(buat_db):
    db, _ = buat_db(rowcount=0)
    repo = AnggotaRepository(db)
    assert repo.ubah(99, Anggota("A001", "Rina", "x", "08")) is False
    assert repo.hapus(99) is False


# ---------- Buku ----------
def test_buku_tambah(buat_db):
    db, conn = buat_db(lastrowid=5)
    obj = Buku("B010", "Judul", "Penulis", 2020, "Umum")
    assert BukuRepository(db).tambah(obj) == 5
    assert conn.executed[0][1] == ("B010", "Judul", "Penulis", 2020, "Umum")
    assert conn.committed


def test_buku_cari_judul_memakai_wildcard(buat_db):
    db, conn = buat_db(rows=[{"judul": "Python"}])
    assert BukuRepository(db).cari_judul("py") == [{"judul": "Python"}]
    assert conn.executed[0][1] == ("%py%",)


def test_buku_hapus_tidak_ditemukan(buat_db):
    db, _ = buat_db(rowcount=0)
    assert BukuRepository(db).hapus(99) is False


def test_buku_ubah_gagal_rollback(buat_db):
    db, conn = buat_db(fail_on=1)
    with pytest.raises(RuntimeError):
        BukuRepository(db).ubah(1, Buku("B1", "J", "P", 2020, "K"))
    assert conn.rolled_back and not conn.committed


# ---------- Petugas ----------
def test_petugas_crud_dasar(buat_db):
    db, conn = buat_db(lastrowid=3, rowcount=1)
    repo = PetugasRepository(db)
    assert repo.tambah(Petugas("Agus", "agus")) == 3
    assert repo.ubah(1, Petugas("Agus S", "agus")) is True
    assert repo.hapus(1) is True


def test_petugas_hapus_gagal_rollback(buat_db):
    db, conn = buat_db(fail_on=1)
    with pytest.raises(RuntimeError):
        PetugasRepository(db).hapus(1)
    assert conn.rolled_back


# ---------- Model Peminjaman ----------
def test_model_total_buku():
    p = Peminjaman(1, 1, "2026-11-19")
    p.tambah_detail(DetailPeminjaman(1, 2))
    p.tambah_detail(DetailPeminjaman(2, 3))
    assert p.total_buku() == 5
    assert p.status == "DIPINJAM"


# ---------- Peminjaman (transaksi) ----------
def _peminjaman_dua_buku():
    p = Peminjaman(1, 2, "2026-11-19")
    p.tambah_detail(DetailPeminjaman(1, 1))
    p.tambah_detail(DetailPeminjaman(2, 2))
    return p


def test_peminjaman_tambah_satu_transaksi(buat_db):
    db, conn = buat_db(lastrowid=10)
    assert PeminjamanRepository(db).tambah(_peminjaman_dua_buku()) == 10
    assert len(conn.executed) == 3  # 1 header + 2 detail
    assert "INSERT INTO peminjaman" in conn.executed[0][0]
    assert conn.executed[1][1] == (10, 1, 1)
    assert conn.executed[2][1] == (10, 2, 2)
    assert conn.committed and conn.closed


def test_peminjaman_tanpa_detail_ditolak(buat_db):
    db, _ = buat_db()
    with pytest.raises(ValueError, match="minimal satu buku"):
        PeminjamanRepository(db).tambah(Peminjaman(1, 1, "2026-11-19"))
    assert db.jumlah_connect == 0  # ditolak sebelum membuka koneksi


def test_peminjaman_detail_gagal_rollback_semua(buat_db):
    db, conn = buat_db(fail_on=3)  # detail kedua gagal
    with pytest.raises(RuntimeError):
        PeminjamanRepository(db).tambah(_peminjaman_dua_buku())
    assert conn.rolled_back and not conn.committed and conn.closed


def test_kembalikan_berhasil_dan_sudah_dikembalikan(buat_db):
    db, conn = buat_db(rowcount=1)
    assert PeminjamanRepository(db).kembalikan(1, "2026-11-20") is True
    assert conn.executed[0][1] == ("2026-11-20", 1)

    db2, _ = buat_db(rowcount=0)
    assert PeminjamanRepository(db2).kembalikan(1, "2026-11-20") is False


def test_riwayat_semua_tanpa_filter(buat_db):
    db, conn = buat_db(rows=[{"id_peminjaman": 1}])
    assert PeminjamanRepository(db).riwayat_semua() == [{"id_peminjaman": 1}]
    sql, params = conn.executed[0]
    assert "WHERE" not in sql
    assert params == ()


def test_riwayat_berdasarkan_nomor_anggota(buat_db):
    db, conn = buat_db(rows=[])
    PeminjamanRepository(db).riwayat_berdasarkan_nomor_anggota("A001")
    sql, params = conn.executed[0]
    assert "WHERE a.nomor_anggota = %s" in sql
    assert params == ("A001",)