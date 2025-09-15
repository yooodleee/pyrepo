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
re.search(r"^hi", "hi Python")
# output: <re.Match object; span=(0, 2), match='hi'>

re.search(r"task$", "do the task")
# output: <re.Match object; span=(7, 11), match='task'>

re.search(r"^hi task$", "hi task")
# output: <re.Match object; span=(0, 7), match='hi task'>

re.search(r"^hi task$", "hi Python task")
# output: None


# %%
test_string = "h hi hii hiii hiiii"
test_patterns = [r"hi?", r"hi*", r"hi+", r"hi{3}", r"hi{2,3}", r"hi{2,}",
                 r"hi??", r"hi*?", r"hi+?", r"hi{2,}?"]

for pattern in test_patterns:
    print(f"{pattern: <9}--> {re.findall(pattern, test_string)}")

# # output: 
# hi?      --> ['h', 'hi', 'hi', 'hi', 'hi']
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
re.findall(r"a|b", "a c d d b ab")
# output: ['a', 'b', 'a', 'b']

re.findall(r"a|b", "c d d b")
# output: ['b']

re.findall(r"(abc)", "ab bc abc ac")
# output: ['abc']

re.findall(r"(abc)", "ab bc ac")
# output: []

re.findall(r"[^a]", "abcde")
# output: ['b', 'c', 'd', 'e']


# %%
match = re.search(r"(\w\d)+", "xyza2b1c3dd")

print(match)
# output: <re.Match object; span=(3, 9), match='a2b1c3'>


# %%
print("matched:", match.group())
# output: matched: a2b1c3

print("span:", match.span())
# output: span: (3, 9)

print(f"start: {match.start()} & end: {match.end()}")
# output: start: 3 & end: 9


# %%
match = re.match(r"(\w+), (\w+)", "Homework, urgent: today")
print(match)
# output: <re.Match object; span=(0, 16), match='Homework, urgent'>


# %%
match.groups()
# output: ('Homework', 'urgent')

match.groups(0)
# output: 'Homework, urgent'

match.groups(1)
# output: 'Homework'

match.groups(2)
# output: 'urgent'


# %%
match.span(0)
# output: (0, 16)

match.span(1)
# output: (0, 8)

match.span(1)
# output: (10, 16)


# %%
