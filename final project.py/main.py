# exception_handling_lab.py

# Custom Exception
class NilaiTidakValidError(Exception):
    """Exception untuk nilai di luar rentang 0-100"""
    pass


# Class Utama
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

    def input_nilai(self, nilai):
        if nilai < 0 or nilai > 100:
            raise NilaiTidakValidError(
                f"Nilai {nilai} tidak valid! Nilai harus antara 0 sampai 100."
            )

        print(f"Nilai {self.nama} berhasil disimpan: {nilai}")


# Program Utama
try:
    nama = input("Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai mahasiswa: "))

    mahasiswa = Mahasiswa(nama)
    mahasiswa.input_nilai(nilai)

except NilaiTidakValidError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Error: Input nilai harus berupa angka!")

finally:
    print("Proses pemeriksaan nilai telah selesai dilakukan.")