
# coding: utf-8

# In[ ]:


# PIN CODE CORRECTION
import csv
import pprint
import xml.etree.cElementTree as ET


def Correct_Pincode(postcode,Corrected_Pin):
    new_postcode = postcode
    if len(postcode) >6:
        print("Problem PostCodes:")
        print (postcode)
        new_postcode = postcode.replace(",","").replace(" ","").replace("-","")
        if new_postcode not in Corrected_Pin:
            Corrected_Pin.append(new_postcode)
    return new_postcode,Corrected_Pin

def is_post_code(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit_pin(osmfile):
    Corrected_Pin = []
    osm_file = open(osmfile, "r",encoding="utf8")
    for event, elem in ET.iterparse(osm_file,events = ('start','end')):
        if elem.tag == "node" or elem.tag == "way":
                    for tag in elem.iter("tag"):
                        if is_post_code(tag):
                            new_value,List_Pin =Correct_Pincode(tag.attrib['v'],Corrected_Pin)
                            tag.attrib['v']= new_value
    print ("Corrected PostCodes:")
    print (List_Pin)

if __name__ == "__main__":
      
    # PREPARING  FOR DATABASE
    OSM_PATH = "Vpura2.osm"  
    audit_pin(OSM_PATH) # Corrected Pincode is just displayed by the function and not written back into a new file

