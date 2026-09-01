berat = int(input("Masukkan berat badan Anda (kg): "))
tinggi = float(input("Masukkan tinggi badan Anda (cm): "))

BMI = berat / ((tinggi / 100) ** 2)

if BMI < 18.5:
    kategori = "Kurus (Underweight)"
    keterangan = "Perlu tambah berat badan."
elif BMI < 24.9:
    kategori = "Normal (Ideal)"
    keterangan = "Pertahankan gaya hidup sehat."
elif BMI < 29.9:
    kategori = "Gemuk (Overweight)"
    keterangan = "Perlu Olahraga lebih."
else:|
    kategori = "Obesitas"
    keterangan = "Konsultasi dokter."

print("Nilai BMI :", BMI)
print("Kategori :", kategori)
print("Keterangan :", keterangan)