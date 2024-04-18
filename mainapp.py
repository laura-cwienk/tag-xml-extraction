import re, pprint

def extract_values(xml_file):
    # Read the XML file
    with open(xml_file, 'r') as file:
        xml_data = file.read()

    # Define the regular expression
    regex_pattern = r'&quot;Name&quot;:&quot;(.*?)&quot;,&quot;Description&quot;'

    # Find all matches
    matches = re.findall(regex_pattern, xml_data)

    return matches

def write_to_txt(values, txt_file):
    # Write values to the text file
    with open(txt_file, 'w') as file:
        for value in values:
            file.write(value + '\n')

# Example usage
xml_file = './data.xml'
values = extract_values(xml_file)
txt_file = './data.txt'

write_to_txt(values, txt_file)
print(f"\nValues extracted:\n{values}")
print(f"\nValues have been written to: {txt_file}")
