import pymysql

from main import pesan_kesalahan


def test_duplikat():
    err = pymysql.err.IntegrityError(1062, "Duplicate entry")
    assert "duplikat" in pesan_kesalahan(err).lower()


def test_foreign_key_tidak_ditemukan():
    err = pymysql.err.IntegrityError(1452, "Cannot add child row")
    assert "Foreign Key" in pesan_kesalahan(err)


def test_data_masih_dipakai():
    err = pymysql.err.IntegrityError(1451, "Cannot delete parent row")
    assert "tidak dapat dihapus" in pesan_kesalahan(err)


def test_integrity_kode_lain():
    err = pymysql.err.IntegrityError(9999, "lain")
    assert "Pelanggaran aturan data" in pesan_kesalahan(err)


def test_check_constraint_mariadb_dan_mysql():
    for kode in (4025, 3819):
        err = pymysql.err.OperationalError(kode, "check")
        assert "CHECK constraint" in pesan_kesalahan(err)


def test_gagal_terhubung():
    for kode in (1045, 1049, 2002, 2003):
        err = pymysql.err.OperationalError(kode, "koneksi")
        assert "Tidak dapat terhubung" in pesan_kesalahan(err)


def test_error_lain_pesan_umum():
    assert pesan_kesalahan(ValueError("x")).startswith("Operasi gagal")
    err = pymysql.err.OperationalError(9999, "aneh")
    assert pesan_kesalahan(err).startswith("Operasi gagal")