import re
pattern = re.compile('abcdabcd')
found_pattern = pattern.findall("abcdabcd")
#def pattern1():
#    if x in pattern:
#        print(found_pattern)
#    else: 
#        print("Match not found")
#pattern()

print(found_pattern)

