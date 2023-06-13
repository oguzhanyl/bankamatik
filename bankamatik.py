EduardoHesap = {
    'ad':'Eduardo Salamanca',
    'hesapNo': '123214124',
    'bakiye': 3000,
    'ekHesap': 2000
}
OguzhanHesap = {
    'ad':'Oğuzhan Yılmaz',
    'hesapNo':'213124124',
    'bakiye': 4000,
    'ekHesap': 3000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye']-=miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if(toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı ? (e/h) : ")
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("paranızı çekebilirsiniz")
                bakiyeSorgula(hesap)
            elif ekHesapKullanimi == 'h':
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL para bulunmakta, ek hesabınızda ise {hesap['ekHesap']} TL para bulunmaktadır.")
            else:
                print('Lütfen geçerli bir ifade girip tekrar deneyiniz. (e/h)')
        else:
            print('üzgünüz bakiye yetersiz.')


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL dir.")

paraCek(OguzhanHesap, 5000)

print('**************************')

paraCek(OguzhanHesap, 3000)