# Alur Cerita: Buah, Makanan, Pakaian dan Aksesoris, Belanja/Bahan Pokok

# Inisialisasi setiap kategori barang
buah = {"apel", "pisang", "jeruk"}
makanan = {"nasi", "daging", "sayur"}
pakaian_aksesoris = {"baju", "celana", "sepatu"}
belanjaan = {"beras", "gula", "minyak"}

# Dialog
print("Hari ini Maya pergi berbelanja untuk keluarganya.")
print("Pertama-tama, Maya memutuskan untuk membeli buah-buahan segar.")
print("Dia memilih apel, pisang, dan jeruk sebagai pilihan buah-buahan untuk minggu ini.")
print("Maya menambahkan buah-buahan tersebut ke dalam keranjang belanja.")

# Menampilkan setiap kategori barang
print("\nBuah:", buah)
print("Makanan:", makanan)
print("Pakaian dan aksesoris:", pakaian_aksesoris)
print("Belanja/bahan pokok:", belanjaan)

# Menghitung jumlah barang dalam setiap kategori
print("\nJumlah buah:", len(buah))
print("Jumlah makanan:", len(makanan))
print("Jumlah pakaian dan aksesoris:", len(pakaian_aksesoris))
print("Jumlah belanja/bahan pokok:", len(belanjaan))

# Dialog
print("\nSetelah itu, Maya melanjutkan perjalanan belanja ke bagian makanan.")
print("Dia membeli beras, gula, minyak, dan beberapa jenis daging untuk menyusun menu masakan keluarganya.")

makanan.add("telur")
print("\nMaya memutuskan untuk menambahkan telur ke dalam keranjang belanja makanan.")

pakaian_aksesoris.update(["topi", "jam tangan"])
print("Maya juga membeli topi dan jam tangan untuk menambah koleksi pakaian dan aksesoris keluarganya.")

belanjaan.remove("minyak")
print("Namun, Maya kehabisan minyak, jadi dia menghapus minyak dari keranjang belanja.")

pakaian_aksesoris.discard("sepatu")
print("Maya memutuskan untuk tidak membeli sepatu, jadi dia menghapus sepatu dari keranjang belanja pakaian dan aksesoris.")

barang_terhapus = belanjaan.pop()
print("Maya memilih untuk menghapus", barang_terhapus, "dari keranjang belanja bahan pokok.")

# belanjaan.clear()
# print("Maya memutuskan untuk tidak membeli barang belanjaan lainnya, jadi dia mengosongkan keranjang belanja.")

semua_barang = buah.union(makanan, pakaian_aksesoris, belanjaan)

print("\nSetelah selesai berbelanja, Maya kembali ke rumah dengan semua barang belanjaannya.")
print("Dia senang karena telah berhasil mendapatkan semua yang dibutuhkan keluarganya dalam satu hari belanja yang efisien.")
