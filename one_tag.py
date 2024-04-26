#Import
import xml.etree.ElementTree as ET
import re 

#Function 

def update_xml(xml):

    root = xml.getroot()
    
    #Find CustomShape element 
    custom_shape_tag = root.find('.//CustomShape')
    
    #Get CustomSerializationInfo attribute
    custom_shape_serialization_info = custom_shape_tag.attrib.get('CustomShapeSerializationInfo', '')

    #Replace name
    modified_name = re.sub( r'Demo', r'3140TI0074.PV', custom_shape_serialization_info)

    #Replace description using the modified name
    modified_description = re.sub(r'no data', r'L1 Air/Air HE3', modified_name)

    #Replace id using the modified description
    modified_id = re.sub(r'"ID":0',r'"ID":6233', modified_description)

    #Update the attribute value with the final modified string
    custom_shape_tag.set('CustomShapeSerializationInfo', modified_id)

    #Save new file with the changes 
    xml.write('output.xml', encoding='utf-8', xml_declaration=True)

    return xml


#Load the xml file 
tree = ET.parse('empty_tag.xml')


#Call update xml funtion
output = update_xml(tree)