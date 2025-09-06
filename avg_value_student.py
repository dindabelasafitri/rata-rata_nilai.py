data_siswa = []

while True:
    nama = input("Masukkan nama siswa: ")
    try:
        umur = int(input("Masukkan umur siswa: "))
        nilai_pkn = int(input("Masukkan nilai PKN: "))
        nilai_sejarah = int(input("Masukkan nilai Sejarah: "))
        nilai_matematika = int(input("Masukkan nilai Matematika: "))
    except ValueError:
        print("Umur dan nilai harus angka!")
        continue

    siswa = {
        "nama": nama,
        "umur": umur,
        "nilai_pkn": nilai_pkn,
        "nilai_sejarah": nilai_sejarah,
        "nilai_matematika": nilai_matematika
    }
    data_siswa.append(siswa)

    lanjut = input("Tambah siswa lagi? (y/n): ")
    if lanjut.lower() != "y":
        break

# Fungsi rata-rata
def rata_rata(nilai_pkn, nilai_sejarah, nilai_matematika):
    return (nilai_pkn + nilai_sejarah + nilai_matematika) / 3

# Menampilkan data siswa
print("\nData Siswa")
for s in data_siswa:
    avg = rata_rata(s["nilai_pkn"], s["nilai_sejarah"], s["nilai_matematika"])
    status = "Lulus" if avg >= 75 else "Tidak Lulus"
    print(f"Nama: {s['nama']}, Umur: {s['umur']}, Rata-Rata: {avg:.2f}, Status: {status}")
