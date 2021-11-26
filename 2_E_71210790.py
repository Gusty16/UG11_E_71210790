a = input("Masukkan kata : ")
ak = len(a)

def hurufTengah():
    if (ak == 7):
        print("Huruf tengah pada kata",a,"adalah",a[2:5])
    elif (ak == 3):
        print("Huruf tengah pada kata",a,"adalah",a[1])
    elif (ak == 6):
        print("Huruf tengah pada kata",a,"adalah",a[2:4])
    elif (ak == 8):
        print("Huruf tengah pada kata",a,"adalah",a[2:6])
    elif (ak == 9):
        print("Huruf tengah pada kata",a,"adalah",a[3:6])
    elif (ak == 5):
        print("Huruf tengah pada kata",a,"adalah",a[2:5])
    else:
        print(a)

if ak != 0 :
    hurufTengah()
else:
    ("anda belum masukan kata")
