import re

string = "Swati"
pattern = "[A-Z]"
result = re.findall(pattern,string)
print(result)

p1 = r"ti$"   #ends with ti
p2 = r"ai$"   #ends with ai
print(re.search(p1, string))
print(re.search(p2, string))


p3 = '\d+' #digits
print(re.findall(p3, string))
string2 = "20bce0996"
print(re.findall(p3,string2))


#re.compile: regex compiled into objects which have methods.
p4 = re.compile('\w')
print(p4.findall(string2))

p5 = re.compile('\W')
string3 = '#swati$%^'
print(p5.findall(string3))

string4 = "ababaababbbbbb"
p6 = re.compile('ab*')
print(p6.findall(string4))

from re import split
#split
string5 = "Sharmila ma'am is sooo sweet :)))"
print(split('\W+', string5))
print(split('\w', string5))


#




