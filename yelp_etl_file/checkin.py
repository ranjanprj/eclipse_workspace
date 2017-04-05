import json
import sqlite3

import codecs
sql_file = codecs.open("D://yelp_data.sql", 'a', encoding='utf8')

def load_data(conn):
    create_sql = """
    
    CREATE TABLE yelp_checkin( 
        checkin_type TEXT,
        checkin_BUSINESS_ID TEXT, 
        checkin_from_time INT,
        checkin_to_time INT,
        checkin_num INT
    );
    """
    
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS yelp_checkin;")
    c.execute(create_sql)
    conn.commit()
    
    
    insert_sql = """
    INSERT INTO yelp_checkin VALUES(
        '{}',
        '{}',
        {},
        {},
        {}
    );
    """
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_checkin.json","r") as f:
        for line in f:
            d = json.loads(line)
    #         print(d)
            
            checkin_type = d['type']
            business_id = d['business_id']
            
            for k,v in d['checkin_info'].items():
                tofrom_time = [int(i) for i in k.split("-")]
                sql = insert_sql.format(checkin_type,business_id,tofrom_time[0],tofrom_time[1],v)
    #             print(sql)  
                sql_file.write(sql)                
                
    conn.commit()
    
    conn.close()
        
    
if __name__ == "__main__":
    conn = sqlite3.connect("D://yelpdb.db")
    load_data(conn)