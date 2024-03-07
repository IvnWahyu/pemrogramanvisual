# Inisialisasi set pelanggan
pelanggan = {"John", "Doe", "Jane", "Smith"}

# Menambahkan pelanggan baru
pelanggan.add("Alice")
pelanggan.add("Bob")

# Menghapus pelanggan yang tidak aktif
pelanggan.discard("Smith")

# Menampilkan daftar pelanggan
print("--------------------------------------")
print("Daftar Pelanggan:")
for nama_pelanggan in pelanggan:
    print(nama_pelanggan)

print("--------------------------------------")
# Mengecek apakah pelanggan tertentu ada dalam set
if "Jane" in pelanggan:
    print("Jane adalah pelanggan tetap.")
else:
    print("Jane bukan pelanggan tetap.")

print("--------------------------------------")
# Menampilkan jumlah total pelanggan
print(f"Total Pelanggan: {len(pelanggan)}")
