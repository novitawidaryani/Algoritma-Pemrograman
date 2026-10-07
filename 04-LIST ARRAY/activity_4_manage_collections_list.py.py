
# VERSI 1
buah1 = ["apel", "jeruk", "rambutan", "durian", "mangga","anggur", "pisang", "semangka", "melon", "pepaya"]

#tanya buah apa yang diinginnkan 

pencarian = input("Buah apa yang anda inginkan? ").lower()

if pencarian in buah1: 
    print("Buah tersedia") 
else:
	print("Buah tidak tersedia")

#VERSI 2

list_buah = ["apel", "jeruk", "rambutan", "durian", "mangga","anggur", "pisang", "semangka", "melon", "pepaya"]

buah = input("Buah apa yang anda inginkan? ").lower()

if buah in list_buah: 
    print("OK, Buah tersedia") 
else:
	print("Maaf" , buah , "tidak tersedia")


#VERSI 3
listbuah = ["apel", "jeruk", "rambutan", "durian", "mangga","anggur", "pisang", "semangka", "melon", "pepaya"]

fruit = input("Buah apa yang anda inginkan? ").lower()

if not (fruit in listbuah):
      print("Maaf, " + fruit + " tidak tersedia")
      exit()

print("OK, Buah tersedia")


