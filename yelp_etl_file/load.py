import json
import psycopg2

import business
import checkin
import tip
import user
import review
import asyncpg
import asyncio

from multiprocessing import Process

def load_checkin():
    print("Loading CHECKIN")
    #conn = asyncpg.connect(host='localhost',port='5432',user='postgres',password='postgres',database='postgres')
    checkin.load_data(get_conn())
    print("done checkin")
   
def load_user():
    print('user')
    user.load_data(get_conn())
    print("done user")
def load_business():
    print('business')
    business.load_data(get_conn())
    print("done business")
def load_review():
    print('review')
    review.load_data(get_conn())
    print("done review")
def load_tip():
    print('tip')
    tip.load_data(get_conn())
    print("done tip")
def get_conn():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
        return conn

    except Exception as e:
        print ("I am unable to connect to the database")
        print(e)

if __name__ == '__main__':
    
    conn = get_conn()
    conn.cursor().execute("drop view if exists yelp_view")
    conn.commit()
    conn.close()
    
#     p1 = Process(target=load_checkin)
#     p2 = Process(target=load_user)
#     p3 = Process(target=load_business)
#     p4 = Process(target=load_review)
#     p5 = Process(target=load_tip)
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p5.start()
    load_checkin()
    load_business()
    load_tip()
    load_review()
    load_user()
   