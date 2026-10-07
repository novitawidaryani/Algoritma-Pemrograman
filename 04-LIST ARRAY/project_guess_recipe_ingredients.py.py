import time

tebak_bahan = ["gula", "garam", "cokelat", "mentega", "telur", "tepung"]
score = 0 

print("Halo, tebak 3 bahan untuk membuat cookies! ")
time.sleep(3)

bahan_1 = input("bahan pertama? ")
if bahan_1 in tebak_bahan: 
    print("selamat, kamu berhasil menebak " + bahan_1)
    score +=1 
else: 
    print("oh no, tebakanmu salah")

bahan_2 = input("bahan kedua? ")
if bahan_2 in tebak_bahan: 
    print("selamat, kamu berhasil menebak " + bahan_2)
    score +=1 
else: 
    print("oh no, tebakanmu salah")

bahan_3 = input("bahan ketiga? ")
if bahan_3 in tebak_bahan: 
    print("selamat, kamu berhasil menebak " + bahan_3)
    score +=1 
else: 
    print("oh no, tebakanmu salah")

print("game over! kamu memiliki " + str(score) + "points")
print("bahan untuk membuat cookies adalah:")
print(tebak_bahan)

