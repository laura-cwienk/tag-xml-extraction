#Imports
import xml.etree.ElementTree as ET
import re
import pandas as pd

def update_xml(xml, tags_data):
    """
    This function receives a xml file and a Dataframe and update 
    the xml according to dataframe's info.

    Args:
        xml(ElementTree) : Read xml file.
        tags_data(Dataframe) : Dataframe with tags info.

    Returns: 
        xml(ElementTree) : Updated xml.

    """

    root = xml.getroot()
    
    # Find all CustomShape elements
    custom_shape_tags = root.findall('.//CustomShape')
    
    # Iterate over each row in the DataFrame
    for index, row in tags_data.iterrows():
        if index < len(custom_shape_tags):
            # Get the corresponding CustomShape tag
            custom_shape_tag = custom_shape_tags[index]
            
            # Extract data from the DataFrame row
            name = row['Name']
            new_id = row['ID']
            
            # Get CustomSerializationInfo attribute
            custom_shape_serialization_info = custom_shape_tag.attrib.get('CustomShapeSerializationInfo', '')

            # Replace name
            modified_name = re.sub(r'Demo', name, custom_shape_serialization_info)

            # Replace ID
            modified_id = re.sub(r'"ID":0', f'"ID":{new_id}', modified_name)

            # Update the attribute value with the final modified string
            custom_shape_tag.set('CustomShapeSerializationInfo', modified_id)

    # Save new file with the changes outside the loop
    xml.write('output.xml', encoding='utf-8', xml_declaration=True)

    return xml

# Load Excel file containing tags information
tags_info = pd.read_excel('tags.xlsx')

# Load the XML file
tree = ET.parse('empty_tag.xml')

# Call update_xml function
output = update_xml(tree, tags_info)