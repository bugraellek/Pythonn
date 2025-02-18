
user_name = input("kullanıcı adınız: ")
user_msg = "hoşgeldin, {}. bugün güzel bir gün.".format(user_name)
print(user_msg)
user_age = int(input("yaşınızı giriniz: "))
user_msg2= "yaşınız, {}. 10 yıl sonra {} yaşında olacak.".format(user_age, user_age+10)
print(user_msg2)
user_nation = input("uyruk: ")
user_msg3= f"uyruğunuz, {user_nation}"
print(user_msg3)
user_wage = float(input("maaş beklentiniz: "))
user_msg4 = "maaş beklentiniz {0:8.2f}".format(user_wage)
print(user_msg4)
user_msg5 = "hoşgeldin "+user_name+" bugün güzel bir"
print(user_msg5)