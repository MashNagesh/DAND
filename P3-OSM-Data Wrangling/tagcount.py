
# coding: utf-8

# In[2]:

# COUNTING THE HIGH LEVEL TAGS INSIDE THE VIDYARANYAPURA FILE

import xml.etree.cElementTree as ET
import pprint

OSM_PATH = "Vpura.osm"


def count_tags(filename):
    dicttag = {}
    for event,elem in  ET.iterparse(filename):
        if elem.tag in dicttag:
            dicttag[elem.tag]=dicttag[elem.tag]+1
        else:
            dicttag[elem.tag]=1
    return dicttag

if __name__ == "__main__":
    tags = count_tags(OSM_PATH) 
    # COUNTING HIGHER LEVEL TAGS
    pprint.pprint(tags)


# In[ ]:



