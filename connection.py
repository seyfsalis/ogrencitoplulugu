import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="toplulukdb",
    user="postgres",
    password="123456")

print("bağlantı başarılı")
    