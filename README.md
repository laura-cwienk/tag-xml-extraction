## Tag XML Extraction
Extract the `tagName` values from the XML generated using [Telerik](https://www.telerik.com/)

### Regular Expressions
Achieved by using [Regex](https://regexr.com/) to match the value in-between the string:
```
&quot;Name&quot;:&quot;(.*?)&quot;,&quot;Description&quot;
```
- *Check [this code line](https://github.com/Pedro-Rosa-10/tag-xml-extraction/blob/main/mainapp.py#L9) for more details*

Where as the `(.*?)` would be the value we are looking for.

### TODOs
1. Extract `tagDescription` from the XML
2. Extract `tagUniqueID` from the XML
3. Export to a `xlsx` file instead of `txt`
