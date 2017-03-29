"""
{'votes': {'funny': 1, 'useful': 4, 'cool': 2}, 
'user_id': 'nEYPahVwXGD2Pjvgkm7QqQ', 
'review_id': 'fVPpqAGtfL46r0jn5B4Fpw',
 'stars': 5, 
 'date': '2011-01-21', 
 'text': "This is by far and away my favorite theater in Pittsburgh! I\n\nf you've ever been here you KNOW how beautiful it is! It's a historic landmark and was built in 1927 and restored in the 80's to it's original state. It holds around 2,200 seats and is the third largest stage in the country. As you can see, I'm a total nerd about this theater.\n\nSo let me give you some BIG insider tips about seating! Avoid at all costs the outer sides of the Left and Right Orchestra (the floor) in the front. You can actually get a cheap seat if you sit in the back of the Left and Right sides but only sit on the aisle. IF an aisle seat isn't available, go for First or Second Tier. I would rather see the show from far away than half see the show! \n\nThe touring Broadway, Pittsburgh CLO, Pittsburgh Opera and Pittsburgh Ballet Theatre perform here. So go support our local theater! Just remember it's right here in the burgh, it's still a fantastic production and it's cheaper than a trip to NYC!", 'type': 'review', 'business_id': 'XY3sN_2uusMSU9i1WINFeg'}
"""

import json
import sqlite3

conn = sqlite3.connect("D://yelpdb.db")

######################################
create_sql = """
create table yelp_review(
user_id text,
review_id text,
stars int,
date datetime,
review_text text
);
"""

drop_sql = """
drop table if exists yelp_review;
"""

insert_sql = """
    insert into yelp_review values('{}','{}',{},'{}','{}');
"""

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS yelp_review;")
c.execute(create_sql)
conn.commit()
###########################################
create_sql = """
create table yelp_review_votes(
user_id text,
review_id text,
funny int,
useful int,
cool int
);
"""

drop_sql = """
drop table if exists yelp_review_votes;
"""

votes_insert_sql = """
    insert into yelp_review_votes values('{}','{}',{},{},{});
"""

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS yelp_review_votes;")
c.execute(create_sql)
conn.commit()
##############



with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_review.json","r") as f:
    for line in f:
        d = json.loads(line)
        sql = insert_sql.format(d['user_id'],d['review_id'],d['stars'],d['date'],d['text'].replace("'","''"))
        c.execute(sql)
        
                
        sql = votes_insert_sql.format(d['user_id'],d['review_id'],d['votes']['funny'],d['votes']['useful'],d['votes']['cool'])
        c.execute(sql)

       
conn.commit()
conn.close()

