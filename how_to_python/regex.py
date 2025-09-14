#########################################
## essentials of regular expressions
#########################################


#%%
import re

messy_data = "process,messy_data_mixed,separators"

regex = re.compile(r"[,_]")
separated_words2 = regex.split(messy_data)

print(separated_words2)
# output: ['process', 'messy', 'data', 'mixed', 'separators']


# %%
import re 

regex = re.compile("do")        # generate pattern
regex.pattern                   # access pattern's attribute
regex.search("do homework")     # use method
regex.findall("don't do that")


# %%
import re 

re.search("pattern", "the string to be searched")
re.findall("pattern", "the string to be searched")


# %%
