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
re.findall(r"a|b", "a c c d b c a")
# output: ['a', 'b', 'a']

re.findall(r"ab", "a c c d b c a ab ce ab")
# output: ['ab', 'ab']

re.findall(r"[^c]", "a c c d b c a ab ce ab")
# # output: 
# ['a',
#  ' ',
#  ' ',
#  ' ',
#  'd',
#  ' ',
#  'b',
#  ' ',
#  ' ',
#  'a',
#  ' ',
#  'a',
#  'b',
#  ' ',
#  'e',
#  ' ',
#  'a',
#  'b']


# %%
match = re.search(r"(\w\d)+", "xyza2b1c3dd")
match 
# output: <re.Match object; span=(3, 9), match='a2b1c3'>

print(f"matched: {match.group()}")
# output: matched: a2b1c3

print(f"span: {match.span()}")
# output: (3, 9)

print(f"start: {match.start()} & end: {match.end()}")
# output: start: 3 & end: 9


# %%
match = re.match("pattern", "string to match")  # Try to apply the pattern at the start of the string.
if match:
    print("do something with the matched")
else:
    print("found no matches")

# output: found no matches


# %%
match = re.match(r"(\w+), (\w+)", "Homework, urgent: today")
print(match)
# output: <re.Match object; span=(0, 16), match='Homework, urgent'>

match.groups()
# # output: ('Homework', 'urgent')

match.group(0)
# output: 'Homework, urgent'

match.group(1)
# output: 'Homework'

match.group(2)
# output: 'urgent'


# %%
re.search(r"\d+", "ab12xy")
# output: <re.Match object; span=(2, 4), match='21'>

re.search(r"\d+", "ab21dczy")
# output: 


# %%
re.match(r"\d+", "ab12xy")
# output: None

re.match(r"\d+", "ab21dczy")
# output: None

re.match(r"\d+", "12abcxyz")
# output: <re.Match object; span=(0, 2), match='12'>


# %%
re.findall(r"h[ie]\w", "hi hey hello")
# output: ['hey', 'hel']

re.findall(r"(h|H)(i|e)", "hi Hey hello")
# output: [('h', 'i'), ('H', 'e'), ('h', 'e')]


# %%
re.finditer(r"(h|H)(i|e)", "hi Hey hello")
# output: <callable_iterator at 0x153e3aee550>


# %%
re.split(r"\d+", 'a1b2c3d4e')
# output: ['a', 'b', 'c', 'd', 'e']
 
 
# %%
re.sub(r"\D", "-", '123,456,789')   # substitute
# output: '123-456-789'
 
 
# %%
raw_data = """101, Homework; Complete physics and math
some random nensense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234; random; record
Another random record"""    # r"(\d{3}), (\w+); (.+)"   regular expression pattern 


regex = re.compile(r"(\d{3}), (\w+); (.+)")
for line in raw_data.split("\n"):
    match = regex.match(line)
    if match:
        print(f"{'Matched:':<12}{match.group()}")


# # output: 
# Matched:    101, Homework; Complete physics and math
# No Match:   some random nonsense
# Matched:    102, Laundry; Wash all the clothes today
# No Match:   54, random; record
# Matched:    103, Museum; All about Egypt
# No Match:   1234, random; record
# No Match:   Another random record


# %%
regex = re.compile(r"(\d{3}), (\w+); (.+)")
tasks = []

for line in raw_data.split("\n"):
    match = regex.match(line)
    if match:
        task = (match.group(1), match.group(2), match.group(3))

        tasks.append(task)

print(tasks)
# output: [('101', 'Homework', 'Complete physics and math'), ('102', 'Laundry', 'Wash all the clothes today'), ('103', 'Museum', 'All about Egypt')]


# %%
regex = re.compile(r"(?P<task_id>\d{3}), (?P<task_title>\w); (?P<task_desc>.+)")
tasks = []

for line in raw_data.split("\n"):
    match = regex.match(line)
    if match:
        task = (match.group('task_id'), match.group('task_title'), match.group('task_desc'))
        tasks.append(task)


# match.groupdict()


# %%
