# amount = int(input("Alınan miktarı giriniz: "))
# items_type = input("Alınan ürünün türünü giriniz: ")

# try:
#     amount = int(input("Alınan miktarı giriniz: "))
#     items_type = input("Alınan ürünün türünü giriniz: ")
# except:
#     print("Miktar değerini tamsayı olarak giriniz.")




# try :
#     item_cost = 3
#     item_price = 5
#     amount = int(input("Toplam alınan miktarı giriniz: "))
#     item_type = input ("Ürün tipini giriniz: ")
#     parts_number = int(input("Parça sayısını giriniz: "))
#     parts_percentage =((amount - parts_number) / amount) *100
#     revenue = item_price * parts_number
#     cost = item_cost * parts_number
#     profit = revenue - cost

#     print("Kalan miktarın yüzdesi: ", parts_percentage)
#     print("Sipariş edilen miktar: ", parts_number)
#     print("Elde edilen gelir: " , revenue)
#     print("Maliyet: ", cost)
#     print("Kar: ", profit)

# except ValueError:
#     print("Miktar tamsayı olmadığı")
# except ZeroDivisionError:
#     print("Stokta ürün bulunmamaktadır.")

# finally:
#     print("Program tammalandı.")

def para_çek(bakiye, cekilecek_miktar):
    if cekilecek_miktar <=0:
        raise ValueError("Çekilecek mikitar sıfırdan büyük olmalı.")
    if cekilecek_miktar> bakiye:
        raise ValueError("Yetersiz bakiye.")
    if cekilecek_miktar > 10000 :
        raise ValueError("Günlük çekim limiti aşıldı.")
    return bakiye - cekilecek_miktar
try:
    hesap_bakiye = 100000
    print(f"Hesap bakiyeniz ", hesap_bakiye, "TL")
    miktar = int(input("Çekmek istediğiniz miktarı girin."))

    yeni_bakiye = para_çek(hesap_bakiye, miktar)
    print(f"işlem başarılı.")
    print(f"Çekilen miktar:", miktar, " TL")
    print(f"Kalan bakiye: {yeni_bakiye} TL")

except ValueError as hata:
    print(f"Hata oluştu", hata)
finally:
    print("İşlem sonlandı.")