import re, pprint, openpyxl

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
    regex_pattern = r'&quot;ID&quot;:(.*?),&quot;Name&quot;:&quot;(.*?)&quot;,&quot;Description&quot;'

    # Find matches
    matches = re.findall(regex_pattern, xml_data)

    # Dict matches
    result_dict = {key: value for key, value in matches}

    return result_dict

def write_to_txt(values, txt_file):
    """ Write dict from extract_values into a txt file

    Args:
        values (dict): key/value pairs for ID and tag name
        txt_file (txt): output file containing dict data
    """
    # Write to txt
    with open(txt_file, 'w') as file:
        for key, value in values.items():
            file.write(f"{key}: {value}\n")

def write_to_excel(values, excel_file):
    """ Write dict from extract_values into a xlsx file

    Args:
        values (dict): key/value pairs for ID and tag name
        excel_file (xlxs): output file containing dict data
    """
    # Create workbook
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write values
    for row, (key, value) in enumerate(values.items(), start=1):
        worksheet.cell(row=row, column=1, value=key)
        worksheet.cell(row=row, column=2, value=value)

    # Save workbook
    workbook.save(excel_file)

# Example usage
xml_file = './data.xml'
values = extract_values(xml_file)
print(f"\nValues extracted:\n{pprint.pformat(values)}")

# For TXT file
# txt_file = './data.txt'
# write_to_txt(values, txt_file)
# print(f"\nValues have been written to: {txt_file}")

# For XLSX file
excel_file = './data.xlsx'
write_to_excel(values, excel_file)
print(f"\nValues have been written to: {excel_file}")
