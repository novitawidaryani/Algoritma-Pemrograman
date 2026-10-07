# Inisialisasi list A dengan beberapa angka
number_list_A = [5, 10, 15, 20]

# Siapkan list B yang kosong
number_list_B = []

# Mengambil setiap item di number_list_A
for item in number_list_A:
    # Kalikan item dengan 2, lalu masukkan ke number_list_B
    number_list_B.append(item * 2)

# Tampilkan hasilnya
print("Hasil List B:", number_list_B)