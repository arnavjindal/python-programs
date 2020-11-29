#
#
import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +91 (703) 2439787
Fax: +91 (703) 2439791
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''
#
# # # findall, search, split, sub, finditer
# # # patt = re.compile(r'fass')
# # # patt = re.compile(r'.adm')
# # # patt = re.compile(r'^Tata')
# # # patt = re.compile(r'iin$')
# # # patt = re.compile(r'ai{2}')
# # # patt = re.compile(r'(ai){1}')
# # # patt = re.compile(r'ai{1}|Fax')
#
#
# # # Special Sequences
# # # patt = re.compile(r'Fax\b')
# # # patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
# # # Task
# # # Given a string with a lot of indian phone numbers starting from +91
# print(type(patt)) #<class 're.Pattern'>
# matches = patt.finditer(mystr)
# print(type(matches)) #<class 'callable_iterator'>
# for match in matches:
#     print(match)
#     print(type(match)) #<class 're.Match'>


"""
practicing -----------------------------------------------
"""


st = """
02225929434
07932903757
952502405719
+918948725234
02223434062
02223714297
01125466913 
01122716158 
95129224927
02502502675
24572223629 
02228627537 
02225243653 
07922130557 
02228821018 
02225236627
01242561014 
02223071477 
"""

pater = re.compile(r'\+91\s\(\d{3}\)\s\d{7}')
mat = pater.finditer(mystr)
for matches in mat:
    # pass
    print(matches.group())
    print(matches)
# print(matches.string)



# knowledge  -----
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match