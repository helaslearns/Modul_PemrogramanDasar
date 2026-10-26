FILE_USERS = "users.txt"
MAKS_PERCOBAAN = 3


# ---------- Fungsi file ----------
def baca_users():
    """Baca users.txt -> dict {username: password}"""
    users = {}
    try:
        with open(FILE_USERS, "r") as file:
            for baris in file:
                baris = baris.strip()
                if not baris or "," not in baris:
                    continue  # lewati baris kosong atau format salah
                username, password = baris.split(",", 1)
                users[username] = password
    except FileNotFoundError:
        pass
    return users


def simpan_users(users):
    with open(FILE_USERS, "w") as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")


# ---------- Fitur 1 ----------
def registrasi():
    users = baca_users()
    print("\n=== REGISTRASI AKUN BARU ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not username or not password:
        print("Error: username dan password tidak boleh kosong.")
        return
    if "," in username or "," in password:
        print("Error: tanda koma (,) tidak boleh digunakan.")
        return
    if username in users:
        print("Error: username sudah terdaftar.")
        return

    with open(FILE_USERS, "a") as file:
        file.write(f"{username},{password}\n")
    print("Registrasi berhasil.")


# ---------- Fitur 2 ----------
def login():
    """Return username jika berhasil, None jika gagal."""
    users = baca_users()
    print("\n=== LOGIN ===")

    for percobaan in range(1, MAKS_PERCOBAAN + 1):
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username] == password:
            print("Login berhasil")
            return username

        sisa = MAKS_PERCOBAAN - percobaan
        if sisa > 0:
            print(f"Username atau password salah. Sisa percobaan: {sisa}")

    print("Login gagal. Kesempatan percobaan habis.")
    return None


# ---------- Fitur 3 ----------
def ganti_password(username):
    users = baca_users()
    print("\n=== GANTI PASSWORD ===")
    lama = input("Password lama: ").strip()
    if users.get(username) != lama:
        print("Error: password lama salah.")
        return

    baru = input("Password baru: ").strip()
    if not baru or "," in baru:
        print("Error: password tidak boleh kosong atau mengandung koma.")
        return

    users[username] = baru
    simpan_users(users)  # semua akun lain ikut ditulis ulang, tidak hilang
    print("Password berhasil diganti.")


# ---------- Fitur 4 ----------
def daftar_pengguna(username):
    if username != "admin":
        print("Akses ditolak: fitur ini khusus admin.")
        return

    users = baca_users()
    print("\n=== DAFTAR PENGGUNA ===")
    for no, nama in enumerate(users, start=1):
        print(f"{no}. {nama}")


# ---------- Menu setelah login ----------
def menu_pengguna(username):
    while True:
        print(f"\n=== MENU ({username}) ===")
        print("1. Ganti Password")
        print("2. Daftar Pengguna (khusus admin)")
        print("0. Logout")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            ganti_password(username)
        elif pilihan == "2":
            daftar_pengguna(username)
        elif pilihan == "0":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


# ---------- Menu utama ----------
def main():
    while True:
        print("\n=== SISTEM LOGIN ===")
        print("1. Registrasi")
        print("2. Login")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            registrasi()
        elif pilihan == "2":
            username = login()
            if username:
                menu_pengguna(username)
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()