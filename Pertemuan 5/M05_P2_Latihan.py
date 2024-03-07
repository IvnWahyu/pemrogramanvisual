# Inisialisasi variabel boolean
suhu_tubuh = 38.5
gejala_flu = True

# Pengecekan kondisi untuk menentukan diagnosis
if suhu_tubuh >= 38.0 or gejala_flu:
    diagnosis = "Flu"
else:
    diagnosis = "Tidak Flu"

print("======================================================")
# Menampilkan diagnosis
print("Diagnosis:", diagnosis)

# Pengecekan apakah pasien memerlukan istirahat
if suhu_tubuh >= 38.0 or gejala_flu:
    perlu_istirahat = True
else:
    perlu_istirahat = False

print("======================================================")
# Menampilkan apakah pasien perlu istirahat
print("Perlu istirahat:", perlu_istirahat)
