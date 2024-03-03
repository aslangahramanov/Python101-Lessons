# FORMAT

# %s

# format()
# f""

# print("Salam %s %s Xos geldiniz. Sizin balansiniz %s" % ("Aslan", "Gahramanov", "25"))


# message = "Salam {0} {1}. Xos geldiniz. Sizin balansiniz {}".format("Aslan", "Gahramanov")

# message = "Salam {name} {surname}. Xos geldiniz. Sizin balansiniz {balance}".format(surname="Gahramanov", name="Aslan", balance=25)


# data = {
#     "name": "Aslan",
#     "surname": "Gahramanov",
#     "balance": 25,
# }



# message = f"Salam {data.get("name")} {data.get("surname")}. Xos geldiniz. Sizin balansiniz {data.get("balance")}"

# print("The number is:{:0d}".format(123))

# print("The float number is:{:f}".format(123))

# print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))





# # integer numbers with minimum width
# print("{:10f}".format(12))

# # width doesn't work for numbers longer than padding
# print("{:6d}".format(1234))

# # padding for float numbers
# print("{:.0f}".format(12.22962352385923897489237489732894))

# # integer numbers with minimum width filled with zeros
# print("{:020d}".format(125))

# # padding for float numbers filled with zeros
# print("{:08.2f}".format(12.2346))


# show the + sign
# print("{:+f} {:+f}".format(12.23, -12.23))

# # # show the - sign only
# print("{:-f} {:-f}".format(12.23, -12.23))

# # # show space for + sign
# print("{: f} {: f}".format(12.23, -12.23))


# integer numbers with right alignment
# print("{:5d}".format(12))

# # float numbers with center alignment
# print("{:^020.3f}".format(12.2346))

# # integer left alignment filled with zeros
# print("{:<08d}".format(11875))
# print("{:>08d}".format(11875))

# # float numbers with center alignment
# print("{:=8.3f}".format(-12.2346))


# string padding with left alignment
# print("{:5}".format("cat"))

# string padding with right alignment
# print("{:>5}".format("cat"))

# # string padding with center alignment
# print("{:^5}".format("cat"))

# # string padding with center alignment
# # and '*' padding character
# print("{:*^5}".format("cat"))


# print("{:*<9.2}".format("Aslan"))



# WHILE LOOP 

email_correct = False
password_correct = False


while not (email_correct and password_correct):
    email = input("Mailinizi daxil edin: ")
    password = input("Sifrenizi daxil edin: ")
    
    if not email and password:
        print("Email ve ya sifreni daxil etmelisiniz!")
        continue
    
    if not '@' in email:
        print("Mail duzgun daxil edilmeyib!")
        continue
        
    elif not (email.endswith(".com") or email.endswith(".net") or email.endswith(".az")):
        print("Mail yalniz '.com, .net ve .az' ile bitmelidir!")
        continue
        
    elif not len(password) >= 8:
        print("Sifre en az 8 xarakterden ibaret olmalidir!")
        continue
        
    else:
        email_correct = True
        password_correct = True
        print("Tebrikler. Siz daxil oldunuz!")
    
    
    


