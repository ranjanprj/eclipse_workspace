"""
business_id - 5UmKMjUEUNdYWqANhGckJw
full_address - 4734 Lebanon Church Rd
Dravosburg, PA 15034
hours - {'Friday': {'close': '21:00', 'open': '11:00'}, 'Tuesday': {'close': '21:00', 'open': '11:00'}, 'Thursday': {'close': '21:00', 'open': '11:00'}, 'Wednesday': {'close': '21:00', 'open': '11:00'}, 'Monday': {'close': '21:00', 'open': '11:00'}}
open - True
categories - ['Fast Food', 'Restaurants']
city - Dravosburg
review_count - 7
name - Mr Hoagie

longitude - -79.9007057
state - PA
stars - 3.5
latitude - 40.3543266
attributes - {'Take-out': True, 'Drive-Thru': False, 'Good For': {'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}, 'Caters': False, 'Noise Level': 'average', 'Takes Reservations': False, 'Delivery': False, 'Ambience': {'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': False}, 'Parking': {'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}, 'Has TV': False, 'Outdoor Seating': False, 'Attire': 'casual', 'Alcohol': 'none', 'Waiter Service': False, 'Accepts Credit Cards': True, 'Good for Kids': True, 'Good For Groups': True, 'Price Range': 1}
type - business

business_id
full_address
open
city
review_count
name
longitude
state
stars
latitude
type


hours
categories
attributes
neighborhoods

"""






import json
import sqlite3



def load_business_data(conn):
    drop_sql = """
    drop table if exists yelp_business;
    """

    create_sql = """
    CREATE TABLE yelp_business(
    business_id text,
    full_address text,
    open bool,
    city text,
    review_count int,
    name text,
    longitude float,
    state text,
    stars int,
    latitude float,
    type text
    );
    
    """
    
    insert_sql = """
    INSERT INTO yelp_business values(
    '{}',
    '{}',
    {},
    '{}',
    {},
    '{}',
    {},
    '{}',
    {},
    {},
    '{}'
    );
    """
    c = conn.cursor()
    c.execute(drop_sql)
    conn.commit()
    c.execute(create_sql)
    conn.commit()
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json","r") as f:
    #     pass
        for line in f.readlines():
            d = json.loads(line)
    #         print(d["open"])
            is_open =  1 if  str(d["open"]) is "True"  else 0
    #         print(is_open)
            sql = insert_sql.format(
                d["business_id"],
                d["full_address"].replace("'","''"),
                is_open,
                d["city"].replace("'","''"),
                d["review_count"],
                d["name"].replace("'","''"),
                d["longitude"],
                d["state"].replace("'","''"),
                d["stars"],
                d["latitude"],
                d["type"]
            )
    #         print(sql)
            c.execute(sql)    
    
    ################################################################################################################################
    ################################################################################################################################
    ################################################################################################################################
    # INSERT HOURS
    drop_sql = """
    drop table if exists yelp_business_hours;
    """
    
    create_sql = """
    CREATE TABLE yelp_business_hours(
    business_id text,
    day_of_week text,
    open datetime,
    close datetime
    );
    
    """
    
    insert_sql = """
    INSERT INTO yelp_business_hours values(
    '{}',
    '{}',
    '{}',
    '{}'
    );
    """
    
    c = conn.cursor()
    c.execute(drop_sql)
    conn.commit()
    c.execute(create_sql)
    conn.commit()
              
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json","r") as f:
    #     pass
        for line in f.readlines():
            d = json.loads(line)   
            business_id = d["business_id"]
            for k,v in d["hours"].items():            
                sql = insert_sql.format(business_id,k,v['open'],v['close'])
                c.execute(sql)            
     
    
    ################################################################################################################################
    ################################################################################################################################
    ################################################################################################################################
    # INSERT categories
    drop_sql = """
    drop table if exists yelp_business_categories;
    """
    
    create_sql = """
    CREATE TABLE yelp_business_categories(
    business_id text,
    category text
    );
    
    """
    
    insert_sql = """
    INSERT INTO yelp_business_categories values(
    '{}',
    '{}'
    );
    """
    
    c = conn.cursor()
    c.execute(drop_sql)
    conn.commit()
    c.execute(create_sql)
    conn.commit()
              
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json","r") as f:
    #     pass
        for line in f.readlines():
          
            d = json.loads(line)   
            business_id = d["business_id"]       
                            
            for i in d["categories"]:
                
                sql = insert_sql.format(business_id,i.replace("'","''"))
                c.execute(sql)
            
         
    
    ################################################################################################################################
    ################################################################################################################################
    ################################################################################################################################
    # INSERT neighborhoods
    drop_sql = """
    drop table if exists yelp_business_neighborhoods;
    """
    
    create_sql = """
    CREATE TABLE yelp_business_neighborhoods(
    business_id text,
    neighborhoods text
    );
    
    """
    
    insert_sql = """
    INSERT INTO yelp_business_neighborhoods values(
    '{}',
    '{}'
    );
    """
    
    c = conn.cursor()
    c.execute(drop_sql)
    conn.commit()
    c.execute(create_sql)
    conn.commit()
              
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json","r") as f:
    #     pass
        for line in f.readlines():
      
            d = json.loads(line)   
            business_id = d["business_id"]       
                            
            for i in d["neighborhoods"]:
                sql = insert_sql.format(business_id,i.replace("'","''"))
                c.execute(sql)
            
         
         
    ################################################################################################################################
    ################################################################################################################################
    ################################################################################################################################
    # INSERT Attributes
    """
    attributes - {'Take-out': True, 'Drive-Thru': False, 'Good For': {'dessert': False, 'latenight': False, 'lunch': False,
              'dinner': False, 'brunch': False, 'breakfast': False}, 'Caters': False, 'Noise Level': 'average', 
                  'Takes Reservations': False, 'Delivery': False, 
                  'Ambience': {'romantic': False, 'intimate': False, 'classy': False, 
                               'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 
                               'upscale': False, 'casual': False}, 
                  'Parking': {'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}, 
                  'Has TV': False, 'Outdoor Seating': False, 'Attire': 'casual', 'Alcohol': 'none', 'Waiter Service': False,
                  'Accepts Credit Cards': True, 'Good for Kids': True, 'Good For Groups': True, 'Price Range': 1}
    """
    drop_sql = """
    drop table if exists yelp_business_attributes;
    """
    
    create_sql = """
    CREATE TABLE yelp_business_attributes(
    
    business_id text,
    take_out bool,
    drive_thru bool,
    caters bool,
    
    noise_level text,
    takes_reservations bool,
    delivery bool,
    has_tv bool,
    
    outdoor_seating bool,
    attire text,
    alcohol text,
    waiter_service bool,
    
    accepts_credit_cards bool,
    good_for_kids bool,
    good_for_groups bool,
    price_range int,
    
    
    
    
    good_for_dessert bool,
    good_for_latenight bool,
    good_for_lunch bool,
    good_for_dinner bool,
    good_for_brunch bool,
    good_for_breakfast bool,
    
    
    
    ambience_romantic bool,
    ambience_intimate bool,
    ambience_classy bool,
    ambience_hipster bool,
    ambience_divey bool,
    ambience_touristy bool,
    ambience_trendy bool,
    ambience_upscale bool,
    ambience_casual bool,
    
    
    
        
    parking_garage bool,
    parking_street bool,
    parking_validated bool,
    parking_lot bool,
    parking_valet bool
    
    );
    
    """
    
    insert_sql = """
    INSERT INTO yelp_business_attributes values(
    '{}',
    {},
    {},
    {},
    
    '{}',
    {},
    {},
    {},
    
    {},
    '{}',
    '{}',
    {},
    
    {},
    {},
    {},
    {},
    
    
    
    
    {},
    {},
    {},
    {},
    {},
    {},
    
    
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    
    {},
    {},
    {},
    {},
    {}
    
    );
    """
    
    c = conn.cursor()
    c.execute(drop_sql)
    conn.commit()
    c.execute(create_sql)
    conn.commit()
        
    simple_att = [
       
    "Take-out",
    "Drive-Thru",
    "Caters",
    
    "Noise Level",
    "Takes Reservations",
    "Delivery",
    "Has TV",
    
    "Outdoor Seating",
    "Attire",
    "Alcohol",
    "Waiter Service",
    
    "Accepts Credit Cards",
    "Good for Kids",
    "Good For Groups",
    "Price Range"
    ]     
    
    with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json","r") as f:
        for line in f.readlines():
            d = json.loads(line)
          
            sql_val= []   
            key_val_not_included = []
            business_id = d["business_id"]       
            sql_val.append(business_id)
            try: 
                for i in simple_att:
                    if i in d["attributes"]:
                       # v = "NULL" if typeof(d["attributes"][i]) is not  and len(d["attributes"][i]) is 0 else d["attributes"][i] 
                        v = d["attributes"][i]
                        if isinstance(v, str): 
                            v.replace("'","''")
                        sql_val.append(v)
                    else:
                        sql_val.append("NULL")
                if len(sql_val) < 16:
                    print("LESS THEN 16")     
                if  d["attributes"] is not None and "Good For" in  d["attributes"]:                
                    for k,v in d["attributes"]["Good For"].items():      
                        sql_val.append(v)
                else:
                        for i in range(0,6):
                            sql_val.append("NULL")
                
                if len(sql_val) < 22:
                    print("LESS THEN 22")
                    for i in range(22-len(sql_val)):
                        sql_val.append("NULL")
                                     
                if  d["attributes"] is not None and  "Ambience" in d["attributes"]:
                    for k,v in d["attributes"]["Ambience"].items():                    
                        sql_val.append(v)
                else:
                        for i in range(0,9):
                            sql_val.append("NULL")
                if len(sql_val) < 31:
                    print("LESS THEN 31")
                    for i in range(31-len(sql_val)):
                        sql_val.append("NULL")
                if  d["attributes"] is not None and  "Parking" in d["attributes"]:
                    for k,v in d["attributes"]["Parking"].items():
                        sql_val.append(v)
                 
                else:
                    for i in range(0,5):
                        sql_val.append("NULL")
                if len(sql_val) < 36:
                    print("LESS THEN 36")
                    for i in range(36-len(sql_val)):
                        sql_val.append("NULL")
            except KeyError as keyerr:
                sql_val.append("KEY")
                print(keyerr)  
            try:            
                new_sql_val = []
                for i in sql_val:
                   
                        
                    if isinstance(i, bool) and str(i) is "True" :
                        new_sql_val.append(1)
                    elif isinstance(i, bool) and str(i) is "False":
                        new_sql_val.append(0)
                    else:
                        new_sql_val.append(i)
    #             print(new_sql_val)
    #             print(len(sql_val))        
                a  = insert_sql.format(*new_sql_val)
                c.execute(a)
    #             print(a) 
            except Exception as ex:
                print(ex)
            
    ###################################################################################################
    
    conn.commit()
    conn.close()
        


if __name__ == "__main__":
    conn = sqlite3.connect("D://yelpdb.db")
    load_business_data(conn)