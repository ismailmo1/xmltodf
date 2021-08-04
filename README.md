## Description
converts nested xml files to dataframe with each element as a column, using dot notation to specify nested elements. This tool uses xmltodict to return a nested dictionary which is flattened recursively.


e.g. 

```html
<outertag>
    <innerTag1>a</innerTag1>
    <innerTag2>b</innerTag2>
</outertag>
<outertag>
    <innerTag1>c</innerTag1>
    <innerTag2>d</innerTag2>
</outertag>
```

will return:

| OuterTag.InnerTag1 | OuterTag.InnerTag2 |
| ----------- | ----------- |
| a| b |
| c | d |
## Instructions
clone/download repo and install dependencies with

`pip install requirements.txt`

cd into directory and use as follows: 

`dict_recursion.py [-h] xml_path [csv_folder_path]`



