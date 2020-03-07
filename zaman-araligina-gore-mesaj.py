saat = int(input("Lütfen saat giriniz:"))
if saat < 0 or saat > 24 :
    print("Hatalı bir saat girdiniz.")
else:
    if  saat > 6 and saat <= 10 :
        print("Hayırlı sabahlar.")
    elif  saat > 10 and saat <= 17 :
        print("Hayırlı günler.")
    elif  saat > 17 and saat <= 21 :
        print("Hayırlı akşamlar.")
    else:
        print("Hayırlı geceler.")
