t = "Program Manipulasi String"
x = t.center(40,"=")
print(x)
print("Pilihan Menu :")
print("1. Hitung kata")
print("2. cek kata")
print("3. ubah kata")
a = input("Pilihan anda : ")

def hitungKata():
    b = input("Masukkan sebuah kalimat/kata : ")
    y = (b.lower())
    c = input("Masukkan kata yang ingin dihitung : ")
    v = y.count(c)
    print("Terdapat sebanyak",v,"kata",c,"didalam string")
    
def cekKata():
    b = input("Masukkan sebuah kalimat/kata : ")
    y = (b.lower())
    c = input("Masukkan kata yang ingin di cek : ")
    p = c.upper()
    v = y.replace(c,p)
    print("Kata",c,"terdapat di dalam string")
    print("String diubah menjadi : ")
    print(v)
    
def ubahKata():
    b = input("Masukkan sebuah kalimat/kata : ")
    y = (b.lower())
    c = input("Masukkan kata yang ingin di ubah : ")
    d = input("Masukkan kata pengganti : ")
    print("Anda akan mengubah kata",c,"menjadi",d,"sebanyak 1x")
    u = input("Apakah anda ingin mengubah jumlah total pengganti kata ? (yes/no): ")
    if u == "yes" :
        z = int(input("Masukkan jumlah total penggantian : "))
        print("String berhasil diubah menjadi : ")
        v = y.replace(c,d,z)
        print(v)
    elif u == "no":
        z = 1
        print("String berhasil diubah menjadi : ")
        v = y.replace(c,d,z)
        print(v)
        
if a == "1":
    hitungKata()
elif a == "2":
    cekKata()
elif a == "3":
    ubahKata()
else:
    print("Menu yang anda pilih tidak ada !")
     
