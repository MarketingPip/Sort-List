import string
import re as regex

# Define the filename here you want to replace content in
FileName = "README.md"

# Create a list for storing eaching word in file
lst = []

# Open the file
with open(FileName, 'r') as f:
    # For each line in file
    for line in f:
        # Append the line (stripped / with no white spaces etc)
        lst.append(line.rstrip())
        

# Default Table Of Content Option
Table_of_Contents = 1

Top_Text_Value = ""
Bottom_Text_Value = ""
# Decide which Table of Contents to use

    


# Function To Check If String / Line Is A Number Or Not
#def is_number_regex(s):
    #""" Returns True is string is a number. """
    # Regex Match for Numbers
    #if regex.match("^\d+?\.\d+?$", s) is None:
   #     return s.isdigit()
    # If match found - returns true.
  #  return True



from collections import defaultdict
word_dict = defaultdict(list)
for word in lst:
  word_dict[word[0]].append(word)

final = " "
for word in word_dict:
 # final += f"{letter} ##"
 # print(f"{letter} ##")  
  final += f"## {letter}" + "\n" + str('\n'.join(word_dict[word])) +"\n"
  



######## END OF NEW CODE


for items in lst:
    # Capalitze each first letter in list
    items = string.capwords(items)
    # Check if item/ word in list is a number
    #Check_If_Number = is_number_regex(items)
    checkIfStartsWith(items)
    

    
with open(FileName, 'r') as f:
    contents = f.read()
    for line in contents:
        if "<!---START-SORT-TOC--->" in contents:
            Re_Sub_Value = "<!---START-SORT-TOC--->(?s).*<!---END-SORT-TOC--->"
            Top_Text_Value = "<!---START-SORT-TOC--->"
            Bottom_Text_Value = "<!---END-SORT-TOC--->"
            print("Found match") 
        else:
            Re_Sub_Value = "<!---START-SORT-TOC:1--->(?s).*<!---END-SORT-TOC--->"
            Table_of_Contents = 2
            Top_Text_Value = "<!---START-SORT-TOC:1--->"
            Bottom_Text_Value = "<!---END-SORT-TOC--->"
        
    if Table_of_Contents == 1:
        TOC= f"""
{Top_Text_Value}
| [A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) |
| ------- | ------- | ------- | ------- | ------- |
| [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) |
| [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) |
| [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) |
| [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) |
|         |         | [Z](#z) |         |         |
|         |         | [#](#numbers)        |         |         |
{Bottom_Text_Value}
"""
    else:
        TOC = f"""
{Top_Text_Value}
[0-9](#numbers) | [A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) |
| [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) 
| [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) 
| [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) 
| [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) |
[Z](#z) |
{Bottom_Text_Value}
"""       
    contents = regex.sub("<!---START-OF-SORTEDLIST--->(?s).*<!---END-OF-SORTEDLIST--->", final, contents)
    contents = regex.sub(Re_Sub_Value, TOC, contents)

# With the filename we use early - write out the sorted results
with open(FileName, 'w') as f:
    f.write(contents)     
    
    
