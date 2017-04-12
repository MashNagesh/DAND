
# coding: utf-8

# In[7]:

import csv, sqlite3

def number_of_nodes():
    result = cur.execute('SELECT COUNT(*) FROM NODES')
    return result.fetchone()[0]

def number_of_ways():
    result = cur.execute('SELECT COUNT(*) FROM WAYS')
    return result.fetchone()[0]

def number_of_unique_users():
    result = cur.execute('SELECT COUNT(DISTINCT(United.UID))             FROM (SELECT UID FROM NODES UNION ALL SELECT UID FROM WAYS)United')
    return result.fetchone()[0]
    
def top_contributing_users():
    users = []
    for row in cur.execute('SELECT United.User,count(*)as num             FROM (SELECT UID,User FROM NODES UNION ALL SELECT UID,User FROM WAYS)United             GROUP BY United.UID             ORDER BY NUM DESC             LIMIT 10'):
        users.append(row)
    return users

def Avg_contribution():
    result = cur.execute('SELECT avg(num) FROM            (SELECT United.User as user ,count(*)AS num FROM            (SELECT UID,User FROM NODES UNION ALL SELECT UID,User FROM WAYS)United             GROUP BY United.UID)grouped')
    return result.fetchone()[0]

def common_ammenities():
    amenities = []
    for row in cur.execute('SELECT value,count(*) as num                FROM Node_tags                WHERE key= "amenity"                GROUP BY value                ORDER by num desc                LIMIT 10'):
                    amenities.append(row)
    return amenities

def popular_bank():
    banks =[]
    for row in cur.execute('SELECT value,count(*)as num FROM Node_tags                         WHERE id in                         (SELECT id FROM Node_tags                         WHERE key="amenity" and (value ="atm" or value ="branch"))and key ="operator"                        GROUP BY value                        ORDER BY num DESC                        LIMIT 10'):
                            banks.append(row)
    return banks

def popular_cuisines():
    cuisine = []
    for row in cur.execute('SELECT value,count(*)as num FROM Node_tags                            WHERE id IN                            (SELECT id FROM Node_tags WHERE key="amenity" and value ="restaurant")                           and key ="cuisine"                            GROUP BY value                            ORDER BY num DESC                            LIMIT 5'):
                                cuisine.append(row)
    return cuisine

if __name__ == '__main__':
    
    con = sqlite3.connect("Vidyaranyapura.db")
    cur = con.cursor()

    print "Number of nodes: " , number_of_nodes()
    print "Number of ways: " , number_of_ways()
    print "Number of unique users: " , number_of_unique_users()
    print "Top contributing users: " , top_contributing_users()
    print "Average Contriution per user: " , Avg_contribution()
    print "Common ammenities: " , common_ammenities()
    print "Popular Banks: " , popular_bank()
    print "Popular cuisines: " , popular_cuisines()


# In[ ]:



