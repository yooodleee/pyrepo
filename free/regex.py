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
re.search(r"^K", "hi Python")
# output: 

re.search(r"Python$", "hi Python")
# output: 

re.search(r"^hi Python$", "hi Python")
# output:

re.search(r"^hi Python$", "hi there Python")
# output: 


# %%
test_string = "h hi hii hiii hiiii"
test_patterns = [
    r"hi", r"hi*", r"hi+", r"hi{3}", r"hi{2,3}", r"hi{2,}",
    r"hi??", r"hi*?", r"hi+?", r"hi{2,}?"
]

for pattern in test_patterns:
    print(f"{pattern: <9}--> {re.findall(pattern, test_string)}")

# # output: 
# hi       --> ['hi', 'hi', 'hi', 'hi']
# hi*      --> ['h', 'hi', 'hii', 'hiii', 'hiiii']
# hi+      --> ['hi', 'hii', 'hiii', 'hiiii']
# hi{3}    --> ['hiii', 'hiii']
# hi{2,3}  --> ['hii', 'hiii', 'hiii']
# hi{2,}   --> ['hii', 'hiii', 'hiiii']
# hi??     --> ['h', 'h', 'h', 'h', 'h']
# hi*?     --> ['h', 'h', 'h', 'h', 'h']
# hi+?     --> ['hi', 'hi', 'hi', 'hi']
# hi{2,}?  --> ['hii', 'hii', 'hii']


# %%
test_text = "#1$2m_M\t"
patterns = ["\d", "\D", "\s", "\S", "\w", "\W", ".", "[lmn]"]

for pattern in patterns:
    print(f"{pattern: <9}---> {re.findall(pattern, test_text)}")

# # output: 
# \d       ---> ['1', '2']
# \D       ---> ['#', '$', 'm', '_', 'M', '\t']
# \s       ---> ['\t']
# \S       ---> ['#', '1', '$', '2', 'm', '_', 'M']
# \w       ---> ['1', '2', 'm', '_', 'M']
# \W       ---> ['#', '$', '\t']
# .        ---> ['#', '1', '$', '2', 'm', '_', 'M', '\t']
# [lmn]    ---> ['m']



# %%
