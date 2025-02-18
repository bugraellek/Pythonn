import random

botNumber = random.randint(1,10)
# print(botNumber)
playerNumber = int(input("1 ile 10 arasında bir sayı girin:"))

while playerNumber!=botNumber:
    print("tahmin edemediniz")
    playerNumber=int(input("tekrar sayı girin:"))
print(f"tahmin ettiniz benim sayım : {botNumber}")

