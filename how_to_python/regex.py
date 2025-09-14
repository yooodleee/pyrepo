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
task_pattern = re.compile("\\\\task")
texts = ["\task", "\\task", "\\\task", "\\\\task"]
for text in texts:
    print(f"Match {text!r}: {task_pattern.match(text)}")

# # output: 
# Match '\task': None
# Match '\\task': <re.Match object; span=(0, 5), match='\\task'>
# Match '\\\task': None
# Match '\\\\task': None


# %%
task_pattern_r = re.compile(r"\\task")
texts = ["\task", "\\task", "\\\task", "\\\\task"]
for text in texts:
    print(f"Match {text!r}: {task_pattern_r.match(text)}")

# # output: 
# Match '\task': None
# Match '\\task': <re.Match object; span=(0, 5), match='\\task'>
# Match '\\\task': None
# Match '\\\\task': None


# %%
