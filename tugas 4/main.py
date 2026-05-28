class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"{self.nama} memiliki nilai {self.nilai}"

    def __eq__(self, other):
        return self.nilai == other.nilai

    def __lt__(self, other):
        return self.nilai < other.nilai


m1 = Mahasiswa("ilyas", 85)
m2 = Mahasiswa("zakkie", 90)

print(m1)              # ilyas memiliki nilai 85
print(m1 == m2)        # False
print(m1 < m2)         # True