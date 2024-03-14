# Input nilai a dan b
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

# Cek apakah a lebih besar dari b
a_lebih_b = a > b

# Cek apakah b lebih besar dari a
b_lebih_a = b > a

# Cek apakah a sama dengan b
a_sama_dengan_b = a == b

# Hitung ppn a sebesar 12% jika lebih dari 10000
ppn_a = a * 0.12 if a > 10000 else 0

# Hitung ppn b sebesar 12% jika lebih dari 50000
ppn_b = b * 0.12 if b > 50000 else 0

# Tambahkan kedua ppn a dan b
total_ppn = ppn_a + ppn_b

# Cek apakah total ppn lebih besar dari 0
total_ppn_lebih_besar_dari_0 = total_ppn > 0

# Hapus a dan b
del a, b

# Cek apakah a dan b masih ada
a_masih_ada = 'a' in locals()
b_masih_ada = 'b' in locals()

# Output
print("Apakah a lebih besar dari b?", a_lebih_b)
print("Apakah b lebih besar dari a?", b_lebih_a)
print("Apakah a sama dengan b?", a_sama_dengan_b)
print("PPN a:", ppn_a)
print("PPN b:", ppn_b)
print("Apakah total PPN lebih besar dari 0?", total_ppn_lebih_besar_dari_0)
print("Apakah nilai a masih ada?", a_masih_ada)
print("Apakah nilai b masih ada?", b_masih_ada)
