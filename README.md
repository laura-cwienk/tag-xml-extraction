## Tag Xml Extraction
Extract the `tagName` values from the XML generated using [Telerik](https://www.telerik.com/)

#### Regular Expressions
This was achieved by using Regex to match the string in-between the value:
```
regex_pattern = r'&quot;Name&quot;:&quot;(.*?)&quot;,&quot;Description&quot;'
```
