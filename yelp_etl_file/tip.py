import json
import sqlite3
import codecs
sql_file = codecs.open("D://yelp_data.sql", 'a', encoding='utf8')

def load_data(conn):
    create_sql = """
    create table yelp_tip(
    tip_user_id text,
    tip_business_id text,
    tip_likes int,
    tip_date date,
    tip_type text
    );
    """
    
    drop_sql = """
    drop table if exists yelp_tip;
    """
    
    insert_sql = """
        insert into yelp_tip values('{}','{}',{},'{}','{}');
    """
    
    
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS yelp_tip;")
    c.execute(create_sql)
    conn.commit()
    
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_tip.json","r") as f,open("D://yelp.sql","a") as sql_file:
        for line in f:
            d = json.loads(line)
            
            sql = insert_sql.format(d['user_id'],d['business_id'],d['likes'],d['date'],d['type'])
            sql_file.write(sql)
            
            
    conn.commit()
    conn.close()
    


if __name__ == "__main__":
    conn = sqlite3.connect("D://yelpdb.db")
    load_data(conn)