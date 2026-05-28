class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo   # atribut private

    # Getter
    def get_saldo(self):
        return self.__saldo

    # Method untuk menambah saldo
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Saldo berhasil ditambah {jumlah}")
        else:
            print("Jumlah setor harus lebih dari 0")

    # Method untuk mengambil saldo
    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil menarik {jumlah}")
        else:
            print("Saldo tidak mencukupi")


# Membuat objek
rekening = RekeningBank("ilyas", 1000000)

# Mengakses data melalui getter
print("Saldo awal:", rekening.get_saldo())

# Menambah saldo
rekening.setor(500000)

# Menarik saldo
rekening.tarik(300000)

print("Saldo akhir:", rekening.get_saldo())