# Daftar pizza yang tersedia
available_pizzas = [
    "margherita",
    "calzone",
    "four cheese",
    "peperoni",
    "napoli"
]

# List untuk menyimpan pesanan
pizza_order = []

# Total harga
total_price = 0

print("Hello!")

# Perulangan pemesanan pizza
continue_ordering = True

while continue_ordering:
    print("\nApakah kamu ingin menambahkan pizza? (yes/no)")
    answer = input("Jawaban: ")

    if answer == "yes":

        # Memilih pizza
        valid_pizza_choice = False

        while not valid_pizza_choice:
            print("\nPizza yang tersedia:")

            for i in range(len(available_pizzas)):
                print(i + 1, available_pizzas[i])

            pizza_choice = int(input("Pizza mana yang kamu inginkan? (pilih nomor): "))

            # Mengecek pilihan pizza
            if pizza_choice > 0 and pizza_choice < len(available_pizzas) + 1:
                valid_pizza_choice = True

                selected_pizza = available_pizzas[pizza_choice - 1]

                # Menambahkan pizza ke pesanan
                pizza_order.append(selected_pizza)

                print("Adding", selected_pizza, "pizza to the list")

                # Harga setiap pizza = 10
                total_price = total_price + 10

            else:
                print("Please choose a correct number.")

    else:
        continue_ordering = False


# Memasukkan tip
valid_tip = False

while not valid_tip:
    tip = int(input("\nWhat tip do you want to leave (0-25%)? "))

    if tip > -1 and tip < 26:
        valid_tip = True
    else:
        print("Please provide a correct number.")


# Menghitung total dengan tip
total_price = total_price + (total_price * tip / 100)


# Menampilkan hasil
print("\nPesanan kamu:", pizza_order)
print("Thank you! The price is now", total_price, "euro.")
print("Pizzas are on the way!")