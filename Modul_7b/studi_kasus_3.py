def main():
    jadwal = [
        ("Senin", "08.00", "Pemrograman 1", "Lab 1"),
        ("Selasa", "10.00", "Basis Data", "Lab 2"),
        ("Rabu", "13.00", "Multimedia", "Ruang 3")
    ]
    
    print("–––––––[Jadwal Kuliah]–––––––")
    print(f'{'|':<10}{"Hari":<10}{"Waktu":<10}{"Mata Kuliah":<20}{"Ruangan":<15}{'|'}')
    print(f'_'*55)
    for hari, waktu, mata_kuliah, ruangan in jadwal:
        print(f'{'|':<10}{hari:<10}{waktu:<10}{mata_kuliah:<20}{ruangan:<15}{'|'}')
    print(f'_'*55)

if __name__ == "__main__":
    main()