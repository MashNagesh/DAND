
# coding: utf-8

# In[ ]:

import xml.etree.cElementTree as ET
import pprint
import re

from collections import defaultdict

# Checking if the keys inside the tags have any problems

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    if lower.findall(element.attrib['k']):
        keys['lower']= keys['lower']+1
    elif lower_colon.findall(element.attrib['k']):
        keys['lower_colon'] = keys['lower_colon']+1
    elif problemchars.findall(element.attrib['k']):
        print (element.attrib['k'])
        keys['problemchars'] = keys['problemchars']+1 
        
    else:
        keys['other']= keys['other']+1
    return keys

#Correction written into a new file
def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    with open('Vpura1.osm','w')as output:
        output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        output.write('<osm>\n  ')
        osm_file = open(filename, "r",encoding="utf8")
        for event,element in ET.iterparse(osm_file,events = ('start','end')):
            if event == 'end' and (element.tag in ["node","way","relation","bounds"]):
                for child in element.iter('tag'):
                    keys = key_type(child, keys)
                    if child.attrib['k']== ("ರಾಜಗೋಪಾಲ ನಗರ ರಸ್ತೆ"):
                        child.attrib['k']="addr:street" 
                        child.attrib['v'] = "Rajagopala Nagar"# as per google translate
                output.write(ET.tostring(element).decode("utf8"))
        output.write('</osm>')
        osm_file.close()
    return keys

#MAIN FUNCTION
if __name__ == "__main__":
   
    OSM_PATH = "Vpura.osm"
    # IDENTIFYING PROBLEMATIC KEYS IF ANY 
    keys = process_map(OSM_PATH)
    pprint.pprint(keys)'''

