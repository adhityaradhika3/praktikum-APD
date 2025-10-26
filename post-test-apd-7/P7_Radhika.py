def perkenalan():
    print('Halo, aku Dhika')

perkenalan()

def salam():
    print ('Halo, Dhika')
def kali():
    x = 5*5
    print(x)

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print ('luas persegi panjang adalah ', luas)
    luas_persegi_panjang(4, 5)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
    
print ("Luas persegi :", luas_persegi(8))