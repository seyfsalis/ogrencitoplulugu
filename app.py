from dbmanager import DbManager
from Kullanicilar import Kullanicilar

class App:
    def __init__(self):
        self.db = DbManager()
    
    
    
    
    def ekleme(self):
        #ad, soyad, telefon, okul_no, tc, mail, sifre, yetki
        name = "test"
        surname = "Şalış"
        phone = "5061429571"
        school_number = "02185076051"
        tc = "12345678910"
        mail = "seyf.salis.99@gmail.com"
        password = "abc123"
        yetki = 3
        no = 6
        test = Kullanicilar(no, name, surname, phone, school_number, tc, mail, password, yetki)
        #self.db.addKullanici(test)
        gelen = self.db.getKullanicilar()
        self.db.editKullanici(test)


        for i in gelen:
            print(i.id, i.ad, i.soyad, i.telefon, i.tc, i.okul_no, i.mail, i.sifre, i.yetki)


        # for i in geldi:
        #     print(f'{i.ad}')

deneme = App()
deneme.ekleme()