# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:45:28 2025

@author: user
"""

print("Hello World")
print("Murod endi o'zini tarixini yozmoqchi")
print("""Yaxshi otga bir qamchi,
yomon otga ming qamchi""" )
print('''yaxshi otga bir qamchi ,
yomon otga ming qamchi''')
print('Assalomu alaykum')
print(2+4*2)
print(2**4)
print("""Murod
Rafiqjonov""")
print("""Murod
Rofiqjonov
Roziqovich""")
#Agar matnni bir nechta qatorlarga bo'lib yozish talab qilinsa """ """ ''' '''bilan yozish talab qilinadi
#Buni ikkinchi usuli ham bor, qatorni oxirida \n belgisini qo'yish
print("Murod\nRofiqjonov")
print("Murod\nva\nAziz\njo'ralar ")
print("Men \"Dell\" Markazidan noutbuk sotib oldim")
print("Men \"Dell\" markali noutbuk sotib oldim")
print(225*5)
print(19/5)
print(19//5)
print(128/32)
print(128//32)
#python matematik amallarni oddiy o'zining qonunida amalga oshiradi ,bo'lish uchun "/" dan 
#ko'paytirish uchun esa * amalidan foydalanamiz 
# E'tibor bersangiz / bo'lish amalidan foydalanganimizda python bo'lgan paytida butun son chiqgan paytida ham ".0" ni qoldiradi 
# Masalan print(32/4) deb buyruq berganda consolda >>> 8.0 deb chiqadi buni yo'qotish uchun '//' 2 ta bo'luv belgisidan foydalanish kerak
# Hatto qoldiq qoladigan amal bo'lsa ham qoldiq qolmaydi 
print(128//7)
print(5**3)
#Pythonda '**'belgisi sonning darajasini anglatadi masalan print(2**4) deb buyruq bersak consolda >>> 16 deb chiqadi
print(2**4)
print("O'nning kvadrati" ,10**2," ga teng ")
print("o'nni 135 ga ko'paytirsak" ,10*135," bo'ladi")
print("28 ni 85 ga ko'paytirsak" ,28*85,"bo'ladi")
#print() yordamida matn va ifodalarni ham jamlab ketish mumkin buning uchun har bir ifoda va matn vergul bilan ajratiladi
print("8 kara 8",2**6,"ga teng" )
#pythonda bo'linmani qoldigini olish % belgisi bilan amalga oshiriladi 
print(15%6)
print(2*5*3.14159)
#Radiusi 5 ga teng aylana uzunligi :print(2*3.14159*5)
# quyidagi matnni aynan shunday ko'rinishda chiqaring
# "NExia", "Tico" , 'Damas' ko'rganlar qilar havas.
print('"Nexia","Tico" , \'Damas\' ko\'rganlar qilar havas.')
# 5ning 4 darajasi 625 
print("5 ning 4 darajasini toping ?\n5 ning 4 darajasi" ,5**4,"ga teng <_>")
# Savol: 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print("22 ni 4 ga bo'lganda qancha qoldiq qoladi ?\n22 ni 4 ga bo'lsak",22//4,"qoldiq yo'q <_> :)")
# Savol tomonlari 125 ga teng bo'lgan kvadratni yuzi va perimetrini toping.
print("Tomonlari 125 ga teng bo'lgan kvadratni perimetri" ,125*4,"ga va yuzi esa" ,125**2," metr kvadratga teng") 
# Bu yerda kvadratni perimetri P=4a , bu yerda a=kvadratni bir tomoni 
# Kvadratni yuzi esa S=a^2 a- kvadratni tomoni 
#Savol: Diametri 12 ga teng bo'lgan doiraning yuzini toping p=3.14
# Agar diametr 12 ga teng bo'lsa demak doiranig radiusi 6 ga teng , doiraning yuzini formulasi S=PR^2
print("Diametri 12 ga teng bo'lgan doirani yuzi" ,3.14*6**2,"ga teng")
# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping. Pifagor teoremasi c=a^2 + b^2) 
import math
print('Katetlari 6 va 7 bo\'lgan to\'g\'ri burchakli uchburchakning gipotenuzasi-',math.sqrt(6**2+7**2),'ga teng')
print(math.sqrt(16))
ism="Abdulloh"
yosh="25"
print(ism)
print(yosh)
ism="Murodjon"
print(ism)
# ism bu o'zgaruvchi uni xohlagan payt o'zartirish mumkin , o'zgaruchilarni katta va kichik harflari har xil talqin qilinadi 
# ism ,ISM Ism bu uchta turli xil o'zgaruvchi , o'zgaruvchilarni tushunarli qilib nomlash kerak y=20 emas yosh=20
# O'zgaruvchilarda faqat lotin alifbosi , (a-z) raqamlar (1-9) va (_) pastgi chiziq qatnashishi mumkin ism_sharif="Murod Rafiqjonov"
# O'zgaruvchilarda 2 dan ko'p so'z qatnashsa pastgi chiziq bilan ajrating 
# Uyga vazifa 
salom_dunyo="Helllo World"
print(salom_dunyo)
xabar='Tramp qayta prezident bo\'ldi'
print(xabar)
xabar="Putin Trampni tabrikladi"
print("Putin Trampni tabrikladi")
print(xabar)
radius=5
pi=3.14159
yuza=pi*radius**2
print("Radiusi", radius,"ga teng doira yuzi", yuza,"ga teng")
print(" I bought this Iphone yesterday 📱")
print(" I love coding.....")
ism="Murodjon"
print("salom mening ismim "+ ism)
ism="Murodjon"
familiya="Rofiqjonov"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)
print("My fullname is",ism_sharif)
print(f"My name is {ism} and my lastname is {familiya}")
print(ism + " " + familiya  )
# Matnlar bilan ishlash 
# Ikki va undan ortiq o'zgaruvchilarni birlashtirish uchun f-string usulidan foydalanamiz  f" {1-o'zgaruvchi}  {2-o'zgaruvchi}"
# Bu usul yordamida uzun matnlarni ham yasash mumkin 
fname="Bond"
lname="James"
print(f"Salom mening ismim {fname}.{lname} {fname} ! <_>")
yil=2004
print(2025-yil)
print(f" Agar sizning tug'ilgan yilingiz {yil}-yil bo'lsa siz hozir {2025-yil} yoshdasiz")
print("Hello world")
print(ism_sharif)
tyil=1998
print(f"Agar siz {tyil}-da tug'ilgan bo'lsangiz, Siz hozir {2025-tyil} yoshdasiz")
# Maxsus belgilar 
# print bilan kod yozayotganda "\t" bilan joy tashlasa bo'ladi , \n bilan esa boshqa qatorga o'tsa bo'ladi 
print("Hello \t world!")
print("Hello \nworld")
# Matnlar bilan ishlash 
# Metodlar- bu o'zgaruvchilarda  va matnlarda to'g'ridan to'g'ri o'zgartirish kiritadigan funsiya 
# Metodlar matnni oxiriga .metod_nomi() bilan kiritiladi
# upper() lower() metodlari
ism="Murodjon"
familiya="Rofiqjonov"
ism_familiya=f"{ism} {familiya}"
print(ism_familiya.upper())
ism_familiya=ism_familiya.upper()
print(ism_familiya.lower())
# upper() metodi har bir harfni bosh harfga o'zgartiradi lower() esa teskarisi , kichiik harflarga 
# title() va capitalize() metodlari 
name="anvar"
last_name="narzullayev"
name_and_last=f"{name} {last_name}"
print(name_and_last.title())
print(name_and_last.capitalize())
# "title()" metodi  matndagi har bir harfni bosh harfi bilan yozadi
# " capitalize" metodi esa matndagi birinchi so'zni bosh harf bilan yozadi 
# Metodlarni nafaqat o'zgaruvchilarga , balki matnlarga ham qo'llasa bo'ladi ,aslida o'zgaruvchi biror matnni (yoki qimatni) manzili xolos 
print("assalomu alaykum".title())
print("assalomu alaykum!".title())
print("james bond".capitalize())
print("james bond".title())
# strip() matn boshidagi va oxiridagi bo'shliqlarni olib tashlaydi 
# rstrip() matn oxiridagi bo'shliqlarni olib tashlaydi 
# lstrip() essa matn boshidagi bo'shliqlarni olib tashlaydi 
brat="       Aziz       "
print("Salom", brat.strip())
print("Salom", brat.rstrip() )
print("Salom", brat.lstrip())
print(" Assalomu    Alaykum    qandaysiz  ? ".strip())
salom="Assalmu    alaykum     qandaysiz   ?"
print(salom.strip())
meva="         olma           "
print(meva.strip())
#naming=input("Ismingiz nima ?")
#print("Assalomu Alaykum ", naming)
#naming=input("Salom, ismingizni kiriting:\n>>>>> ")
#print("Assalomu Alaykum", naming.title())
print(salom_dunyo)
# Integers-butun sonlar , musbat , manfiy yoki 0 ga teng bo'lishi mumkin  
a=20   # int-butun son
b= -10  # manfiy va butun son
c=0
d=a+b
print(d)
q=5.5 # O'nlik sonlar float deb ataladi , buni to'liq qiib floating point numbers , suzuvchi o'nik sonlar deb ataladi , 
# Ingliz tilida o'lik sonlar biznikidek vergul bilan emas nuqta blan ajratiladi , ular qiymatiga qarab joyi o'zgargani uchun floating-suzuvchi deb aytilgan 
aholi_soni= 39_561_200 # Pyhtonda juda katta sonlarni "_" pastgi chiziqcha bilan o'ziga tushunarli qilib ajratish mumkin , buni qiymatga dahli bo'lmaydi 
print(aholi_soni)
pi=3.14159
radius=15
diametr=radius*2
aylana_uzunligi=diametr*pi
print(aylana_uzunligi) 
a=2
b=8.0
c=a+b
print(c) 
print(a*b) # butun va o'nlik sonlar bilan bajariladigan barcha arifmetik  amallar qiymati  pythonda o'nlik son bilan chiqadi 
print(a**b)
# Uzun sonlarni kiritishda pythonda sonlarni (_) pastgi chiziq bilan kiritish mumkin , python buni inobatga olmaydi
aholi_soni= 38_333_251
print(f"O'zbekistonda aholi soni-{aholi_soni} taga yetdi")
PI=3.14159
# KONSTANTA - python tilida aniq bir konstanta yo'q , ammo butun dunyoda dasturchilar konstantani katta harflar bilan yozishga keishgan masalan PI=3.14159
# agar PI=3.14159 deb konstanta bersak uni Variable explorer jadvalida ko'rsatmaydi ,ammo molcha python ni qabul qiladi , va uni consolga buyruq berib chiqarish mumkin 
print(PI)
x,y,z=3,4,5
# Bir nechta qiymatlarni birdaniga berish uchun - har bir o'zgaruvchi va qiymatlarni (,) vergul bilan ajratamiz
yosh,name,yil=20,"murod",2004
print(f"Assalomu alaykum Mening ismim {name.title()} ,{yil}-yilman va yoshim {yosh} da")
ism="Jobir"
yosh=16
xabar= ism + " " + str(yosh) + " yoshda"
print(xabar)
ism="murodjon"
yosh=20
xabar= ism.title() + " " +  str(yosh) + " yoshda"
print(xabar)
# pythonda str() matnni va int(), float() butun va o'nlik sonlarni qo'shib bo'lmaydi , buning uchun ikkalasini yo str , yoki int yoki float bo'lishi kerak 
# bularni bir biriga mos qilish uchun har xil funksiyalar bor 
# str() int yoki floatturidagi sonlarni matn ko'rinishida qaytaradi
# int() string yoki float ko'rinishidagi qiymatlarni butun songa qaytaradi , bunda matn butun son ko'rinishida berilishi kerak 
# float() str yoki int ko'rinishidagi qiymatlarni o'nlik son ko'rinishida beradi 
mevalar=["Olma","Anor","Anjir","Uzum","Xurmo","Behi","Nok"]
print(meva)
print(meva[0])
print(meva)
# List- ro'yxatlar , biz o'zgaruvchilarga har bittasiga faqat bitta qiymat berayotgan edik , list-ro'yxat yordamida esa bitta qiymat emas,bir nechta qiymat ham bersa bo'ladi
#Ro'yxat yasashimiz uchun [] to'rtburchak qavs bilan foydalanamiz , va har bir qiymatni (,) vergul bilan ajratishimiz kerak , qo'shilib ketmaslik uchun qiymatlarni
mevalar=["Olma","shaftoli","o'rik","Banan", "Uzum" ,"Anjir" ]
print(mevalar)
narxlar=[32900,21300,56000,40000]
print("Birinchi meva ",mevalar[0])
print("Ikkinchi meva ",mevalar[1] )
mevalar[-1]="Apelsin"
print(mevalar)
print("Ro'xatdagi uchinchi meva bu ",mevalar[2].capitalize())
print("Ro'xatdagi uchinchi meva bu ",mevalar[2].upper())
cars=["BMW","Mercedes","Tesla","Alfa Rameo","Lamborghini" ,"BYD" ,"Jetour"]
del cars[-2]
print(cars)
print(cars)
cars.remove("Jetour")
# Ro'yxatlarga .append() funksiyasi orqali qiymatlarni ro'yxatni oxiriga qo'shsa bo'ladi 
noutbuk_markalari=['HP','Makbuk','Samsung','Lenovo','Toshiba','LG']
noutbuk_markalari.append('Dell')
print(noutbuk_markalari)
del noutbuk_markalari[4]
print(noutbuk_markalari)
noutbuk_markalari.remove('LG')
print(noutbuk_markalari)
noutbuk_markalari.append('LG')
print(noutbuk_markalari)
noutbuk_markalari.insert(0,'Makbuk')
print(noutbuk_markalari)
noutbuk_markalari.remove('Makbuk')
print(noutbuk_markalari)
noutbuk_markalari.remove('Makbuk')
print(noutbuk_markalari)
noutbuk_markalari.insert(-1,'Makbuk')
print(noutbuk_markalari)
noutbuk_markalari.insert(-0,'Toshiba')
print(noutbuk_markalari)
noutbuk_markalari.append('Asus')
print(noutbuk_markalari)
noutbuk_markalari.insert(2,'Acer')
print(noutbuk_markalari)
noutbuk_markalari.remove('Makbuk')
print(noutbuk_markalari)
noutbuk_markalari.insert(0,'Macbook')
print(noutbuk_markalari)
del noutbuk_markalari[1]
print(noutbuk_markalari)
kerakli_tovarlar=['Muqaddima kitobi','Espander','Bloknot','Powerbank']
mahsulot=kerakli_tovarlar.pop(1)
print('Men u kuni ' + mahsulot+ 'ni Temudan sotib olgan edim')
print('Qolgan tovarlar esa -',kerakli_tovarlar )
# .pop() funksiyasi yordamida ro'yxatdagi qiymatlardan birini sug'urib olib biror boshqa o'zgaruvchiga joylasa bo'ladi 
telefonlar=['Apple','Samsung','Xiaomi','Nokia','ZTE','Huawei',"Infinix",'Oppo']
telefon=telefonlar.pop(1)
print('Men 2021-yilda ' +telefon+' A31 telefon markasini sotib olgan edim')
print(telefonlar)
# Agar .pop() index siz beradigan bo'lsayiz ro'yxatni oxiridagi qiymatni sug'urib olib beradi , pastga qarang ! 
xohlaganim=telefonlar.pop()
print("Men "+xohlaganim+" telefon markasidan olishni xohlayman" )
#AMALIYOT
# Ismlar degan ro'yxat tuzing va kamida 3 ta yaqin do'stingizni ismini kiriting 
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib consolga chiqaring
ismlar=["Aziz","Sunnat","Aziz sinfdosh","Muxammadali"] 
print("Salom "+ismlar[3]+ " yaxshimisan jo'ra ?")
print(ismlar[0] + ' va ' + ismlar[2] + ' eski hamsoyalar' )
print([ismlar[1]+ ' g\'ildirakni g\'izilllatib g\'ildiratdi '])
sonlar=[12, 17 , 10.5, 20.6, -6 ]
print(sonlar[1] + sonlar[2])
print(sonlar[0]+sonlar[-1])
sonlar.insert(4,20.6)
print(sonlar)
del sonlar[4]
print(sonlar)
del sonlar[3]
print(sonlar)
sonlar.insert(3,17)
print(sonlar)
sonlar[1]=18
print(sonlar)
sonlar[2]=2004
del sonlar[4]
print(sonlar)
sonlar.append(20)
print(sonlar)
sonlar.append(21)
print(sonlar)
sonlar.append("Murod")
print(sonlar)
del sonlar[-1]
print(sonlar)
sonlar.insert(0,2003)
print(sonlar)
t_shaxslar=['Imom Al-Buxoriy','Alisher Navoiy ','Amir Temur','Imom G\'azolliy']
z_shaxslar=['Anvar Narx']
# son=(input("Istalgan soningizni kiriting:\n>>> "))
# son=int(son)
# if son>0 :
#     print("Kiritgan soningiz musbat.")
# else:
#     print("Kiritgan soningiz manfiy.")
# istalgan_son=int(input("Birorta random son kiriting:\n>>>> "))
# if istalgan_son>0:
#     print(int(istalgan_son**0.5))
# else:
#     print("Berilgan sonni ildizini hisoblash uchun musbat son \
# kiriting")
#  Kiritilgan sonning toq yoki juftligini konsolga chiqaruvchi dastur yozing 


# if va else yordamida biz faqat bitta shartni tekshirishimiz mumkin , if-elif-else yordamida esa biz bir nechta shartlarni tekshira olamiz
# if bilan boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin 
# son=int(input("Istalgan son kiriting:\n>>>"))
# if son>0:
#     print("Kiritgan soningiz musbat.")
# elif son==0 :
#     print("Kiritgan soningiz 0 ga teng.")
# else:
#     print("Kiritgan soningiz manfiy")
# yosh=int(input("Bu atraksionga kirish uchun yoshingizni ayting:\n>>> "))
# if 18<yosh<50 :
#     print("Sizni kirish chiptangiz narhi 20000 so'm")
# elif yosh<18 :
#     print("Sizga kirish mumkin emas,siz hali voyaga yetmagansiz")
# elif yosh>50 :
#     print("Sizga kirish mumkin emas yoshingiz katta, yuragingiz ko'tarmasligi mumkin.")
# narx=41000
# choy=True
# salat=True
# assorti=False
# coca_cola=False
# zero_cola=True
# kompot=False
# if choy :
#     print("Mijoz choy oldi")
#     narx=narx +6000
# if salat :
#     print("Mijoz salat oldi")
#     narx=narx+8000
# if assorti :
#     print("Mijoz salat oldi")
#     narx=narx+15000
# if coca_cola :
#     print("Mijoz coca cola oldi")
#     narx=narx + 10000
# if zero_cola :
#     print("Mijoz zero cola oldi")
#     narx=narx+9000
# if kompot :
#     narx=narx+8000
#     print("Mijoz kompot oldi")
# print(f"Jami narx {narx} so'm bo'ldi hurmatli mijoz ")
# menyu=['Qozon kabob','Shashlik','Manti','Somsa','Norin']
# 'Manti' in menyu # menyuda manti bormi
# menyu=['Qozon kabob','Shashlik','Manti','Somsa','Norin']
# ovqat=input('Assalomu alaykum hurmatli mijoz , nima ovqat yeysiz \n >>> ')
# if ovqat.capitalize() in menyu :
#     print("Buyurtma qabul qilindi")
# else :
#     print("Afsuski bizning menyuda bunday taom yo'q -_-") 
menyu=['Qozon kabob','Shashlik','Manti','Somsa','Norin']
# not in operatori yordamida biz biror element yo'qligini tekshirishimiz mumkin
'Osh' not in menyu  # True deb out berdi , chunki Osh menyuda bor 
'Somsa' not in menyu # False deb out berdi chunki Somsa menyuda bor 
for taom in menyu :
    print(taom.lower())
# menyu=['Qozon kabob','Shashlik','Manti','Somsa','Norin']
# buyurtmalar=['Shashlik','Norin','Somsa','Osh']
# for food in buyurtmalar :
#     if food in menyu:
#         print(f"Menyuda {food} bor")
#     else:
#         print(f"Afsuski {food} bizning menyuda yo'q -_-")(
car={'model':'BMW','colour':'blue'}
kalit=car.get('kalit','Bunday mashina mavjud emas')
print(kalit)
print("Hello World")
friedns=['Aziz Sattorov','Aziz Raimov','Aziz-Asl','Javohir']
print(friedns[0])
for friend in friedns :
    print("Assalomu Alaykum",friend)
    print("Xush Kelibsiz")
mehmonlar=[]
for n in range(5):
    mehmonlar.append(input(f"{n+1}- mehmonni kiriting "))
print(mehmonlar)
























    