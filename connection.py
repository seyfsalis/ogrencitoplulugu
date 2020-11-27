import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="toplulukdb",
        user="postgres",
        password="123456")
except Exception as err:
    print(err)


