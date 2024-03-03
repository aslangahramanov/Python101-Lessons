# a=int(input("1-ci Ədədi daxil edin: "))
# b=int(input("2-ci Ədədi daxil edin: "))

# sum="Toplama +"
# cix="Çıxma -"
# vur="Vurma x"
# bol="Bölmə /"

# print(sum + "\n" + cix + "\n" + vur + "\n" + bol)

# emel=input("Əməliyyatı daxil edin: ")

# if emel in sum :
#     print("Ədədlərin Cəmi= ",(a+b))

# elif emel in cix:
#     print("Ədədlərin Fərqi= ",(a-b))

# elif emel in vur:  
#     print("Ədədlərin hasili= ",(a*b))

# elif emel in bol:
#     if a!=0 and b!=0:
#         print("Ədədlərin qisməti= ",(a/b))
#     else:
#         print("0 a Bölmək mümkün deyil!")

# else:
#     pass



# -----------------------------------------------------------------------------------------



# a=input("Adınızı qeyd edin: ")
# b=input("Soyadınızı qeyd edin: ")
# c=input("Yaşınızı qeyd edin: ")

# print("Ad: ",a + "\n" + "Soyad: ",b + "\n" + "Yaş: ",c)


# -----------------------------------------------------------------------------------------



# ad = "Seyfeddin"
# soy = "Memmedov"
# hobbi = ["Football", "Music", "Movie"]

# a = len(ad)
# b = len(soy)
# c = len(hobbi)

# print("Ad ", a, "\nSoyad ", b, "\nHobbi ", c)

# -----------------------------------------------------------------------------------------

# a = 65

# print(type(a))

# b=str(a)

# print(type(b))

# -----------------------------------------------------------------------------------------


# a="2"

# print(type(a))

# b=int(a)

# print(type(b))


# -----------------------------------------------------------------------------------------


# a=2.25

# print(type(a),a)

# b=int(a)

# print(type(b),b)


# ----------FOR AND IF ------------------------------1-------------------------------------

# for eded in range(1, 11):

#     if eded % 2 == 0:

#         print( eded," - Cüt ədəddir.")

#     else:

#         print( eded," - Tək ədəddir.")

# --------------------------------------2--------------------------------------------------

# name=input("Adınızı daxil edin: ")
# age=int(input("Yaşınızı daxil edin: "))

# if age<18:
#     print( f"Hörmətli {name}, siz giriş etmək hüququna malik deyilsiniz!")

# else:
#     print(f"Hörmətli {name},müvəfəqqiyətlə giriş etdiniz!")

# --------------------------------------3--------------------------------------------------

# data = {"name": "Salman", "surname": "Ahmedov", "email": "salam@gmail.com", "password": "salam"}

# a=data.get("email")
# b=data.get("password")

# mail=input("Email daxil edin:")
# passw=input("Kodu daxil edin:")

# if a==mail and b==passw:
#     print("Xoş Gəldiniz {} {}".format(data.get("name"),data.get("surname")))

# else:
#     print("Daxil etdiyiniz məlumatlar yanlışdır!")

# --------------------------------------4--------------------------------------------------

# info=input("Məlumatı daxil edin :")

# width=len(info)

# print(width)

# if width % 2 == 0:
#     print("Daxil etdiyiniz məlumatın simvol sayı CÜTDÜR!")
# else:
#     print("Daxil etdiyinz məlumatın simvol sayı TƏKDİR!")
 
# ---------------------------------------5-------------------------------------------------

# 1 ci Üsul

# sum=0


# for i in range(16):
    
#     sum=sum+i

#     print(sum)


# 2 ci Üsul

# print(sum(list(range(16))))

# ---------------------------------------6-------------------------------------------------

# numbers=input("Vergül qoymaqla ədədləri daxil edin: ")

# num2=numbers.split(",")
# print(num2)

# for i in (num2):
#     i=int(i)
#     print(i**2)

# ---------------------------------------7-------------------------------------------------

# text=input("Mətni Daxil edin: ")

# big_letter = sum(1 for harf in text if harf.isupper())
# small_letter = sum(1 for harf in text if harf.islower())

# print(f"Böyük hərf sayısı: {big_letter}")
# print(f"Kiçik hərf sayısı: {small_letter}")

# ------------WHILE and FORMAT---------------------------1---------------------------------

# name=input("Adınızı daxil edin: ")
# surname=input("Soyadınızı daxil edin: ")
# card=int(input("Kartın nömrəsini daxil edin: "))

# print(f"Ad: {name}")
# print(f"Soyad: {surname}")
# print(f"Kart: {card}")

# ---------------------------------------2-------------------------------------------------

# for i in range(1,11):
#     print("{:05d}".format(i))


# --------------------------------------3--------------------------------------------------

# name=input("Adınızı daxil edin: ")
# surname=input("Soyadınızı daxil edin: ")
# lang=input("Proqramlaşdırma dilini yazın: ")

# print("Salam. Mənim adım %s %s. Mən %s programlaşdırma dilini öyrənirəm" % (name,surname,lang))

# --------------------------------------4--------------------------------------------------

# Product = "Kitab"
# amount = 5
# cost = 4.5785

# print("Sizin {} {} var. Qiymeti-{:.1f} .".format(amount,Product,cost))
# cost2=float("{:.1f}".format(cost))

# print("Ümumi məbləğ: ", cost2*amount)

# --------------------------------------5--------------------------------------------------

# haqq=0

# while haqq<5:

#     numb=int(input("Ədədi daxil edin: "))


#     if not 5==numb:
        
#         print("Düzgün bilmədiniz qalan haqqınız: ",5-haqq)
#         haqq=haqq+1
#         continue
        
#     else:
#         print("Təbriklər siz düz tapdınız!")
#         break


# --------------------------------------6--------------------------------------------------

# count=0

# while count<3:
#     mail=input("Mail daxil edin: ")
#     passw=input("Parol daxil edin: ")

#     if not "@" in mail:
        
#         print("Maili duzgun daxil edin! ")
#         count+=1
#         print("Qalan haqqiniz-",3-count)
#         continue

#     elif not len(passw)>8:

#         print("Parol duzgun daxil edin! ")
#         count+=1
#         print("Qalan haqqiniz-",3-count)
#         continue

#     else:
#         print("Xos Geldiniz!")
#         break

# --------------------------------------7--------------------------------------------------

# numb=int(input("Ədədi daxil edin: "))

# fact = 1
 
# for i in range(1, numb+1):
#     fact = fact * i
 
# print(f"{numb} Faktorialı : ", fact)











# ----------------ASCİİ----------------------1---------------------------------------------

# numb=(input("Xarakteri daxil edin : "))


# print("ASCII cədvələ görə qarşılığı: " ,ord(numb))





# --------------------------------------2--------------------------------------------------

# # -------Upper-------------------------------

# txt= "Men AZERBAYCANLIYAM"

# result="M"

# for i in txt:

#     char=ord(i)

#     if 65<=char<=90:

#         result += i

#     elif char==32:
#         result = result + " "

#     else:
#         upper_ord=char-32
#         upper_char=chr(upper_ord)
#         result = result + upper_char

# print(result)




# -------Lower-------------------------------

# txt= "MeN AZERBAYcAnLiYAM!"

# result=""

# for i in txt:

#     char=ord(i)

#     if 65 <= char <=97:
#         lower_ord=char+32
#         lower_char=chr(lower_ord)
#         result += lower_char

#     elif char==32:
#         result = result + " "

#     elif 97 <= char <= 122:
#         result += i
        
    
# print(result)
        
# print(result)



# -------first char upper-------------------------------

    
    


# --------------------------------------3--------------------------------------------------

# txt=input("Cümlə daxil edin: ")

# for i in txt:

#     char=ord(i)

#     print(char)

# --------------LIST------------------------4----------------------------------------------

# data = ["School","Eat","Hand","Phone"] 
# print(data)

# -----------1

# data.append("Watch")
# print(data)

# -----------2

# data.remove("School")
# print(data)

# -----------3

# new_data = ["People", "Programming", "Football"]
# data.extend(new_data)
# print(data)
            
# -----------4

# data2=data.copy
# print(id(data))
# print(id(data2))

# -----------5

# data.insert(2,"Python")
# print(data)

# -----------6

# a=data.pop(3)
# print(data)
# print(a)

# -----------7

# new_data = ["People", "Programming", "Football"]
# print(new_data)
# new_data.remove("Football")
# print(new_data)

# -----------8

# data.clear()
# print(a)

# -----------9

# data.sort()
# print(data)

# data.reverse()
# print(data)



# prog_name = input("Programlasdirma dilini daxil edin: ")
# prog_version = input("Programlasdirma dilinin versiyasini daxil edin: ")


# # print("Men" + prog_name + prog_version + "versiyasini oyrenirem")


# full_text = "Men {1} {2} versiyasini oyrenirem".format(prog_name, prog_version)

# print(full_text)





text = "men Python 3.12 versiyasini oyrenirem"

result = ""


    
if 97 <= ord(text[0]) <= 122:
    capital_ord = ord(text[0]) - 32
    capital_char = chr(capital_ord)
    result += capital_char
    
elif 48 <= ord(text[0]) <= 57 or 65 <= ord(text[0]) <= 90:
    result += text[0]

else:
    result = "" 


    

for i in text[1:]:
    char_ord = ord(i)

    if 65 <= char_ord <= 90:
        upper_ord = char_ord + 32
        upper_char = chr(upper_ord)
        result += upper_char
        
    elif char_ord == 32:
            result += " "
        
    else:
        result += i
        
print(result)
    
    
letters = {
    "ü" : "u",
    "ö" : "o",
    "ş" : "sh",
    "ç" : "ch",
    "ğ" : 'g',
    "ı" : "i",
    "v": "w",
    "ə" : "e",
}


az_text = "Mən Python Öyrənirəm,ümumiyyətlə sizə nə"
 
en_text = ""


for i in az_text.lower():
    char = letters.get(i)
    
    if char:
        en_text += char
        
    elif i == " " or i == "," o:
        en_text += "-"
        
    else:
        en_text += i
        
        
print(en_text)