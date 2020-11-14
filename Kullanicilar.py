class Kullanicilar:
    def __init__(self,id, ad, soyad, telefon, okul_no, tc, mail, sifre, yetki):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.okul_no = okul_no
        self.tc = tc 
        self.mail = mail
        self.sifre = sifre
        self.yetki = yetki


    @staticmethod
    def CreateKullanici(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Kullanicilar(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6],obj[7],obj[8]))
        else:
            for i in obj:
                list.append(Kullanicilar(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],obj[8]))
        return list