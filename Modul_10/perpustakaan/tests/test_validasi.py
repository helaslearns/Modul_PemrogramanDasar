from datetime import date

import pytest

from validasi import (
    validasi_angka,
    validasi_tahun_terbit,
    validasi_tanggal,
    validasi_teks,
)


# ---- validasi_teks ----
def test_teks_dirapikan():
    assert validasi_teks("  Rina  ", "Nama", 100) == "Rina"


def test_teks_kosong_wajib_error():
    with pytest.raises(ValueError, match="wajib diisi"):
        validasi_teks("   ", "Nama")


def test_teks_kosong_opsional_mengembalikan_none():
    assert validasi_teks("", "Alamat", wajib=False) is None
    assert validasi_teks(None, "Alamat", wajib=False) is None


def test_teks_melebihi_maksimal():
    with pytest.raises(ValueError, match="maksimal 5"):
        validasi_teks("abcdef", "Kode", 5)


def test_teks_tepat_batas_maksimal():
    assert validasi_teks("abcde", "Kode", 5) == "abcde"


# ---- validasi_angka ----
def test_angka_valid():
    assert validasi_angka(" 12 ", "ID") == 12


@pytest.mark.parametrize("nilai", ["abc", "1.5", "", "  "])
def test_angka_bukan_bilangan_bulat(nilai):
    with pytest.raises(ValueError, match="angka bulat"):
        validasi_angka(nilai, "ID")


def test_angka_di_bawah_minimum():
    with pytest.raises(ValueError, match="minimal 1"):
        validasi_angka("0", "ID", minimum=1)


def test_angka_di_atas_maksimum():
    with pytest.raises(ValueError, match="maksimal 99"):
        validasi_angka("100", "Jumlah", maksimum=99)


def test_angka_tepat_di_batas():
    assert validasi_angka("1", "ID", 1, 99) == 1
    assert validasi_angka("99", "ID", 1, 99) == 99


# ---- validasi_tanggal ----
def test_tanggal_valid():
    assert validasi_tanggal("2026-11-19", "Tanggal") == date(2026, 11, 19)


@pytest.mark.parametrize("nilai", ["19-11-2026", "2026/11/19", "2026-02-30", "abc"])
def test_tanggal_format_salah(nilai):
    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        validasi_tanggal(nilai, "Tanggal")


def test_tanggal_kosong():
    with pytest.raises(ValueError, match="wajib diisi"):
        validasi_tanggal("", "Tanggal")
    assert validasi_tanggal("", "Tanggal", wajib=False) is None


# ---- validasi_tahun_terbit ----
def test_tahun_terbit_valid():
    assert validasi_tahun_terbit("2021") == 2021


def test_tahun_terbit_terlalu_lama():
    with pytest.raises(ValueError):
        validasi_tahun_terbit("1499")


def test_tahun_terbit_di_masa_depan():
    with pytest.raises(ValueError):
        validasi_tahun_terbit(str(date.today().year + 1))