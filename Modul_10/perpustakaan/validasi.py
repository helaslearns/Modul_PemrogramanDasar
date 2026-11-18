from datetime import date, datetime
 
 
def validasi_teks(nilai, nama_kolom, maksimal=None, wajib=True):
    """Mengembalikan teks yang sudah dirapikan, atau melempar ValueError."""
    nilai = (nilai or "").strip()
    if not nilai:
        if wajib:
            raise ValueError(f"{nama_kolom} wajib diisi.")
        return None
    if maksimal is not None and len(nilai) > maksimal:
        raise ValueError(f"{nama_kolom} maksimal {maksimal} karakter.")
    return nilai
 
 
def validasi_angka(nilai, nama_kolom, minimum=None, maksimum=None):
    """Mengembalikan bilangan bulat, atau melempar ValueError."""
    try:
        angka = int(str(nilai).strip())
    except ValueError:
        raise ValueError(f"{nama_kolom} harus berupa angka bulat.") from None
    if minimum is not None and angka < minimum:
        raise ValueError(f"{nama_kolom} minimal {minimum}.")
    if maksimum is not None and angka > maksimum:
        raise ValueError(f"{nama_kolom} maksimal {maksimum}.")
    return angka
 
 
def validasi_tanggal(nilai, nama_kolom, wajib=True):
    """Mengembalikan objek date dari teks YYYY-MM-DD, atau melempar ValueError."""
    nilai = (nilai or "").strip()
    if not nilai:
        if wajib:
            raise ValueError(f"{nama_kolom} wajib diisi.")
        return None
    try:
        return datetime.strptime(nilai, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(
            f"{nama_kolom} harus berformat YYYY-MM-DD (contoh 2026-11-19)."
        ) from None
 
 
def validasi_tahun_terbit(nilai):
    return validasi_angka(nilai, "Tahun terbit", 1500, date.today().year)
