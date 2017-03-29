import json
import psycopg2
import business

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
    # conn = psycopg2.connect("dbname='postgres' tip='postgres' host='localhost' password='LinuxlovePostgres1981'")
    business.load_business_data(conn)

    conn.commit()
except Exception as e:
    print ("I am unable to connect to the database")
    print(e)

