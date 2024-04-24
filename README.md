## Tag XML Extraction
Extract `tagName` and `tagID` values from a [Telerik](https://www.telerik.com/) generated XML.

### Regular Expressions
Achieved by using [Regex](https://regexr.com/) to match the value in-between the string:
```
&quot;ID&quot;:(.*?),&quot;Name&quot;:&quot;(.*?)&quot;,&quot;Description&quot;
```
- *Check [this code line](https://github.com/Pedro-Rosa-10/tag-xml-extraction/blob/main/mainapp.py#L17) for more details*

Where as the `(.*?)` would be the value we are looking for.

### Compilation
Microsoft Windows executable (`.exe`) created using [WinPython tool](https://github.com/winpython/winpython).

### TODOs
1. Extract `tagDescription` from the XML
2. Extract `tagTooltip` data from the XML
3. Create new XML with new data to import
