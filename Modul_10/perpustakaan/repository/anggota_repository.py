class AnggotaRepository:
    def __init__(self, database):
        self.database = database
 
    def tambah(self, anggota):
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO anggota
                       (nomor_anggota, nama, alamat, nomor_telepon)
                       VALUES (%s, %s, %s, %s)""",
                    (anggota.nomor_anggota, anggota.nama, anggota.alamat,
                     anggota.nomor_telepon)
                )
                id_baru = cur.lastrowid
            conn.commit()
            return id_baru
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
 
    def tampilkan_semua(self):
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM anggota ORDER BY id_anggota")
                return cur.fetchall()
        finally:
            conn.close()
 
    def cari_berdasarkan_nomor(self, nomor_anggota):
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM anggota WHERE nomor_anggota=%s",
                            (nomor_anggota,))
                return cur.fetchone()
        finally:
            conn.close()
 
    def ubah(self, id_anggota, anggota):
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE anggota
                       SET nomor_anggota=%s, nama=%s, alamat=%s, nomor_telepon=%s
                       WHERE id_anggota=%s""",
                    (anggota.nomor_anggota, anggota.nama, anggota.alamat,
                     anggota.nomor_telepon, id_anggota)
                )
                berubah = cur.rowcount
            conn.commit()
            return berubah > 0
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
 
    def hapus(self, id_anggota):
        conn = self.database.connect()
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM anggota WHERE id_anggota=%s",
                            (id_anggota,))
                berubah = cur.rowcount
            conn.commit()
            return berubah > 0
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()