



class AlatPembayaran:
    def proses_bayar(self, jumlah):
        print(f"Memproses pembayaran sebesar Rp{jumlah}")



class KartuKredit(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah:,} berhasil menggunakan Kartu Kredit.")



class EWallet(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah:,} berhasil menggunakan E-Wallet.")



class TransferBank(AlatPembayaran):
    def proses_bayar(self, jumlah):
        print(f"Pembayaran Rp{jumlah:,} berhasil melalui Transfer Bank.")



def jalankan_transaksi(objek, jumlah):
    print("\nMenjalankan transaksi...")
    objek.proses_bayar(jumlah)



def main():
    print("=== PROGRAM POLYMORPHISM DAN DUCK TYPING ===")

   
    kartu = KartuKredit()
    ewallet = EWallet()
    transfer = TransferBank()

    
    jalankan_transaksi(kartu, 50000)
    jalankan_transaksi(ewallet, 75000)
    jalankan_transaksi(transfer, 100000)



if __name__ == "__main__":
    main()