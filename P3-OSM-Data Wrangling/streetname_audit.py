
# coding: utf-8

# In[ ]:

# CHECKING THE STREET TYPES and MAPPING THE STREET NAMES
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Road", "Cross", "Colony", "Block", "Place", "Square", "Lane", "Extension", 
            "Layout", "Nagar", "Main","Town","Suburb","Stage","Post","Peenya"]

Mapping = { "cross": "Cross",
            "road": "Road",
            "block":"Block",
            "colony":"Colony",              
            }
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    new_street_name = street_name
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            new_street_name = update_name(street_name)
    return new_street_name
            
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit(osmfile):
    with open('Vpura2.osm','w')as output: # to update corrections
        output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        output.write('<osm>\n  ')
        osm_file = open(osmfile, "r",encoding="utf8")
        street_types = defaultdict(set)
        for event, elem in ET.iterparse(osm_file,events = ('start','end')):
            if event == 'end' and (elem.tag in ["node","way","relation","bounds"]):
                if elem.tag == "node" or elem.tag == "way":
                    for tag in elem.iter("tag"):
                        if is_street_name(tag):
                            new_value =audit_street_type(street_types, tag.attrib['v'])
                            tag.attrib['v']= new_value
                output.write(ET.tostring(elem).decode('utf8'))
        output.write('</osm>')
        osm_file.close()
    return street_types

def update_name(name, mapping = Mapping):
    if name.find(",")!= -1: # replacing the unwanted commas
        name = name.replace(',','')
    else:# replacing the last word
        split = name.rsplit(' ', 1)
        if len(split)>1:
            newname =split[0]
            keyword = split[1]
            if keyword in mapping:
                keyword = mapping[keyword]
            name = newname+' '+keyword
    return name

#MAIN FUNCTION
if __name__ == "__main__":
    
    #PROBLEMS CORRECTED AND WRITTEN TO NEW FILE Vpura1.osm and will be henceforth used in the analysis
    OSM_PATH = "Vpura1.osm"
    #MAPPING STREET NAMES
    st_types = audit(OSM_PATH)
    pprint.pprint(dict(st_types))

