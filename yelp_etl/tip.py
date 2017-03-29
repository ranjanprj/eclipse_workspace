import json
import sqlite3


create_sql = """
create table yelp_tip(
user_id text,
business_id text,
likes int,
date datetime,
type text
);
"""

drop_sql = """
drop table if exists yelp_tip;
"""

insert_sql = """
    insert into yelp_tip values('{}','{}',{},{},'{}');
"""
conn = sqlite3.connect("D://yelpdb.db")

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS yelp_tip;")
c.execute(create_sql)
conn.commit()


with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_tip.json","r") as f:
    for line in f.readlines():
        d = json.loads(line)
        
        sql = insert_sql.format(d['user_id'],d['business_id'],d['likes'],d['date'],d['type'])
        c.execute(sql)
        
conn.commit()
conn.close()

