"""
{'Take-out': True, 'Drive-Thru': False, 

            'Good For': {'dessert': False, 'latenight': False, 
             'lunch': False, 'dinner': False, 'brunch': False, 
             'breakfast': False}, 'Caters': False, 
             'Noise Level': 'average', 
             'Takes Reservations': False, 'Delivery': False, 
             
             'Ambience': {'romantic': False, 'intimate': False, 'classy': False, 
                 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 
                 'upscale': False, 'casual': False}, 
                 
              'Parking': {'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}, 
             
              'Has TV': False, 'Outdoor Seating': False, 
              'Attire': 'casual', 'Alcohol': 'none', 
              'Waiter Service': False, 'Accepts Credit Cards': True, 'Good for Kids': True, 'Good For Groups': True, 'Price Range': 1}
              
     
Take-out
Drive-Thru
Caters
Noise Level
Takes Reservations
Delivery
Has TV
Outdoor Seating
Attire
Alcohol
Waiter Service
Accepts Credit Cards
Good for Kids
Good For Groups
Price Range
"""

"""

Attributes

    take_out boolean,
drive_thru boolean,
good_for boolean,
caters boolean,
noise_level boolean,
takes_reservations boolean,
delivery boolean,
ambience boolean,
parking boolean,
has_tv boolean,
outdoor_seating boolean,
attire boolean,
alcohol boolean,
waiter_service boolean,
accepts_credit_cards boolean,
good_for_kids boolean,
good_for_groups boolean,
price_range boolean,


Good For

    good_for_dessert boolean,
good_for_latenight boolean,
good_for_lunch boolean,
good_for_dinner boolean,
good_for_brunch boolean,
good_for_breakfast boolean,


Ambience

ambience_romantic boolean,
ambience_intimate boolean,
ambience_classy boolean,
ambience_hipster boolean,
ambience_divey boolean,
ambience_touristy boolean,
ambience_trendy boolean,
ambience_upscale boolean,
ambience_casual boolean,


Parking
    
   parking_garage boolean,
parking_street boolean,
parking_validated boolean,
parking_lot boolean,
parking_valet boolean,

"""
import json
# 
# with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json","r") as f:
#     d = json.loads(f.readline())    
#     for k,v in d['attributes'].items():
#         print('"' + k + '",')
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

# with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_business.json","r") as f:
#     
#         d = json.loads(f.readline())
#         sql_val= []   
#         business_id = d["business_id"]    
#         
#         sql_val.append(business_id)
#         for i in simple_att:
#             sql_val.append(d["attributes"][i])
#         print(sql_val)
# 
# 
# print("""{0},{1}""".format(*[1,2]))



with open("D:\\DATA_DUMP\\yelp_dataset_challenge_academic_dataset\\yelp_academic_dataset_user.json","r") as f:
    for line in f:
        d = json.loads(line)
        key_list = ['profile', 'cute', 'funny', 'plain', 'writer', 'note', 'photos', 'hot', 'cool', 'more']
        
        l = [d['compliments'][key] if key in d['compliments'] else 0 for key in key_list ]
        print(len(l))
        