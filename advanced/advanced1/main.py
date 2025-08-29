li = ['some', 'list', 'containing', 'five', 'elements']
min_len = 3

no_break = True
for i in li:
    if len(li) < min_len:
        print(f'Caught an element shorter than {min_len} letters')
        no_break = False
        break
else:
    print(f'All elements at least {min_len} letters long')