class Forumlar:
    def __init__(self, id, baslik, icerik, kullanici_id, grup_id):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.baslik = baslik
        self.icerik = icerik
        self.kullanici_id = kullanici_id
        self.grup_id = grup_id


    @staticmethod
    def CreateForum(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Forumlar(obj[0],obj[1],obj[2],obj[3],obj[4]))
        else:
            for i in obj:
                list.append(Forumlar(i[0],i[1],i[2],i[3],i[4]))
        return list    