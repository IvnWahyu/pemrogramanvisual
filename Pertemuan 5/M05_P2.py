print("Case 1")

f = bool(True)
g = bool(False)
print(f)
print(g)
print("======================================================")

print("Case 2")

print(3>2)
print(3+2==5)
print(3<2)
print("======================================================")

print("Case 3")

Penghasilan = 20000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusdibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusdibayar = 0.1 * Penghasilan

print("Pajak yang harus Anda bayar: Rp ", PajakYangHarusdibayar)

print("Case 4")

a = 3
b = "Ini data string"
c = ("Laptop", "buku", "ballpen")
d = ["Laptop", "buku", "ballpen"]
e = {"Laptop":"asus", "buku":"buku_teks", "ballpen":"arrow"}
f = {1, 2, 3, 4, 5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("======================================================")

print("Case 5")

a = 0
b = ""
c = ()
d = []
e = {}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("======================================================")

print("Case 6")
class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("======================================================")