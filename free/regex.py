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
task_pattern = re.compile("\\\\task")   # \\, \\task 
texts = ["\task", "\\task", "\\\task", "\\\\task"]

for text in texts:
    print(f"Match {text!r}: {task_pattern.match(text)}")

# # output: 
# Match '\task': None
# Match '\\task': <re.Match object; span=(0, 5), match='\\task'>
# Match '\\\task': None
# Match '\\\\task': None


# %%
task_pattern = re.compile("\\\\pattern")    # \\, \\pattern 
texts = ["\pattern", "\\pattern", "\\\pattern", "\\\\pattern"]

for text in texts:
    print(f"Match {text!r}: {task_pattern.match(text)}")

# output: 


# %%
task_pattern_r = re.compile(r"\\task")      # raw string: \\task 
texts = ["\task", "\\task", "\\\task", "\\\\task"]

for text in texts:
    print(f"Match {text!r}: {task_pattern_r.match(text)}")

# # output: 
# Match '\task': None
# Match '\\task': <re.Match object; span=(0, 5), match='\\task'>
# Match '\\\task': None
# Match '\\\\task': None


# %%
task_pattern_r = re.compile(r"\\pattern")
texts = ["\pattern", "\\pattern", "\\\pattern", "\\\\pattern"]

for text in texts:
    print(f"Match {text!r}: {task_pattern_r.match(text)}")

# # output: 
# Match '\\pattern': <re.Match object; span=(0, 8), match='\\pattern'>
# Match '\\pattern': <re.Match object; span=(0, 8), match='\\pattern'>
# Match '\\\\pattern': None
# Match '\\\\pattern': None


# %%
