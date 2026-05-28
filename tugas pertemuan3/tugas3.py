class Mahasiswa:

    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    
    def tampilkan_data(self):
        print(f"Nama  : {self.nama}")
        print(f"Nilai : {self.nilai}")

    
    def status_kelulusan(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"

    
    @staticmethod
    def info_universitas():
        print("Universitas Darussalam Gontor")

    
    @staticmethod
    def hitung_nilai_akhir(tugas, uts, uas):
        return (tugas + uts + uas) / 3



mhs1 = Mahasiswa("ilyas", 80)


mhs1.tampilkan_data()
print("Status :", mhs1.status_kelulusan())

print("-------------------")


Mahasiswa.info_universitas()

nilai_akhir = Mahasiswa.hitung_nilai_akhir(85, 70, 90)
print("Nilai Akhir :", nilai_akhir)