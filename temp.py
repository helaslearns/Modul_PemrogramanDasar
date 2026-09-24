def main():
    teks = "python"
    hasil = {huruf: teks.count(huruf) for huruf in teks}

    print(hasil)

if __name__ == "__main__":
    main()