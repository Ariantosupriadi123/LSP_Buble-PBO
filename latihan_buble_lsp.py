def garis():
    print("------------------------")

def sort_asc(array):
       array = sorted(array)
       return(array)


def sort_desc(array):
   array = sorted(array, reverse = True)
   return(array)

def rata_rata(angka):
    return sum(angka)/len(angka)

garis()
print("Masukan tiga buah nilai")

nilai_a = int(input("Nilai A : "))
nilai_b = int(input("Nilai B : "))
nilai_c = int(input("Nilai C : "))

angka = [nilai_a, nilai_b, nilai_c]
garis()
print()

print("HASIL AKHIR----")
print("Urutan Nilai Ascending : ",(sort_asc(angka)))
print("Urutan Nilai Descending : ",(sort_desc(angka)))

print("Nilai Max : ", max(angka))

print("Nilai Min : ", min(angka))

print("Nilai RATA RATA : ", (rata_rata(angka)))
