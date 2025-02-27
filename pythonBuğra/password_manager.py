from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
master_password = input("Password girişinizi yapın: ")
key = load_key() + master_password.encode()
fer = Fernet(key)
#görüntüleme
def görüntüleme():
    with open("parola.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if not data:
                continue
            user, passw = data.split("|")
            print("kullanıcı adı:" , user , "parola:" , fer.decrypt(passw.encode()))
#değiştirme(ekleme)
def ekleme():
    name = input("kullanıcı adı: ")
    password = input("parola: ")
    with open("parola.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")
while True:
    mode = input("mevcut parolanızı görüntülemek mi istersiniz yoksa yeni bir parola mı belirlemek istersiniz? (çıkm ak için k yazın.)\n").lower()
    #programdan çıkış
    if mode=="k":
        break
    #görüntüleme
    elif mode == "görüntüleme":
        görüntüleme()
    #değiştirme(ekleme)
    elif mode == "ekleme":
        ekleme()
    else:
        print("geçersiz komut")
        continue