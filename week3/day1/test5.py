import re
with open(r'/Users/investmentguy/Documents/coding_temple/week3/day1/regex_test.txt', encoding='utf-8') as f:
    data = f.read()
    print(data)
    
    
def accounts(data):
    pattern = re.compile(r"([a-zA-Z\s]+)")
    matches = pattern.findall(data)
    for match in matches:
        print(f'{match[1]} {match[2]}')
    else:
        return
accounts(data)