data_siswa = []
nama = input("masukkan nama siswa: ")
try: 
   umur = int(input("masukkan umur siswa: "))
   nilai_pkn = int(input("masukkan nilai PKN: "))
   nilai_sejarah = int(input("masukkan nilai sejarah: "))
   nilai_matematika = int(input("masukkan nilai matematika: "))  
except ValueError:
   print("umur dan nilai harus angka!")
   continue

siswa = {"nama": nama, "umur": umur, "nilai_pkn": nilai_pkn, "nilai_sejarah": nilai_sejarah, "nilai_matematika": nilai_matematika}
data_siswa.append(siswa)

#menghitung rata-rata
def rata_rata(nilai_pkn, nilai_sejarah, nilai_matematika):
    return(nilai_pkn + nilai_sejarah + nilai_matematika) / 3

avg = rata_rata(nilai_pkn, nilai_sejarah, nilai_matematika)


#cek lulus apa tidak?
if avg >= 75:
   print("lulus")
elif avg < 75:
   print("tidak lulus")


print("\nData Siswa")
for s in data_siswa:
    print(f"Nama: {s['nama']}, Umur: {s['umur']} Rata-Rata: {avg}")
