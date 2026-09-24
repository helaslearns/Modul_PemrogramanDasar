pegawai = [
        {"nip": "PG001", "nama": "Rina", "jabatan": "Staf Administrasi", "gaji": 4500000},
        {"nip": "PG002", "nama": "Budi", "jabatan": "Manajer", "gaji": 8500000}
    ]

for item in pegawai:
    for key, value in item.items():
        print(f'{key}: {value}')
        print()