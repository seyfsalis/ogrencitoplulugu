class Galeriler:
    def __init__(self, id, yol, kullanici_id, grup_id):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.yol = yol
        self.kullanici_id = kullanici_id
        self.grup_id = grup_id

    @staticmethod
    def CreateGaleri(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Galeriler(obj[0],obj[1],obj[2],obj[3]))
        else:
            for i in obj:
                list.append(Galeriler(i[0],i[1],i[2],i[3]))
        return list    