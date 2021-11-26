print("Menu Program Yang Tersedia")
print("1. pangkatkan angka")
print("2. akarkan bilangan")
a = int(input("Masukkan pilihan yang diinginkan : "))
print("Masukkan angka yang ingin di Pangkatkan")
b = float(input("Angka : "))
print("ingin memodifikasi pangkat ?(yes/no)")
c = input(":")

def pangkatAngka():
    if (a == 1) and (c == "yes"):
        d = float(input("Masukkan nilai pangkat : "))
        print("Hasil dari",b,"^",d,"=",b ** d)
    elif (a == 1) and (c == "no"):
        print("Hasil dari",b,"^2 =",b ** 2)
    else :
        print("Menu program tidak tersedia")
def akarBilangan():
    if (a == 2) and (c == "yes"):
        e = float(input("Masukkan nilai akar : "))
        print("Hasil akar pangkat",e,"dari",b,"=",b ** (1 / e))
    elif (a == 2) and (c == "no"):
        f = b ** (1 / 2)
        print("Hasil akar pangkat 2 dari",b,"=",round(f, 2))
    else :
        print("Menu program tidak tersedia")
        
if a == 1 :
    pangkatAngka()
elif a == 2 :
    akarBilangan()
else:
    print("Mennu program tidak tersedia")
