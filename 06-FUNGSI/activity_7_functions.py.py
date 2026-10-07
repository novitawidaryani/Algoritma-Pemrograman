# 1. Buat fungsi untuk setiap operasi
def tambah_2_angka(angka1, angka2):
    return angka1 + angka2

def kurang_2_angka(angka1, angka2):
    return angka1 - angka2

def kali_2_angka(angka1, angka2):
    return angka1 * angka2

def bagi_2_angka(angka1, angka2):
    return angka1 / angka2

# 2. Mulai dan Cetak instruksi kalkulator
print("Welcome to the Calculator!")
print("Please provide 2 numbers and then an operation type")

# 3 & 4. Minta pengguna memasukkan angka 1 dan angka 2
num1 = float(input("Masukkan angka 1: "))
num2 = float(input("Masukkan angka 2: "))

# 5. Minta pengguna memasukkan jenis operasi menggunakan ANGKA
operasi = input("Operation type? (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ")

# 6. Pengecekan kondisi operasi menggunakan input angka
if operasi == '1':
    # 1 untuk addition (+)
    print("Hasil:", tambah_2_angka(num1, num2))
    
elif operasi == '2':
    # 2 untuk subtraction (-)
    print("Hasil:", kurang_2_angka(num1, num2))
    
elif operasi == '3':
    # 3 untuk multiplication (*)
    print("Hasil:", kali_2_angka(num1, num2))
    
elif operasi == '4':
    # 4 untuk division (/)
    print("Hasil:", bagi_2_angka(num1, num2))
    
else:
    # Jika angka yang dimasukkan bukan 1, 2, 3, atau 4
    print("print error message")