import psycopg2
from datetime import datetime 
from connection import connection
from Kullanicilar import Kullanicilar
from Duyurular import Duyurular
from Etkinlikler import Etkinlikler
from Forumlar import Forumlar
from Galeriler import Galeriler
from Gruplar import Gruplar

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def addKullanici(self, kullanici: Kullanicilar):
        sql = "INSERT INTO Kullanicilar(ad, soyad, telefon, okul_no, tc, mail, sifre, yetki) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        value = (kullanici.ad, kullanici.soyad, kullanici.telefon,kullanici.okul_no, kullanici.tc, kullanici.mail, kullanici.sifre, kullanici.yetki)
        self.cursor.execute(sql, value)
        
        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def editKullanici(self, kullanici: Kullanicilar):
        sql = "update Kullanicilar set ad=%s, soyad=%s, telefon=%s, okul_no=%s, tc=%s, mail=%s, sifre=%s, yetki=%s where id=%s"
        value = (kullanici.ad, kullanici.soyad, kullanici.telefon, kullanici.okul_no, kullanici.tc, kullanici.mail, kullanici.sifre, kullanici.yetki, kullanici.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def deleteKullanici(self, id):
        sql = "delete from kullanicilar where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def getKullanicilar(self):
        sql = "select * from kullanicilar"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            list = []
            for row in obj:
                list.append(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                print(list)
                # id = row[0]
                # ad = row[1]
                # soyad = row[2]
                # telefon = row[3]
                # okul_no = row[4]
                # tc = row[5]
                # mail = row[6]
                # sifre = row[7]
                # yetki = row[8]
                #print(f'id={id},ad={ad},soyad={soyad},telefon={telefon},okul_no={okul_no},tc={tc},mail={mail},sifre={sifre},yetki={yetki}')
        except Exception as err:
            print("hata: ", err)
            
    def addDuyuru(self, duyuru, Duyurular):
        sql = "INSERT INTO Duyurular(baslik, icerik, tarih, kullanici_id, grup_id) VALUES (%s, %s, %s, %s, %s)"
        value = (duyuru.baslik, duyuru.icerik, duyuru.tarih, duyuru.kullanici_id, duyuru.grup_id)
        self.cursor.execute(sql, value)
        
        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def editDuyuru(self, duyuru, Duyurular):
        sql = "update duyurular set baslik=%s, icerik=%s, tarih=%s, kullanici_id=%s, grup_id=%s where id=%s"
        value = (duyuru.baslik, duyuru.icerik, duyuru.tarih, duyuru.kullanici_id, duyuru.grup_id, duyuru.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def deleteDuyuru(self, id):
        sql = "delete from duyurular where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def getDuyuru(self):
        sql = "select * from duyurular"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Duyurular.CreateDuyuru(obj)
        except Exception as err:
            print("hata: ", err)

    def addEtkinlik(self, etkinlik, Etkinlikler):
        sql = "INSERT INTO Etkinlikler(baslik, icerik, mekan, kullanici_id, grup_id) VALUES (%s, %s, %s, %s, %s)"
        value = (etkinlik.baslik, etkinlik.icerik, etkinlik.mekan, etkinlik.kullanici_id, etkinlik.grup_id)
        self.cursor.execute(sql, value)
        
        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def editEtkinlik(self, etkinlik, Etkinlikler):
        sql = "update duyurular set baslik=%s, icerik=%s, mekan=%s, kullanici_id=%s, grup_id=%s where id=%s"
        value = (etkinlik.baslik, etkinlik.icerik, etkinlik.mekan, etkinlik.kullanici_id, etkinlik.grup_id, etkinlik.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def deleteEtkinlik(self, id):
        sql = "delete from etkinlikler where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def getEtkinlik(self):
        sql = "select * from etkinlikler"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Etkinlikler.CreateEtkinlik(obj)
        except Exception as err:
            print("hata: ", err)

    def addForum(self, forum, Forumlar):
        sql = "INSERT INTO forumlar(baslik, icerik, kullanici_id, grup_id) VALUES (%s, %s, %s, %s)"
        value = (forum.baslik, forum.icerik, forum.kullanici_id, forum.grup_id)
        self.cursor.execute(sql, value)
        
        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def editForum(self, forum, Forumlar):
        sql = "update forumlar set baslik=%s, icerik=%s, kullanici_id=%s, grup_id=%s where id=%s"
        value = (forum.baslik, forum.icerik, forum.kullanici_id, forum.grup_id, forum.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def deleteForum(self, id):
        sql = "delete from forumlar where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def getForum(self):
        sql = "select * from forumlar"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Forumlar.CreateForum(obj)
        except Exception as err:
            print("hata: ", err)

    def addGaleri(self, galeri, Geleriler):
        sql = "INSERT INTO galeriler(yol, kullanici_id, grup_id) VALUES (%s, %s, %s)"
        value = (galeri.yol, galeri.kullanici_id, galeri.grup_id)
        self.cursor.execute(sql, value)
        
        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def deleteGaleri(self, id):
        sql = "delete from galeriler where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def getGaleri(self):
        sql = "select * from galeriler"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Galeriler.CreateGaleri(obj)
        except Exception as err:
            print("hata: ", err)

    def __del__(self):
        self.connection.close()

    def addGrup(self, grup, Gruplar):
        sql = "INSERT INTO gruplar(ad) VALUES (%s)"
        value = (grup.ad)
        self.cursor.execute(sql, value)
        
        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def editGrup(self, grup, Gruplar):
        sql = "update gruplar set ad=%s where id=%s"
        value = (grup.ad, grup.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def deleteGrup(self, id):
        sql = "delete from gruplar where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
        except Exception as err:
            print("hata: ", err)

    def getGrup(self):
        sql = "select * from gruplar"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Gruplar.CreateGrup(obj)
        except Exception as err:
            print("hata: ", err)