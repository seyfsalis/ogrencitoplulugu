from dbmanager import DbManager
from Kullanicilar import Kullanicilar

class App:
    def __init__(self):
        self.db = DbManager()
    
    
    
    
    def ekleme(self):
        
        self.db.getKullanicilar()

        
        # for i in geldi:
        #     print(f'{i.ad}')

deneme = App()
deneme.ekleme()