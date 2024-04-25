import re

def extract_values(xml_file):
    """ Extract unique tag ID and tag name from XML

    Args:
        xml_file (xml): source of the IDs and names

    Returns:
        dict: dict with ID as key and tag name as value
    """
    # Read XML file
    with open(xml_file, 'r') as file:
        xml_data = file.read()

    # Define Regex
    # regex_pattern = r'&quot;ID&quot;:(.*?),&quot;Name&quot;:&quot;(.*?)&quot;,&quot;Description&quot;'
    regex_pattern = r'DataTableColNumber&quot;:(.*?),&quot;DataTableShowTagName'

    # Find matches
    matches = re.findall(regex_pattern, xml_data)

    # Dict matches
    # result_dict = {key: value for key, value in matches}
    result_dict = matches

    return result_dict

def write_to_xml(xml_file):
    """ Write range(0, len(array)) to the 'Col No.'

    Args:
        xml_file (str): path to the XML file

    Returns:
        None
    """
    # Read XML file
    with open(xml_file, 'r') as file:
        xml_data = file.read()

    # Define Regex
    regex_pattern = r'DataTableColNumber&quot;:(.*?),&quot;DataTableShowTagName'

    # Find matches
    matches = re.findall(regex_pattern, xml_data)

    # Length of the first array
    length = len(matches)

    # Generate the array starting from 0 and incrementing by 1
    result_array = list(range(0, length + 1))
    # result_array = ['0'] * length

    # Replace each match with a separate line where the number is incremented sequentially
    modified_xml_data = xml_data
    for i, match in enumerate(matches):
        modified_xml_data = modified_xml_data.replace(f'DataTableColNumber&quot;:{match},&quot;DataTableShowTagName', f'DataTableColNumber&quot;:{result_array[i] + 1},&quot;DataTableShowTagName', 1)
        # modified_xml_data = modified_xml_data.replace(f'DataTableColNumber&quot;:{match},&quot;DataTableShowTagName', f'DataTableColNumber&quot;:{result_array[i]},&quot;DataTableShowTagName', 1)

    # Write the modified XML data back to the file
    with open(xml_file, 'w') as file:
        file.write(modified_xml_data)

# Example usage
xml_file = './data.xml'

# Values before editing
old_values = extract_values(xml_file)
print(f"\nOld values:\n{print(old_values)}")

# Values after editing
values = write_to_xml(xml_file)
new_values = extract_values(xml_file)
print(f"\nNew values:\n{print(new_values)}")
