
class Mahasiswa:

    
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

   
    def tampilkan_data(self):
        print("Nama     :", self.nama)
        print("NIM      :", self.nim)
        print("Jurusan  :", self.jurusan)



mhs1 = Mahasiswa("Ilyas", "462025611061", "Informatika")
mhs2 = Mahasiswa("Zakkie", "462025611062", "Sistem Informasi")


mhs1.tampilkan_data()

print("------------------")

mhs2.tampilkan_data()