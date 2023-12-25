# İSÜ BANKA HESABI PROJESİ -- KEMAL DEMİR 222016715 Bilgisayar Programcılığı ASIL PROJE
p = "İyi günler Dileriz"
sozluk1 = {"isim1": "Ahmet", "pas1": 1234, "bakiyeA": 100,
 "isim2": "Zeynep", "pas2": 4321, "bakiyeZ": 200,
 "isim3": "Alberto", "pas3": 4422, "bakiyeL": 300}
sozluk2 = [{"withdrawA": [], "depositA": [], "eftA": [],
 "withdrawZ":[], "depositZ": [], "eftZ": [],
 "withdrawL":[], "depositL": [], "eftL": []}]
# Hesap bilgisi kısmında tarih ve saat için eklenilen kısım.
from datetime import datetime # https://python.sitesi.web.tr/python-datetime.html
t = datetime.now()
t = (t.strftime("%x %X"))
def main():
 print("——— İSTİNYE Bank'a Hoş Geldiniz (v.0.3) ———")
 print(" ——————— " + t + " ————————")
 islemler = input("1-Giriş \n2-Çıkış ")
 if islemler == "2":
  print(p)
  exit() # https://codeberryschool.com/blog/en/how-to-end-a-program-in-python/
 elif islemler == "1":
  ka = input("Lütfen Kullanıcı Adınızı Girin ") # ka = kullanıcıadı
  pas = int(input("Lütfen Şifrenizi Girin ")) # pas = password
 if sozluk1["isim1"] != ka != sozluk1["isim2"] != ka != sozluk1["isim3"]: # Kullanıcı adları "ka"'ya eşit değilse yazdır.
  print("Sistemde Böyle bir kullanıcı kayıtlı değildir")
  print(" ")
 main()
 if ka == sozluk1["isim1"]:
   if pas != 1234:
    print("Şifreniz Hatalı. Lütfen Tekrar Deneyiniz")
   print(" ")
 main()
 if ka == sozluk1["isim2"]:
  if pas != 4321:
   print("Şifreniz Hatalı. Lütfen Tekrar Deneyiniz")
 print(" ")
 main()
 if ka == sozluk1["isim3"]:
  if pas != 4422:
   print("Şifreniz Hatalı. Lütfen Tekrar Deneyiniz")
   print(" ")
 main()

 else:
  print("Sisteme Hoş Geldiniz")

 def main2():
  print(" ")
  print("Merhaba " + str(ka))
 islemlerr = input(
 "Lütfen Yapmak İstediğiniz İşlemi Seçin \n1- Para Yatırma \n2- Para Çekme \n3- Para Transferi "
 "\n4- İşlem Geçmişi \n5- Hesap Detayları \n6- Çıkış")
 if islemlerr == "6":
 main()
 if islemlerr == "1": # PARA YATIRMA
 deposit = int(input("Lütfen Yatırmak istediğiniz Para Miktarını Girin: "))
 def toplama():
 if ka == sozluk1["isim1"]:
 sozluk1["bakiyeA"] += deposit
 sozluk2[0]["depositA"].append(t + " Tarihinde Hesabınıza " + str(deposit) + " TL Para Yatırıldı")
 return sozluk1["bakiyeA"]
 elif ka == sozluk1["isim2"]:
 sozluk1["bakiyeZ"] += deposit
 sozluk2[0]["depositZ"].append(t + " Tarihinde Hesabınıza " + str(deposit) + " TL Para Yatırıldı")
 return sozluk1["bakiyeZ"]
 else:
 sozluk1["bakiyeL"] += deposit
 sozluk2[0]["depositL"].append(t + " Tarihinde Hesabınıza " + str(deposit) + " TL Para Yatırıldı")
 return sozluk1["bakiyeL"]
 print("Yatırdığınız Para Sonucu Mevcut Hesap Bakiyeniz: " + str(toplama()) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "Evet":
 main2()
 else:
 main()
 if islemlerr == "2": # PARA ÇEKME
 withdraw = int(input("Lütfen Çekmek İstediğiniz Para Miktarını Girin: "))
 if ka == sozluk1["isim1"]:
 if withdraw <= sozluk1["bakiyeA"]:
 sozluk1["bakiyeA"] -= withdraw
 sozluk2[0]["withdrawA"].append(t + " Tarihinde Hesabınızdan " + str(withdraw) + " TL Para Çekildi")
 print("Hesabından {} TL Para Çekilmiştir. Mevcut Hesap Bakiyeniz {}".format(withdraw, sozluk1[
 "bakiyeA"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeA"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 elif ka == sozluk1["isim2"]:
 if withdraw <= sozluk1["bakiyeZ"]:
 sozluk1["bakiyeZ"] -= withdraw
 sozluk2[0]["withdrawZ"].append(t + " Tarihinde Hesabınızdan " + str(withdraw) + " TL Para Çekildi")
 print("Hesabından {} TL Para Çekilmiştir. Mevcut Hesap Bakiyeniz {}".format(withdraw, sozluk1[
 "bakiyeZ"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeZ"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 elif ka == sozluk1["isim3"]:
 if withdraw <= sozluk1["bakiyeL"]:
 sozluk1["bakiyeL"] -= withdraw
 sozluk2[0]["withdrawL"].append(t + " Tarihinde Hesabınızdan " + str(withdraw) + " TL Para Çekildi")
 print("Hesabından {} TL Para Çekilmiştir. Mevcut Hesap Bakiyeniz {}".format(withdraw, sozluk1[
 "bakiyeL"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeL"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 if islemlerr == "3": # TRANSFER İŞLEMİ
 if ka == sozluk1["isim1"]:
 menu = input("Lütfen Kişilerinizden Para Yollamak istediğiniz Kişiyi Seçin \nKişilerinizde kayıtlı "
 "olan kişiler;\n1- Zeynep \n2- Alberto \n5- Çıkış ")
 if menu == "5":
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 if menu == "1": # AHMET, ZEYNEP'E PARA ATARSA;
 eft = int(input("Lütfen Transfer Etmek İstediğiniz Bakiyeyi Giriniz: "))
 if eft <= sozluk1["bakiyeA"]:
 sozluk1["bakiyeA"] -= eft
 sozluk1["bakiyeZ"] += eft
 sozluk2[0]["eftA"].append(t + " Tarihinde Hesabınızdan " + str(eft) + " TL Para {}"
 " Adlı Kullanıcıya Transfer Edildi.".format(sozluk1["isim2"]))
 print("Hesabından {} TL Para, {} Adlı Kişiye Transfer Edilmiştir. "
 "Mevcut Hesap Bakiyeniz {}".format(eft, sozluk1["isim2"], sozluk1["bakiyeA"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeA"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 elif menu == "2": # AHMET, ALBERTO'YA PARA ATARSA;
 eft = int(input("Lütfen Transfer Etmek İstediğiniz Bakiyeyi Giriniz: "))
 if eft <= sozluk1["bakiyeA"]:
 sozluk1["bakiyeA"] -= eft
 sozluk1["bakiyeL"] += eft
 sozluk2[0]["eftA"].append(
 t + " Tarihinde Hesabınızdan " + str(eft) + " TL Para {}"
 " Adlı Kullanıcıya Transfer Edildi.".format(sozluk1["isim3"]))
 print("Hesabından {} TL Para, {} Adlı Kişiye Transfer Edilmiştir. "
 "Mevcut Hesap Bakiyeniz {}".format(eft, sozluk1["isim3"], sozluk1["bakiyeA"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeA"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 if ka == sozluk1["isim2"]:
 menu = input("Lütfen Kişilerinizden Para Yollamak istediğiniz Kişiyi Seçin \nKişilerinizde kayıtlı "
 "olan kişiler;\n1- Ahmet \n2- Alberto \n5- Çıkış ")
 if menu == "5":
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 if menu == "1": # ZEYNEP, AHMET'E PARA ATARSA;
 eft = int(input("Lütfen Transfer Etmek İstediğiniz Bakiyeyi Giriniz: "))
 if eft <= sozluk1["bakiyeZ"]:
 sozluk1["bakiyeZ"] -= eft
 sozluk1["bakiyeA"] += eft
 sozluk2[0]["eftZ"].append(t + " Tarihinde Hesabınızdan " + str(eft) + " TL Para {}"
 " Adlı Kullanıcıya Transfer Edildi.".format(sozluk1["isim1"]))
 print("Hesabından {} TL Para, {} Adlı Kişiye Transfer Edilmiştir. "
 "Mevcut Hesap Bakiyeniz {}".format(eft, sozluk1["isim1"], sozluk1["bakiyeZ"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeZ"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 elif menu == "2": # ZEYNEP, ALBERTO'YA PARA ATARSA;
 eft = int(input("Lütfen Transfer Etmek İstediğiniz Bakiyeyi Giriniz: "))
 if eft <= sozluk1["bakiyeZ"]:
 sozluk1["bakiyeZ"] -= eft
 sozluk1["bakiyeL"] += eft
 sozluk2[0]["eftZ"].append(t + " Tarihinde Hesabınızdan " + str(eft) + " TL Para {}"
 " Adlı Kullanıcıya Transfer Edildi.".format(sozluk1["isim3"]))
 print("Hesabından {} TL Para, {} Adlı Kişiye Transfer Edilmiştir. "
 "Mevcut Hesap Bakiyeniz {}".format(eft, sozluk1["isim2"], sozluk1["bakiyeA"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeZ"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 if ka == sozluk1["isim3"]:
 menu = input("Lütfen Kişilerinizden Para Yollamak istediğiniz Kişiyi Seçin \nKişilerinizde kayıtlı "
 "olan kişiler;\n1- Ahmet \n2- Zeynep \n5- Çıkış ")
 if menu == "5":
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
  main2()
 else:
 main()
 if menu == "1": # ALBERTO, AHMET'E PARA ATARSA;
 eft = int(input("Lütfen Transfer Etmek İstediğiniz Bakiyeyi Giriniz: "))
 if eft <= sozluk1["bakiyeL"]:
 sozluk1["bakiyeL"] -= eft
 sozluk1["bakiyeA"] += eft
 sozluk2[0]["eftL"].append(t + " Tarihinde Hesabınızdan " + str(eft) + " TL Para {}"
 " Adlı Kullanıcıya Transfer Edildi.".format(sozluk1["isim1"]))
 print("Hesabından {} TL Para, {} Adlı Kişiye Transfer Edilmiştir. "
 "Mevcut Hesap Bakiyeniz {}".format(eft, sozluk1["isim1"], sozluk1["bakiyeL"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeL"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 elif menu == "2": # ALBERTO, ZEYNEP'E PARA ATARSA;
 eft = int(input("Lütfen Transfer Etmek İstediğiniz Bakiyeyi Giriniz: "))
 if eft <= sozluk1["bakiyeL"]:
 sozluk1["bakiyeL"] -= eft
 sozluk1["bakiyeZ"] += eft
 sozluk2[0]["eftL"].append(t + " Tarihinde Hesabınızdan " + str(eft) + " TL Para {}"
 " Adlı Kullanıcıya Transfer Edildi.".format(sozluk1["isim2"]))
 print("Hesabından {} TL Para, {} Adlı Kişiye Transfer Edilmiştir. "
 "Mevcut Hesap Bakiyeniz {}".format(eft, sozluk1["isim2"], sozluk1["bakiyeL"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 else:
 print("Hesabında Yeterli Para Mevcut Değil. Mevcut Hesap Bakiyeniz {}".format(
 sozluk1["bakiyeL"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 if islemlerr == "4": # İŞLEM GEÇMİŞİ
 print(" ")
 print("Kullanıcı Aktivite Raporu")
 print(" ")
 print("---Para Yatırma Aktiviteleri---")
 if ka == sozluk1["isim1"]:
 print(sozluk2[0]["depositA"])
 elif ka == sozluk1["isim2"]:
 print(sozluk2[0]["depositZ"])
 else:
 print(sozluk2[0]["depositL"])
 print(" ")
 print("---Para Çekme Aktiviteleri---")
 if ka == sozluk1["isim1"]:
 print(sozluk2[0]["withdrawA"])
 elif ka == sozluk1["isim2"]:
 print(sozluk2[0]["withdrawZ"])
 else:
 print(sozluk2[0]["withdrawL"])
 print(" ")
 print("---Para Transferi Aktiviteleri---")
 if ka == sozluk1["isim1"]:
 print(sozluk2[0]["eftA"])
 elif ka == sozluk1["isim2"]:
 print(sozluk2[0]["eftZ"])
 else:
 print(sozluk2[0]["eftL"])
 print(" ")
 print(" ")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 if islemlerr == "5": # HESAP BİLGİLERİ
 print(" ")
 print(" ")
 print("——————— İSTİNYE Bank ———————")
 print("–————" + t + "-—————")
 print("————————————————————————————")
 print(" ")
 print("İsminiz: " + ka)
 print("Şifreniz: " + str(pas))
 if ka == sozluk1["isim1"]:
 print("Bakiyeniz: " + str(sozluk1["bakiyeA"]) + " TL")
 print(" ")
 elif ka == sozluk1["isim2"]:
 print("Bakiyeniz: " + str(sozluk1["bakiyeZ"]) + " TL")
 else:
 print("Bakiyeniz: " + str(sozluk1["bakiyeL"]) + " TL")
 e = input("İşleme Devam Etmek İster misiniz? (Evet Hayır)")
 if e == "Evet" and "evet":
 main2()
 else:
 main()
 main2()
main()