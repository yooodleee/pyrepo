############################
## Regex
############################


# %%
string = "Hello World!"
string.find('H')
# output: 0


# %%
import re 

messy_data = "Work,Hard_Type,Easy"

regex = re.compile(r"[,_]")     # returning a pattern object.
separated_words = regex.split(messy_data)

print(separated_words)
# output: ['Work', 'Hard', 'Type', 'Easy']


# %%
regex = re.compile("do")

regex.pattern # access to pattern attribute
regex.search("do homework") 
regex.findall("don't do that")


# %%
re.search("pattern", "the string to be searched")
re.findall("pattern", "the string to be searched")


# %%
pattern = re.compile(r"[,_]")
result = pattern.findall("apple_banana,grape")

print(result)
# output: ['_', ',']


# %%
text = "apple_banana,grape"
parts = re.split(r"[,_]", text)

print(parts)
# output: ['apple', 'banana', 'grape']


# %%
