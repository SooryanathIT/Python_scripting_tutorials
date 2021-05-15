import re

'''pattern = r'^[aA]...e'
words   = ["Apple" , "AMan" , "azhee" , "alpine" , "ajzx" , "a...e"]

for word in words : 

    print(re.findall(pattern , word))

'''


#a followed b  0 or more b's

pattern = r'ab*b{0,1}'
words = ["bbbbbb" , "abnnnnnn" , "abbbbbbbbbbbb" , "a"]

for word in words : 

    print(re.findall(pattern , word))