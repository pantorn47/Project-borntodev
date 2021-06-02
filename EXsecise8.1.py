

username = input("ID: ")
password = input("Password: ")

if username == "1" and password == "1":
    print("Login Sucsess")
    print("----------------------------------")
    print("------Welcome to THC Shop-------")
    print("----------------------------------")
    print("1.OG Kush         X 1g 300")
    print("2.Banana Kush     X 1g 320")
    print("3.Purple Kush     X 1g 300")
    print("4.Wild Thai       X 1g 220")
    print("5.GG4             X 1g 350")
    print("6.GSC             X 1g 330")


    OGKush = 300
    BananaKush = 320
    PurpleKush = 300
    WildThai = 220
    GG4 = 350
    GSC = 330

    resultGSC=0
    resultGG4=0
    resultOGKush=0
    resultWildThai=0
    resultBananaKush=0
    resultPurpleKush=0

    userSelected = int(input('สินค้าที่ต้องการ? (ใส่ตัวเลขด้านหน้าเมนู) : '))
    while userSelected != 0 :
        if userSelected == 1:
                amount = int(input("จำนวน G: "))
                print("OG Kush")
                print ("result  = ",OGKush*amount ,"THB.")
                resultOGKush = OGKush * amount
                userSelected= int(input("ต้องการสินค้าเพิ่มพิมพ์ตัวเลขหน้าชื่อสินค้า  (หากไม่ต้องการกด 0) : "))
        elif userSelected == 2:
                print("Banana Kush")
                amount = int(input("จำนวน G: "))
                print("result  = ", BananaKush * amount, "THB.")
                resultBananaKush = BananaKush * amount
                userSelected = int(input("ต้องการสินค้าเพิ่มพิมพ์ตัวเลขหน้าชื่อสินค้า (หากไม่ต้องการกด 0) : "))
        elif userSelected == 3:
                print("PurpleKush")
                amount = int(input("จำนวน G: "))
                print("result  = ", PurpleKush * amount, "THB.")
                resultPurpleKush = PurpleKush * amount
                userSelected = int(input("ต้องการสินค้าเพิ่มพิมพ์ตัวเลขหน้าชื่อสินค้า (หากไม่ต้องการกด 0) : "))
        elif userSelected == 4:
                print("WildThai")
                amount = int(input("จำนวน G: "))
                print("result  = ", WildThai * amount, "THB.")
                resultWildThai = WildThai * amount
                userSelected = int(input("ต้องการสินค้าเพิ่มพิมพ์ตัวเลขหน้าชื่อสินค้า (หากไม่ต้องการกด 0) : "))
        elif userSelected == 5:
                print("GG4")
                amount = int(input("จำนวน G: "))
                print("result  = ", GG4 * amount, "THB.")
                resultGG4 = GG4 * amount
                userSelected = int(input("ต้องการสินค้าเพิ่มพิมพ์ตัวเลขหน้าชื่อสินค้า (หากไม่ต้องการกด 0) : "))
        elif userSelected == 6:
                print("GSC")
                amount = int(input("จำนวน G: "))
                print("result  = ", GSC * amount, "THB.")
                resultGSC = GSC * amount
                userSelected = int(input("ต้องการสินค้าเพิ่มพิมพ์ตัวเลขหน้าชื่อสินค้า (หากไม่ต้องการกด 0) : "))
    else :
        print("------------------------")
        print("สินค้าทั้งหมดราคา", resultGSC+resultGG4+resultWildThai+resultPurpleKush+resultBananaKush+resultOGKush , "THB")
        print("------------------------")
        print('กดถัดไปเพื่อชำระสินค้า')
else:
    print("Try Again")
