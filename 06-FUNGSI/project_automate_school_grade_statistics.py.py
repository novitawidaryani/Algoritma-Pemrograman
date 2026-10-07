# FUNGSI UNTUK MENGUMPULKAN NILAI
def get_grades_from_user(daftar_nilai):
    while True:
        nilai = float(input("Masukkan nilai (ketik -1 untuk berhenti): "))
        
        if nilai == -1:
            return daftar_nilai
            
        elif nilai >= 0 and nilai <= 10:
            daftar_nilai.append(nilai)
            print("Nilai berhasil ditambahkan!")
            
        else:
            print("Pesan Error: Nilai tidak valid! Masukkan angka antara 0 hingga 10.")

# FUNGSI UNTUK MENCARI NILAI MINIMUM
def compute_list_minimum(grades):
    minimum = grades[0]  
    index = 0            
    
    while index < len(grades):
        if grades[index] < minimum:
            minimum = grades[index]  
        index = index + 1            
        
    return minimum

# FUNGSI UNTUK MENCARI NILAI MAXIMUM
def compute_list_maximum(grades):
    maximum = grades[0]  
    index = 0            
    
    while index < len(grades):
        if grades[index] > maximum:
            maximum = grades[index]  
        index = index + 1            
        
    return maximum

# FUNGSI UNTUK MENGHITUNG RATA-RATA
def compute_list_average(grades):
    total_sum = 0  
    index = 0      
    
    while index < len(grades):
        total_sum = total_sum + grades[index]  
        index = index + 1                      
        
    average = total_sum / len(grades)  
    return average

# ==========================================
# ALUR UTAMA
# ==========================================

print("=== Program Pendataan & Perhitungan Nilai ===")

# 1. Pengumpulan nilai
list_nilai_siswa = []
list_nilai_siswa = get_grades_from_user(list_nilai_siswa)

# 2. Menampilkan daftar dan jumlah nilai
print("\n=== Hasil Akhir ===")
print("Daftar semua nilai:", list_nilai_siswa)

jumlah_nilai = len(list_nilai_siswa)
print("Banyaknya data nilai:", jumlah_nilai)

# 3. Menghitung Minimum, Maximum, dan Average
# Pastikan ada data nilai yang dimasukkan sebelum dihitung
if jumlah_nilai > 0:
    # Menggunakan fungsi manual yang sudah kita buat di atas
    nilai_minimum = compute_list_minimum(list_nilai_siswa)
    nilai_maximum = compute_list_maximum(list_nilai_siswa)
    rata_rata = compute_list_average(list_nilai_siswa)
    
    print("Nilai Terkecil (Minimum) :", nilai_minimum)
    print("Nilai Terbesar (Maximum) :", nilai_maximum)
    print("Nilai Rata-rata (Average):", rata_rata)
    
else:
    print("Kamu belum memasukkan nilai apa pun, perhitungan tidak bisa dilakukan.")