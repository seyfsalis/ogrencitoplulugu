class Duyurular:
    def __init__(self, id, baslik, icerik, tarih, kullanici_id, grup_id):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.baslik = baslik
        self.icerik = icerik
        self.tarih = tarih
        self.kullanici_id = kullanici_id
        self.grup_id = grup_id


    
    @staticmethod
    def CreateDuyuru(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Duyurular(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5]))
        else:
            for i in obj:
                list.append(Duyurular(i[0],i[1],i[2],i[3],i[4],obj[5]))
        return list