CREATE DATABASE perpustakaan;
 
USE perpustakaan;
 
CREATE TABLE anggota (
    id_anggota INT AUTO_INCREMENT PRIMARY KEY,
    nomor_anggota VARCHAR(15) NOT NULL UNIQUE,
    nama VARCHAR(100) NOT NULL,
    alamat VARCHAR(255),
    nomor_telepon VARCHAR(20)
) ENGINE=InnoDB;
 
CREATE TABLE buku (
    id_buku INT AUTO_INCREMENT PRIMARY KEY,
    kode_buku VARCHAR(15) NOT NULL UNIQUE,
    judul VARCHAR(150) NOT NULL,
    penulis VARCHAR(100) NOT NULL,
    tahun_terbit INT NOT NULL,
    kategori VARCHAR(50) NOT NULL
) ENGINE=InnoDB;
 
CREATE TABLE petugas (
    id_petugas INT AUTO_INCREMENT PRIMARY KEY,
    nama_petugas VARCHAR(100) NOT NULL,
    username VARCHAR(30) NOT NULL UNIQUE
) ENGINE=InnoDB;
 
CREATE TABLE peminjaman (
    id_peminjaman INT AUTO_INCREMENT PRIMARY KEY,
    id_anggota INT NOT NULL,
    id_petugas INT NOT NULL,
    tanggal_pinjam DATE NOT NULL,
    tanggal_kembali DATE NULL,
    status VARCHAR(15) NOT NULL DEFAULT 'DIPINJAM',
    CONSTRAINT fk_peminjaman_anggota
        FOREIGN KEY (id_anggota) REFERENCES anggota(id_anggota)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_peminjaman_petugas
        FOREIGN KEY (id_petugas) REFERENCES petugas(id_petugas)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT ck_peminjaman_status
        CHECK (status IN ('DIPINJAM', 'DIKEMBALIKAN'))
) ENGINE=InnoDB;
 
CREATE TABLE detail_peminjaman (
    id_detail INT AUTO_INCREMENT PRIMARY KEY,
    id_peminjaman INT NOT NULL,
    id_buku INT NOT NULL,
    jumlah INT NOT NULL DEFAULT 1,
    CONSTRAINT fk_detail_peminjaman
        FOREIGN KEY (id_peminjaman) REFERENCES peminjaman(id_peminjaman)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_detail_buku
        FOREIGN KEY (id_buku) REFERENCES buku(id_buku)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT uq_detail UNIQUE (id_peminjaman, id_buku),
    CONSTRAINT ck_detail_jumlah CHECK (jumlah > 0)
) ENGINE=InnoDB;
 
INSERT INTO anggota (nomor_anggota, nama, alamat, nomor_telepon) VALUES
('A001', 'Rina Wulandari', 'Jl. Slamet Riyadi No. 10, Surakarta', '081234567890'),
('A002', 'Dimas Pratama', 'Jl. Ir. Sutami No. 36, Surakarta', '085711112222'),
('A003', 'Sinta Lestari', 'Jl. Kartini No. 5, Karanganyar', '082133334444');
 
INSERT INTO buku (kode_buku, judul, penulis, tahun_terbit, kategori) VALUES
('B001', 'Pemrograman Python untuk Pemula', 'Ahmad Fauzi', 2021, 'Pemrograman'),
('B002', 'Basis Data Relasional', 'Siti Nurhaliza', 2019, 'Basis Data'),
('B003', 'Jaringan Komputer Dasar', 'Budi Santoso', 2020, 'Jaringan'),
('B004', 'Struktur Data dan Algoritma', 'Dewi Anggraini', 2022, 'Pemrograman');
 
INSERT INTO petugas (nama_petugas, username) VALUES
('Agus Setiawan', 'agus'),
('Maya Puspita', 'maya');