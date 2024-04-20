import random

sayi = random.randint(1, 100)
tahmin_hakki = 6

print("1 ile 100 arasında bir sayı tahmin et!")

while tahmin_hakki > 0:
    tahmin = int(input("Tahmininizi girin: "))
    
    if tahmin == sayi:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    else:
        tahmin_hakki -= 1
        if tahmin < sayi:
            print("Daha yüksek bir sayı girin.")
        else:
            print("Daha düşük bir sayı girin.")
        
        if tahmin_hakki == 0:
            print("Tahmin hakkınız kalmadı. Doğru cevap: ", sayi)
