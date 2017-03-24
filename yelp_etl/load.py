import json
import psycopg2
try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
    # conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='LinuxlovePostgres1981'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS YELPBIZ(data JSON)")
    conn.commit()
except Exception as e:
    print ("I am unable to connect to the database")
    print(e)

with open('D:\DATA_DUMP\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_business.json') as bizfile:
    for line in bizfile:
        print(line)
        data = json.loads(line)
        # print(data)
        print( "'%s','%s','%s','%s',%s,%s,%s,%s" % ( data['name'],data['full_address'],data['city'],data['state'],data['latitude'],data['longitude'],data['stars'],data['review_count']
))

        insert = """INSERT INTO YELPTBL(
            name,
            full_address,
            city,
            state,
            latitude,
            longitude,
            stars,
            review_count
        ) VALUES('%s','%s','%s','%s',%s,%s,%s,%s)""" \
                 % \
                 (data['name'].replace("'","''"),data['full_address'].replace("'","''"),data['city'].replace("'","''"),data['state'].replace("'","''"),data['latitude'],data['longitude'],data['stars'],data['review_count']
                  )
        cur.execute(insert)
        conn.commit()
conn.commit()
conn.close()