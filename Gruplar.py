class Gruplar:
    def __init__(self, id, ad):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.ad = ad

    @staticmethod
    def CreateGrup(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Gruplar(obj[0],obj[1]))
        else:
            for i in obj:
                list.append(Gruplar(i[0],i[1]))
        return list    