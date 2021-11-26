t = "Program test aritmatika dasar"
x = t.center(45,"=")
print(x)
print("Pilihan level yang tersedia :")
print("1. Easy")
print("2. Medium")
print("3. Hard")
a = int(input("Masukkan tingkatan yang ingin anda coba : "))

def generate():
    if a == 1 :
        import random
        b = int(random.randint(20,50))
        list = ["+","-","/","*"]
        c = str(random.choice(list))
        d = int(random.randint(20,50))
        print("Berapakah hasil dari",b,c,d)
        j = float(input("Masukkan Jawaban Anda : "))
        if c == "+" :
            z = (b + d)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,"=",z)
        elif c == "-":
            z = (b - d)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,"=",z)
        elif c == "/":
            z = (b / d)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,"=",z)
        elif c == "*":
            z = (b * d)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,"=",z)
        else :
            print("Jawaban Anda Salah")
            
    elif a == 2 :
        import random
        b = random.randint(20,70)
        list = ["+","-","/","*"]
        c = random.choice(list)
        d = random.randint(20,70)
        e = random.randint(20,70)
        f = random.choice(list)
        print("Berapakah hasil dari",b,c,d,f,e)
        j = float(input("Masukkan Jawaban Anda : "))
        if (c == "+") and (f == "+") :
            z = (b + d + e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "-") and (f == "-"):
            z = (b - d - e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "/") and (f == "/"):
            z = (b / d / e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "*") and (f == "*"):
            z = (b * d * e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "+") and (f == "-") :
            z = (b + d - e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "-") and (f == "+"):
            z = (b - d + e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "/") and (f == "+"):
            z = (b / d + e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "*") and (f == "+"):
            z = (b * d + e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "+") and (f == "/") :
            z = (b + d / e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "-") and (f == "/"):
            z = (b - d / e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "/") and (f == "-"):
            z = (b / d - e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "*") and (f == "-"):
            z = (b * d - e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "+") and (f == "*") :
            z = (b + d * e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "-") and (f == "*"):
            z = (b - d * e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "/") and (f == "*"):
            z = (b / d * e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        elif (c == "*") and (f == "/"):
            z = (b * d / e)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,"=",z)
        else :
            print("Jawaban Anda Salah")
    elif a == 3 :
        import random
        b = random.randint(20,100)
        list = ["+","-","/","*"]
        c = random.choice(list)
        d = random.randint(20,100)
        e = random.randint(20,100)
        f = random.choice(list)
        g = random.randint(20,100)
        h = random.choice(list)
        print("Berapakah hasil dari",b,c,d,f,e,h,g)
        j = float(input("Masukkan Jawaban Anda : "))
        if (c == "+") and (f == "+") and (h == "+") :
            z = (b + d + e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "-") and (h == "-"):
            z = (b - d - e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "/") and (h == "/"):
            z = (b / d / e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "*") and (h == "*"):
            z = (b * d * e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "+") and (h == "-") :
            z = (b + d + e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "-") and (h == "+"):
            z = (b - d - e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "/") and (h == "+"):
            z = (b / d / e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "*") and (h == "+"):
            z = (b * d * e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "-") and (h == "-") :
            z = (b + d - e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "+") and (h == "+"):
            z = (b - d + e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "+") and (h == "+"):
            z = (b / d + e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "+") and (h == "+"):
            z = (b * d + e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "-") and (h == "+") :
            z = (b + d - e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "+") and (h == "-"):
            z = (b - d + e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "+") and (h == "/"):
            z = (b / d + e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "+") and (h == "*"):
            z = (b * d + e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "+") and (h == "/") :
            z = (b + d + e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "-") and (h == "/"):
            z = (b - d - e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "/") and (h == "-"):
            z = (b / d / e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "*") and (h == "-"):
            z = (b * d * e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "/") and (h == "/") :
            z = (b + d / e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "/") and (h == "/"):
            z = (b - d / e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "-") and (h == "-"):
            z = (b / d - e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "-") and (h == "-"):
            z = (b * d - e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "/") and (h == "+") :
            z = (b + d / e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "/") and (h == "-"):
            z = (b - d / e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "-") and (h == "/"):
            z = (b / d - e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "-") and (h == "*"):
            z = (b * d - e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "+") and (h == "*") :
            z = (b + d + e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "-") and (h == "*"):
            z = (b - d - e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "/") and (h == "*"):
            z = (b / d / e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "*") and (h == "/"):
            z = (b * d * e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "*") and (h == "*") :
            z = (b + d * e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "*") and (h == "*"):
            z = (b - d * e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "*") and (h == "*"):
            z = (b / d * e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "/") and (h == "/"):
            z = (b * d / e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "*") and (h == "+") :
            z = (b + d * e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "*") and (h == "-"):
            z = (b - d * e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "*") and (h == "/"):
            z = (b / d * e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "/") and (h == "*"):
            z = (b * d / e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "*") and (h == "+") :
            z = (b + d * e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "*") and (h == "-"):
            z = (b - d * e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "*") and (h == "/"):
            z = (b / d * e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "/") and (h == "*"):
            z = (b * d / e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "-") and (h == "/") :
            z = (b + d - e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "+") and (h == "/"):
            z = (b - d + e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "+") and (h == "-"):
            z = (b / d + e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "+") and (h == "-"):
            z = (b * d + e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "/") and (h == "*") :
            z = (b + d / e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "/") and (h == "*"):
            z = (b - d / e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "-") and (h == "*"):
            z = (b / d - e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "-") and (h == "/"):
            z = (b * d - e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "*") and (h == "-") :
            z = (b + d * e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "*") and (h == "+"):
            z = (b - d * e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "*") and (h == "+"):
            z = (b / d * e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "/") and (h == "+"):
            z = (b * d / e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "/") and (h == "-") :
            z = (b + d / e - g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "-") and (f == "/") and (h == "+"):
            z = (b - d / e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "/") and (f == "-") and (h == "+"):
            z = (b / d - e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "-") and (h == "+"):
            z = (b * d - e + g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "*") and (f == "+") and (h == "/"):
            z = (b * d + e / g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        elif (c == "+") and (f == "-") and (h == "*"):
            z = (b + d - e * g)
            if j == z:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Salah !")
                print("Hasil dari",b,c,d,f,e,h,g,"=",z)
        else :
            print("wadidaw")
        
    else :
        print("swidi")

#def cekHasil():
    
if a == 1:
    generate()
elif a == 2:
    generate()
elif a == 3:
    generate()
else:
    print("Menu yang anda pilih tidak ada !")
