import json
import sqlite3



conn = sqlite3.connect("D://yelpdb.db")
create_sql = """

CREATE TABLE yelp_checkin_info( 
    CHECKIN_TYPE TEXT,
    BUSINESS_ID TEXT, 
    FROM_TIME INT,
    TO_TIME INT,
    CHECKIN_NUM INT
);
"""

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS yelp_checkin_info;")
c.execute(create_sql)
conn.commit()


insert_sql = """
INSERT INTO YELP_CHECKIN_INFO VALUES(
    '{}',
    '{}',
    {},
    {},
    {}
);
"""

with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_checkin.json","r") as f:
    for line in f.readlines():
        d = json.loads(line)
#         print(d)
        
        checkin_type = d['type']
        business_id = d['business_id']
        
        for k,v in d['checkin_info'].items():
            tofrom_time = [int(i) for i in k.split("-")]
            sql = insert_sql.format(checkin_type,business_id,tofrom_time[0],tofrom_time[1],v)
#             print(sql)  
            c.execute(sql)
            
    conn.commit()
    conn.close()
        
    