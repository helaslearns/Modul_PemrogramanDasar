class PeminjamanRepository:
    """Mengelola transaksi peminjaman (header + detail) dan laporan riwayat."""
 
    def __init__(self, database):
        self.database = database
 
    def tambah(self, peminjaman):
        """Menyimpan peminjaman beserta seluruh detail dalam SATU transaksi.
 
        Jika salah satu detail gagal (mis. id_buku tidak ada), seluruh
        perubahan dibatalkan dengan rollback sehingga tidak ada data parsial.
        """
        if not peminjaman.daftar_detail:
            raise ValueError("Peminjaman harus memuat minimal satu buku.")
 
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO peminjaman
                       (id_anggota, id_petugas, tanggal_pinjam,
                        tanggal_kembali, status)
                       VALUES (%s, %s, %s, %s, %s)""",
                    (peminjaman.id_anggota, peminjaman.id_petugas,
                     peminjaman.tanggal_pinjam, peminjaman.tanggal_kembali,
                     peminjaman.status)
                )
                id_baru = cur.lastrowid
                for detail in peminjaman.daftar_detail:
                    cur.execute(
                        """INSERT INTO detail_peminjaman
                           (id_peminjaman, id_buku, jumlah)
                           VALUES (%s, %s, %s)""",
                        (id_baru, detail.id_buku, detail.jumlah)
                    )
            conn.commit()
            return id_baru
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
 
    def kembalikan(self, id_peminjaman, tanggal_kembali):
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE peminjaman
                       SET status='DIKEMBALIKAN', tanggal_kembali=%s
                       WHERE id_peminjaman=%s AND status='DIPINJAM'""",
                    (tanggal_kembali, id_peminjaman)
                )
                berubah = cur.rowcount
            conn.commit()
            return berubah > 0
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
 
    def riwayat_semua(self):
        return self._riwayat("", ())
 
    def riwayat_berdasarkan_nomor_anggota(self, nomor_anggota):
        return self._riwayat("WHERE a.nomor_anggota = %s", (nomor_anggota,))
 
    def _riwayat(self, kondisi, parameter):
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT
                        p.id_peminjaman,
                        a.nomor_anggota,
                        a.nama AS nama_anggota,
                        pt.nama_petugas,
                        p.tanggal_pinjam,
                        p.tanggal_kembali,
                        p.status,
                        b.kode_buku,
                        b.judul,
                        d.jumlah
                    FROM peminjaman p
                    JOIN anggota a ON a.id_anggota = p.id_anggota
                    JOIN petugas pt ON pt.id_petugas = p.id_petugas
                    JOIN detail_peminjaman d ON d.id_peminjaman = p.id_peminjaman
                    JOIN buku b ON b.id_buku = d.id_buku
                    {kondisi}
                    ORDER BY p.tanggal_pinjam DESC, p.id_peminjaman, b.kode_buku
                """, parameter)
                return cur.fetchall()
        finally:
            conn.close()