from abc import ABC, abstractmethod


# ==========================================
# 1. INHERITANCE & POLYMORPHISM (Class User)
# ==========================================
class User(ABC):

  def __init__(self, id_user, nama, username):
    self._id_user = id_user
    self._nama = nama
    self._username = username

  @abstractmethod
  def tampilkan_info(self):
    pass


class Admin(User):

  def __init__(self, id_user, nama, username, hak_akses):
    super().__init__(id_user, nama, username)
    self.hak_akses = hak_akses

  def tampilkan_info(self):
    print(
        f"[ADMIN] ID: {self._id_user} | Nama: {self._nama} | Hak Akses:"
        f" {self.hak_akses}"
    )


class Kasir(User):

  def __init__(self, id_user, nama, username, shift):
    super().__init__(id_user, nama, username)
    self.shift = shift

  def tampilkan_info(self):
    print(
        f"[KASIR] ID: {self._id_user} | Nama: {self._nama} | Shift: {self.shift}"
    )


# ==========================================
# 2. ENCAPSULATION (Class Pelanggan)
# ==========================================
class Pelanggan:

  def __init__(self, id_pelanggan, nama, nomor_telepon, plat_nomor):
    # Atribut Private (Encapsulation)
    self.__id_pelanggan = id_pelanggan
    self.__nama = nama
    self.__nomor_telepon = nomor_telepon
    self.__plat_nomor = plat_nomor

  # Getter & Setter menggunakan Decorator @property
  @property
  def id_pelanggan(self):
    return self.__id_pelanggan

  @id_pelanggan.setter
  def id_pelanggan(self, value):
    self.__id_pelanggan = value

  @property
  def nama(self):
    return self.__nama

  @nama.setter
  def nama(self, value):
    self.__nama = value

  @property
  def nomor_telepon(self):
    return self.__nomor_telepon

  @nomor_telepon.setter
  def nomor_telepon(self, value):
    self.__nomor_telepon = value

  @property
  def plat_nomor(self):
    return self.__plat_nomor

  @plat_nomor.setter
  def plat_nomor(self, value):
    self.__plat_nomor = value


# ==========================================
# Class Layanan
# ==========================================
class Layanan:

  def __init__(self, id_layanan, nama_layanan, harga):
    self.id_layanan = id_layanan
    self.nama_layanan = nama_layanan
    self.harga = harga


# ==========================================
# Class Transaksi
# ==========================================
class Transaksi:

  def __init__(self, id_transaksi, pelanggan, layanan):
    self.id_transaksi = id_transaksi
    self.pelanggan = pelanggan
    self.layanan = layanan
    self.total_biaya = self.hitung_total_biaya()

  def hitung_total_biaya(self):
    return self.layanan.harga


# ==========================================
# SISTEM UTAMA ADMINISTRASI CUCI MOTOR
# ==========================================
class SistemAdministrasiCuciMotor:

  def __init__(self):
    self.daftar_pelanggan = []
    self.daftar_layanan = []
    self.daftar_transaksi = []
    self._inisialisasi_data_awal()

  def _inisialisasi_data_awal(self):
    self.daftar_layanan.append(Layanan("L01", "Cuci Regular", 15000))
    self.daftar_layanan.append(Layanan("L02", "Cuci Wax / Pengilap", 25000))
    self.daftar_layanan.append(
        Layanan("L03", "Cuci Salju + Semir Ban", 20000)
    )
    self.daftar_pelanggan.append(
        Pelanggan("P01", "Andi", "08123456789", "B 1234 ABC")
    )

  def menu_pelanggan(self):
    print("\n--- MANAJEMEN PELANGGAN ---")
    print("1. Tambah Pelanggan")
    print("2. Tampilkan Daftar Pelanggan")
    print("3. Cari Pelanggan")
    sub_pilihan = input("Pilih opsi: ")

    if sub_pilihan == "1":
      id_p = input("Masukkan ID Pelanggan: ")
      nama = input("Masukkan Nama: ")
      telp = input("Masukkan No. Telepon: ")
      plat = input("Masukkan Plat Nomor Motor: ")
      self.daftar_pelanggan.append(Pelanggan(id_p, nama, telp, plat))
      print("Pelanggan berhasil ditambahkan!")
    elif sub_pilihan == "2":
      print("\n--- DAFTAR PELANGGAN ---")
      for p in self.daftar_pelanggan:
        print(
            f"ID: {p.id_pelanggan} | Nama: {p.nama} | Telp: {p.nomor_telepon} |"
            f" Plat: {p.plat_nomor}"
        )
    elif sub_pilihan == "3":
      keyword = input("Masukkan Nama atau Plat Nomor yang dicari: ").lower()
      ditemukan = False
      for p in self.daftar_pelanggan:
        if (
            keyword in p.nama.lower()
            or keyword in p.plat_nomor.lower()
        ):
          print(
              f"Ditemukan -> ID: {p.id_pelanggan} | Nama: {p.nama} | Plat:"
              f" {p.plat_nomor}"
          )
          ditemukan = True
      if not ditemukan:
        print("Data pelanggan tidak ditemukan.")

  def menu_layanan(self):
    print("\n--- MANAJEMEN LAYANAN ---")
    print("1. Tambah Jenis Layanan")
    print("2. Tampilkan Daftar Layanan & Tarif")
    sub_pilihan = input("Pilih opsi: ")

    if sub_pilihan == "1":
      id_l = input("Masukkan ID Layanan: ")
      nama = input("Masukkan Nama Layanan: ")
      tarif = float(input("Masukkan Tarif (Rp): "))
      self.daftar_layanan.append(Layanan(id_l, nama, tarif))
      print("Layanan baru berhasil ditambahkan!")
    elif sub_pilihan == "2":
      self.tampilkan_daftar_layanan()

  def tampilkan_daftar_layanan(self):
    print("\n--- DAFTAR LAYANAN DAN TARIF ---")
    for l in self.daftar_layanan:
      print(
          f"ID: {l.id_layanan} | Layanan: {l.nama_layanan} | Tarif: Rp"
          f" {int(l.harga):,}"
      )

  def catat_transaksi(self):
    print("\n--- CATAT TRANSAKSI BARU ---")
    id_trx = input("Masukkan ID Transaksi: ")
    input_pelanggan = input("Masukkan ID / Nama Pelanggan: ")

    pelanggan_terpilih = None
    for p in self.daftar_pelanggan:
      if (
          p.id_pelanggan.lower() == input_pelanggan.lower()
          or p.nama.lower() == input_pelanggan.lower()
      ):
        pelanggan_terpilih = p
        break

    if not pelanggan_terpilih:
      print(
          "Pelanggan tidak ditemukan. Silakan tambahkan data pelanggan terlebih"
          " dahulu."
      )
      return

    self.tampilkan_daftar_layanan()
    id_layanan = input("Masukkan ID Layanan yang dipilih: ")
    layanan_terpilih = None
    for l in self.daftar_layanan:
      if l.id_layanan.lower() == id_layanan.lower():
        layanan_terpilih = l
        break

    if not layanan_terpilih:
      print("Layanan tidak ditemukan!")
      return

    trx = Transaksi(id_trx, pelanggan_terpilih, layanan_terpilih)
    self.daftar_transaksi.append(trx)
    print("\nTransaksi Berhasil Dicatat!")
    print(f"Total Biaya: Rp {int(trx.total_biaya):,}")

  def tampilkan_laporan(self):
    print("\n=======================================================")
    print("           LAPORAN TRANSAKSI DAN PENDAPATAN           ")
    print("=======================================================")

    if not self.daftar_transaksi:
      print("Belum ada transaksi yang tercatat.")
      return

    total_pendapatan = 0
    for t in self.daftar_transaksi:
      print(f"ID Trx   : {t.id_transaksi}")
      print(
          f"Pelanggan: {t.pelanggan.nama} ({t.pelanggan.plat_nomor})"
      )
      print(f"Layanan  : {t.layanan.nama_layanan}")
      print(f"Biaya    : Rp {int(t.total_biaya):,}")
      print("-------------------------------------------------------")
      total_pendapatan += t.total_biaya

    print(f"TOTAL KENDARAAN DICUCI : {len(self.daftar_transaksi)} Motor")
    print(f"TOTAL PENDAPATAN       : Rp {int(total_pendapatan):,}")
    print("=======================================================")


def main():
  # Pengujian Polymorphism
  print("=== DATA PENGGUNA SISTEM (POLYMORPHISM) ===")
  admin = Admin("U01", "Ilyas Maulana", "admin_ilyas", "Full Access")
  kasir = Kasir("U02", "Budi Santoso", "kasir_budi", "Pagi")
  admin.tampilkan_info()
  kasir.tampilkan_info()
  print("=========================================\n")

  app = SistemAdministrasiCuciMotor()

  while True:
    print("=== MENU SISTEM ADMINISTRASI CUCI MOTOR ===")
    print("1. Manajemen Data Pelanggan")
    print("2. Manajemen Layanan")
    print("3. Catat Transaksi Baru")
    print("4. Laporan Transaksi & Pendapatan")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
      app.menu_pelanggan()
    elif pilihan == "2":
      app.menu_layanan()
    elif pilihan == "3":
      app.catat_transaksi()
    elif pilihan == "4":
      app.tampilkan_laporan()
    elif pilihan == "5":
      print("Terima kasih telah menggunakan sistem ini!")
      break
    else:
      print("Pilihan tidak valid!")
    print()


if __name__ == "__main__":
  main()