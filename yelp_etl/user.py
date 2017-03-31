"""
{'yelping_since': '2015-12', 
    'votes': {'funny': 0, 'useful': 0, 'cool': 0}, 
    'review_count': 1, 
    'name': 'Tammie', 
    'user_id': 'pyheQjz-d1K37grnX7pVjw', 
     
    'fans': 0, 
    'average_stars': 5.0, 
    'type': 'user', 
    'friends': [],
    'compliments': {}, 
    'elite': []}


{'yelping_since': '2014-04', 
    'review_count': 6, '
    name': 'Joshua', 
    'user_id': '_ga7D44jMNKZd6935odm8w', 
    'fans': 0, 
    'average_stars': 4.5, 
    'type': 'user', 
    
    'compliments': {'cool': 1}, 
    'elite': []
    'friends': ['OvS94I6_4AB_tOhI_w0D3w', 'jWhJAAQH9OXfaxUhup9OUw'], 
    'votes': {'funny': 2, 'useful': 4, 'cool': 3}, 
    
    }

"""

import json
import sqlite3

def load_data(conn):
    
    create_sql = """
    create table yelp_user(
    user_yelping_since date, 
    user_review_count int, 
    user_name text, 
    user_id text,
    user_fans int, 
    user_average_stars float, 
    user_type text
    );
    """
    
    drop_sql = """
    drop table if exists yelp_user;
    """
    
    insert_sql = """
        insert into yelp_user values('{}',{},'{}','{}',{},{},'{}');
    """
    
    
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS yelp_user;")
    c.execute(create_sql)
    conn.commit()
    key_len = 0
    key = []
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_user.json","r") as f,open("D://yelp.sql","a") as sql_file:
        for line in f:
            
            d = json.loads(line)
    #         print(d['compliments'])
            if len(d['compliments'].keys()) > key_len:
                key_len = len(d['compliments'].keys())
                key.append(d['compliments'])
            
            sql = insert_sql.format(d['yelping_since']+"-01",d['review_count'],d['name'].replace("'","''"),d['user_id'],d['fans'],d['average_stars'],d['type'])
            c.execute(sql)
            
    conn.commit()
    print(key_len)
    print(key)
    
    ##################
    ## FRIENDS
    ##############
    create_sql = """
    create table yelp_user_friends(
    user_id text,
    friend_id text
    );
    """
    
    drop_sql = """
    drop table if exists yelp_user_friends;
    """
    
    insert_sql = """
        insert into yelp_user_friends values('{}','{}');
    """
    
    
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS yelp_user_friends;")
    c.execute(create_sql)
    conn.commit()
    
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_user.json","r") as f,open("D://yelp.sql","a") as sql_file:
        for line in f:
            d = json.loads(line)
            for friend in d['friends']:            
                sql = insert_sql.format(d['user_id'],friend)
                c.execute(sql)
            
    conn.commit()
    
    
    
    ##################
    ## ELITES
    ##############
    create_sql = """
    create table yelp_user_elite(
    user_id text,
    elite int
    );
    """
    
    drop_sql = """
    drop table if exists yelp_user_elite;
    """
    
    insert_sql = """
        insert into yelp_user_elite values('{}',{});
    """
    
    
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS yelp_user_elite;")
    c.execute(create_sql)
    conn.commit()
    
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_user.json","r") as f,open("D://yelp.sql","a") as sql_file:
        for line in f:
            d = json.loads(line)
            for elite in d['elite']:            
                sql = insert_sql.format(d['user_id'],elite)
            c.execute(sql)
            
    conn.commit()
    
    print("ELITE INSERTED")
    
    ####################################################
    # compliments
    # {'profile': 117, 'cute': 204, 'funny': 594, 'plain': 970, 'writer': 346, 'list': 38, 'note': 611, 'photos': 361, 'hot': 1111, 'cool': 1675, 'more': 137}]
    
    ##################################################
    
    create_sql = """
    create table yelp_user_compliments(
    user_id text,
    profile int, 
    cute int, 
    funny int, 
    plain int ,
    writer int,
    list int, 
    note int,
    photos int,
    hot int,
    cool int,
    more int
    );
    """
    
    drop_sql = """
    drop table if exists yelp_user_compliments;
    """
    
    insert_sql = """
        insert into yelp_user_compliments values('{}',{},{},{},{},{},{},{},{},{},{},{});
    """
    
    
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS yelp_user_compliments;")
    c.execute(create_sql)
    conn.commit()
    
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_user.json","r") as f,open("D://yelp.sql","a") as sql_file:
        for line in f:
            d = json.loads(line)
            key_list = ['profile', 'cute', 'funny', 'plain', 'writer','list', 'note', 'photos', 'hot', 'cool', 'more']
            l = [d['compliments'][key] if key in d['compliments'] else 0 for key in key_list ]
            sql = insert_sql.format(d['user_id'],*l)
            c.execute(sql)
            
    conn.commit()
    
    ##############################
    #   VOTES
    ############################
    create_sql = """
    create table yelp_user_votes(
    user_id text,
    review_id text,
    funny int,
    useful int,
    cool int
    );
    """
    
    drop_sql = """
    drop table if exists yelp_user_votes;
    """
    
    votes_insert_sql = """
        insert into yelp_user_votes values('{}','{}',{},{},{});
    """
    
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS yelp_user_votes;")
    c.execute(create_sql)
    conn.commit()
    
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_review.json","r") as f,open("D://yelp.sql","a") as sql_file:
        for line in f:
            d = json.loads(line)   
            sql = votes_insert_sql.format(d['user_id'],d['review_id'],d['votes']['funny'],d['votes']['useful'],d['votes']['cool'])
            c.execute(sql)
    
           
    conn.commit()
    

    conn.close()

if __name__ == "__main__":
    conn = sqlite3.connect("D://yelpdb.db")
    load_data(conn)