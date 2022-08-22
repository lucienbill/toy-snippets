def formatMdTable(s):
    lines = s.split("\n")
    
    # read each line -> get max column length
    max_l = list(0 for n in range(len(lines[0].split("|")))) #init
    
    for l in lines:
        columns = l.split("|")
        index = 0
        for c in columns:
            if len(c) > max_l[index]:
                max_l[index] = len(c)
            index += 1

    # Format lines
    newTable = []
    for l in lines:
        columns = l.split("|")
        index = 0
        newCol = []
        for c in columns:
            # fill the empty space (with spaces)
            filler = "".join(list(" " for n in range(max_l[index] - len(c))))
            newCol.append(c + filler)
            index += 1
        newTable.append("|".join(newCol))

    # Special case : second line (ex: "| --- | ------- |"
    newTable[1] = newTable[1].replace(" ", "-").replace("|-", "| ").replace("-|", " |")
    return "\n".join(newTable)
        
# Example
i = "| Syntax | Description |\
\n| --- | ----------- |\
\n| Header | Title |\
\n| Paragraph | Text |"

print(formatMdTable(i))
