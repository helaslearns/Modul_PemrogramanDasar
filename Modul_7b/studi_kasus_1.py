import matplotlib.pyplot as plt
import numpy as np

def show_table(titik):
    print("–––––––[Tabel Koordinat Titik]–––––––")
    print(f'_'*21)
    print(f'{'|':<5}{"X":<5}{'|':<5}{"Y":<5}{'|'}')
    print(f'_'*21)
    for items in titik:
        x, y = items
        print(f'{'|':<5}{x:<5}{'|':<5}{y:<5}{'|'}')
    print(f'_'*21)
    print(f'Jumlah titik: {len(titik)}')

def main():
    titik = [(0, 0), (2, 3), (4, 1), (-1, 5)]

    show_table(titik)
    for i in range(2):
        x, y = input("Masukkan koordinat titik (format: x,y): ").split(",")
        titik.append((int(x), int(y)))
    clear_screen = lambda: print("\033[H\033[J", end="")
    clear_screen()
    show_table(titik)

    x_coords = [item[0] for item in titik]
    y_coords = [item[1] for item in titik]
    
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Grafik Titik')
    plt.grid(True)
    plt.show()
 

if __name__ == "__main__":
    main()