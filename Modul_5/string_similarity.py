import string
import re

def main():
    print("Masukkan 2 kalimat untuk dibandingkan:")
    kalimat_1 = input("Kalimat 1: ")
    kalimat_2 = input("Kalimat 2: ")

    similarity_score = []

    for i in range(len(kalimat_1)):
        if kalimat_1[i] == kalimat_2[i]:
            similarity_score.append(1)
        else:
            similarity_score.append(0)

    print(f"Skor Kemiripan: {sum(similarity_score) / len(similarity_score) * 100:.2f}%")

if __name__ == "__main__":
    main()