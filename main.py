ytop = []
t = 0
ay = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Oğustos","Eylül","Ekim","Kasım","Aralık"]
print("Yıllık giderleri hesaplamak için sorulara yanıt veriniz. ")
for i in range(12):
    atop = []
    print(ay[t] , " ayına göre cevaplayınız.")
    atop.append(int(input("Aylık mutfak gideri: ")))
    atop.append(int(input("Aylık elektrik gideri: ")))
    atop.append(int(input("Aylık su gideri: ")))
    atop.append(int(input("Aylık doğalgaz gideri: ")))
    atop.append(int(input("Aylık alışveriş gideri: ")))
    atop.append(int(input("Aylık kırtasiye gideri: ")))
    print(" ayının toplam masrafı" , sum(atop) , "")
    ytop.append(int(sum(atop)))
    t+=1
print("Yıllık bütün harcamanız: " , sum(ytop))