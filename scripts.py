# 97 submission HackerRank Accepted con punteggio pieno, dalla più recente.
# Ogni sezione è uno script autonomo: eseguirne una alla volta.
# I codici sono conservati come inviati; alcuni richiedono NumPy o Python 2.

# === Linear Algebra | punteggio 20.0 | submission 485448193 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n = int(input())

matrix = np.array([input().split() for _ in range(n)], float)

print(round(np.linalg.det(matrix), 2))

# === Polynomials | punteggio 20.0 | submission 485447854 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

coeffs = list(map(float, input().split()))
x = float(input())

print(np.polyval(coeffs, x))

# === Inner and Outer | punteggio 20.0 | submission 485447541 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

a = np.array(input().split(), int)
b = np.array(input().split(), int)

print(np.inner(a, b))
print(np.outer(a, b))

# === Dot and Cross | punteggio 20.0 | submission 485447433 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n = int(input())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(np.dot(a, b))

# === Mean, Var, and Std | punteggio 20.0 | submission 485447304 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.around(np.std(arr), 11))

# === Insertion Sort - Part 2 | punteggio 30.0 | submission 485447075 ===
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        while i > 0 and arr[i] < arr[i - 1]:
            trash = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = trash
            i -= 1
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

# === Insertion Sort - Part 1 | punteggio 30.0 | submission 485445519 ===
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    x = arr[-1]
    i = n - 2
    while x < arr[i] and i >= 0:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = x
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# === Recursive Digit Sum | punteggio 30.0 | submission 485444061 ===
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if len(n) > 1:
        return superDigit(str(sum(int(i) for i in n)), k)
    return n * k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(superDigit(n, k), 1)

    fptr.write(str(result) + '\n')

    fptr.close()

# === Viral Advertising | punteggio 15.0 | submission 485433292 ===
#!/bin/python3

import math as m
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    dl = [2]
    ds = 0
    for i in range(n):
        if i == 0:
            continue
        ds = dl[i-1] * 3
        dl.append(m.floor(ds / 2))
    return sum(dl)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# === Number Line Jumps | punteggio 10.0 | submission 485432538 ===
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# === Birthday Cake Candles | punteggio 10.0 | submission 485431283 ===
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    m = max(candles)
    count = 0
    for c in candles:
        if c == m:
            count += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# === Min and Max | punteggio 20.0 | submission 485431034 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

print(np.max(np.min(np.array([input().split() for _ in range(int(input().split()[0]))], int), axis = 1)))

# === Sum and Prod | punteggio 20.0 | submission 485430840 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

print(np.prod(np.sum(np.array([input().split() for _ in range(int(input().split()[0]))], int), axis = 0)))

# === Floor, Ceil and Rint | punteggio 20.0 | submission 485430675 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')

a = np.array(input().split(), float)

for fn in [np.floor, np.ceil, np.rint]:
    print(fn(a))

# === Array Mathematics | punteggio 20.0 | submission 485430452 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n, _ = map(int, input().split())
a1 = np.array([input().split() for _ in range(n)], int)
a2 = np.array([input().split() for _ in range(n)], int)

for op in ['add', 'subtract', 'multiply', 'floor_divide', 'mod', 'power']:
    print(getattr(np, op)(a1, a2))

# === Eye and Identity | punteggio 20.0 | submission 485429883 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m))

# === Zeros and Ones | punteggio 20.0 | submission 485429699 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype = int))
print(np.ones(shape, dtype = int))

# === Concatenate | punteggio 20.0 | submission 485429351 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M, _ = map(int, input().split())
a1 = np.array([input().split() for _ in range(N)], dtype = int)
a2 = np.array([input().split() for _ in range(M)], dtype = int)

print(np.concatenate((a1, a2)))

# === Transpose and Flatten | punteggio 20.0 | submission 485428933 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

N, M = input().split()
l = []
for i in range(int(N)):
    row = input().split()
    l2 = []
    for j in range(int(M)):
        l2.append(int(row[j]))
    l.append(l2)
l = numpy.array(l)   
print(numpy.transpose(l))
print(l.flatten())

# === Shape and Reshape | punteggio 20.0 | submission 485428086 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
print(numpy.reshape([int(i) for i in input().split()], (3, 3)))

# === Arrays | punteggio 20.0 | submission 485386892 ===
import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# === Decorators 2 - Name Directory | punteggio 30.0 | submission 485386064 ===
import operator

def person_lister(f):
    def inner(people):
        for person in people:
            person[2] = int(person[2])
        people.sort(key=operator.itemgetter(2))
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# === Standardize Mobile Number Using Decorators | punteggio 30.0 | submission 485385225 ===
def wrapper(f):
    
    def fun(l):
        formatted = [f"+91 {n[-10:-5]} {n[-5:]}" for n in l]
        
        return f(formatted)

    return fun
    
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

# === XML2 - Find the Maximum Depth | punteggio 20.0 | submission 485384045 ===
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# === XML 1 - Find the Score | punteggio 20.0 | submission 485383355 ===
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    n = len(node.attrib)
    for child in node:
        if len(child) == 0:
            n += len(child.attrib)
        else:
            n += len(child.attrib) + get_attr_number(child)
    return n

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# === Matrix Script | punteggio 100.0 | submission 485322151 ===
#!/bin/python3

import math
import os
import random
import re
import sys


n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

decoded = "".join(matrix[row][col] for col in range(m) for row in range(n))

pattern = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'

print(re.sub(pattern, ' ', decoded))

# === Validating Postal Codes | punteggio 80.0 | submission 485320879 ===
regex_integer_in_range = r"^[1-9]\d{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# === Validating Credit Card Numbers | punteggio 40.0 | submission 485319347 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

for _ in range(int(input())):
    number = input()
    if re.match(pattern, number):
        if re.search(r'(\d)\1{3}', number.replace('-', '')):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")

# === Validating UID | punteggio 40.0 | submission 485237660 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r"^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[a-zA-Z0-9]{10}$"

for _ in range(int(input())):
    uid = input().strip()
    print("Valid" if re.match(pattern, uid) else "Invalid")

# === Detect HTML Tags, Attributes and Attribute Values | punteggio 30.0 | submission 485237273 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")
    
    handle_startendtag = handle_starttag
    
html_code = "\n".join(input() for _ in range(int(input())))

MyHTMLParser().feed(html_code)

# === Hex Color Code | punteggio 30.0 | submission 485235619 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'(?<!^)(#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}))\b'

for _ in range(int(input())):
    matches = re.findall(pattern, input())
    for color in matches:
        print(color)

# === Validating and Parsing Email Addresses | punteggio 20.0 | submission 485234487 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

email_pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for _ in range(int(input())):
    name, addr = email.utils.parseaddr(input())
    
    if re.match(email_pattern, addr):
        print(email.utils.formataddr((name, addr)))

# === HTML Parser - Part 2 | punteggio 30.0 | submission 485233701 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split("\n")) > 1:
            print(">>> Multi-line Comment")
            for d in data.split("\n"):
                print(d)
        else:
            print(f">>> Single-line Comment\n{data}")
    def handle_data(self, data):
        if data != "\n":
            print(f">>> Data\n{data}")
            
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input()+"\n")

# === HTML Parser - Part 1 | punteggio 30.0 | submission 485232215 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

parser = MyHTMLParser()  
for _ in range(int(input())):
    parser.feed(input())

# === Validating Roman Numerals | punteggio 20.0 | submission 485230542 ===
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"  # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

# === Regex Substitution | punteggio 20.0 | submission 485131025 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    s = input()
    s = re.sub(r"(?<= )\&{2}(?= )", "and", s)
    s = re.sub(r"(?<= )\|{2}(?= )", "or", s)
    print(s)

# === Re.findall() & Re.finditer() | punteggio 20.0 | submission 485109747 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
found = False

l = re.finditer(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])", s)

for i in l:
    print(i.group(1))
    found = True
    
if not found:
    print("-1")

# === Re.start() & Re.end() | punteggio 20.0 | submission 485108583 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
sub = input()
found = False

for m in re.finditer(f"(?={re.escape(sub)})", s):
    if m:
        print(f"({m.start()}, {m.start() + len(sub) - 1})")
        found = True

if not found:
    print("(-1, -1)")

# === Validating phone numbers | punteggio 20.0 | submission 485106775 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    n = input()
    if re.match("^[789]\d{9}$", n):
        print("YES")
    else:
        print("NO")

# === Group(), Groups() & Groupdict() | punteggio 20.0 | submission 485105753 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = re.search(r"([a-zA-Z0-9])\1+", input())
if m:
    print(m.group(1))
else:
    print(-1)

# === Re.split() | punteggio 20.0 | submission 485103512 ===
regex_pattern = r"[,.]"  # Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

# === Detect Floating Point Number | punteggio 20.0 | submission 484872101 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    num = input()
    
    if num[-1] == ".":
        print("False")
        continue
    
    dotcount = num.count(".")
    if dotcount != 1:
        print("False")
        continue
    
    try:
        float(num)
        print("True")
    except ValueError:
        print("False")

# === Map and Lambda Function | punteggio 20.0 | submission 484720208 ===
cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    l = [0]
    for i in range(1, n):
        if i <= 2:
            l.append(1)
        else:
            l.append(l[-2]+l[-1])
    return l
    
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# === ginortS | punteggio 40.0 | submission 484650756 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()
Sl, Su, So, Se = [], [], [], []
for i in S:
    if i.islower():
        Sl.append(i)
    elif i.isupper():
        Su.append(i)
    elif int(i) % 2 != 0:
        So.append(i)
    elif int(i) % 2 == 0:
        Se.append(i)

Sl.sort()
Su.sort()
So.sort()
Se.sort()

print("".join(Sl + Su + So + Se))

# === Athlete Sort | punteggio 30.0 | submission 484648006 ===
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    
    arr.sort(key=lambda x: x[k])
    
    for row in arr:
        print(*row)

# === Zipped! | punteggio 10.0 | submission 484646253 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())
L = []

for i in range(X):
    L.append(input().split())
    for j in range(N):
        L[i][j] = float(L[i][j])

for i in range(N):
    print(sum(list(zip(*L))[i])/X)

# === Exceptions | punteggio 10.0 | submission 484356021 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a, b = input().split()
        
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# === Time Delta | punteggio 30.0 | submission 484354964 ===
#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    form = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, form)
    t2 = datetime.strptime(t2, form)
    return(str(int(abs((t1 - t2).total_seconds()))))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# === Calendar Module | punteggio 10.0 | submission 484351394 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from calendar import weekday

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
l = input().split()
print(days[weekday(int(l[2]), int(l[0]), int(l[1]))])

# === Word Order | punteggio 50.0 | submission 484350613 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

l = Counter([input() for _ in range(int(input()))])
print(len(l))
print(*l.values())

# === Company Logo | punteggio 30.0 | submission 484350180 ===
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    print(*[f"{x} {y}" for x, y in sorted(Counter(input()).items(), key = lambda x: (-x[1], x[0]))[:3]], sep = "\n")

# === Piling Up! | punteggio 50.0 | submission 484343067 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

def checkstack():
    _, d = int(input()), deque(map(int, input().split()))
    pile = deque()
    for i in d:
        if len(pile) == 0:
            if i <= d[-1]:
                pile.append(d[-1])
            else:
                pile.append(i)
        elif len(pile) > 0:
            if i <= d[-1] and d[-1] <= pile[0]:
                pile.appendleft(d[-1])
            elif i > d[-1] and i <= pile[0]:
                pile.appendleft(i)
            else:
                return print("No")
    return print("Yes")
   

if __name__ == "__main__":
    for _ in range(int(input())):
        checkstack()

# === Collections.deque() | punteggio 20.0 | submission 484341719 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):
    attr = input().split()
    if len(attr) > 1:
        getattr(d, attr[0])(attr[1])
    else:
        getattr(d, attr[0])()

print(*d)

# === Collections.OrderedDict() | punteggio 20.0 | submission 484331776 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

OD = OrderedDict()

for _ in range(int(input())):
    row = input().split()
    item = " ".join(row[:-1])
    if item not in OD:
        OD[item] = int(row[-1])
    else:
        OD[item] += int(row[-1])

for key, value in OD.items():
    print(f"{key} {value}")

# === DefaultDict Tutorial | punteggio 20.0 | submission 484297173 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)
for i in range(n):
    d[input()].append(i + 1)

for _ in range(m):
    print(*d.get(input(), [-1]))

# === collections.Counter() | punteggio 10.0 | submission 484293869 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

_, L = int(input()), input().split()
I = Counter(L)

Money = 0

for _ in range(int(input())):
    size, price = input().split() 
    if I[size] > 0:
        I[size] -= 1
        Money += int(price)
    else:
        continue
        
print(Money)

# === Check Strict Superset | punteggio 10.0 | submission 484062940 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
N = int(input())
count = 0
for _ in range(N):
    S = set(input().split())
    if S & A == S and len(A & S) > 0:
        count += 1
print(count == N)

# === Check Subset | punteggio 10.0 | submission 484062381 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    _, A, _, B = input(), set(input().split()), input(), set(input().split())
    print(A & B == A)

# === The Captain's Room | punteggio 10.0 | submission 484061775 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
A = input().split()

s1 = set()
s2 = set()

for i in A:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
        
print((s1 - s2).pop())

# === Set Mutations | punteggio 10.0 | submission 484059699 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
_, A = input(), set(map(int, input().split()))
for i in range(int(input())):
    getattr(A, input().split()[0])(int(x) for x in input().split())
print(sum(A))

# === Set .symmetric_difference() Operation | punteggio 10.0 | submission 484058897 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
_, E, _, F = input(), set(input().split()), input(), set(input().split())
print(len(E ^ F))

# === Set .difference() Operation | punteggio 10.0 | submission 484058746 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
_, E, _, F = input(), set(input().split()), input(), set(input().split())
print(len(E - F))

# === Set .intersection() Operation | punteggio 10.0 | submission 484058585 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
_, E, _, F = input(), set(input().split()), input(), set(input().split())
print(len(E & F))

# === Set .union() Operation | punteggio 10.0 | submission 484058445 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
_, E, _, F = input(), set(input().split()), input(), set(input().split())
print(len(E | F))

# === Set .discard(), .remove() & .pop() | punteggio 10.0 | submission 484057967 ===
n = int(input())
s = set(map(int, input().split()))

N = int(input())
comms = [input() for _ in range(N)]

for i in comms:
    if i.split()[0] == "remove" and int(i.split()[1]) in s:
        s.remove(int(i.split()[1]))
    elif i.split()[0] == "discard":
        s.discard(int(i.split()[1]))
    elif i == "pop" and len(s) > 0:
        s.pop()

print(sum(s))

# === Set .add() | punteggio 10.0 | submission 483931451 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    N = int(input())
    s = set()
    for i in range(N):
        s.add(input())
    print(len(s))

# === No Idea! | punteggio 50.0 | submission 483931041 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    input()
    arr = input().split()
    A, B = set(input().split()), set(input().split())
    happiness = 0
    for i in arr:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1
    print(happiness)

# === Symmetric Difference | punteggio 10.0 | submission 483929145 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    M, Sm, N, Sn = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
    Diff = list((Sm.union(Sn)).difference(Sm.intersection(Sn)))
    Diff.sort()
    for i in Diff:
        print(i)

# === Introduction to Sets | punteggio 10.0 | submission 483778471 ===
def average(array):
    array2 = set(array)
    return f"{sum(array2)/len(array2):.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# === Merge the Tools! | punteggio 40.0 | submission 483774121 ===
def merge_the_tools(string, k):
    T = [string[i:i+k] for i in range(0, len(string), k)]
    T2 = []
    for t in T:
        t2 = ""
        for l in t:
            if l in t2:
                continue
            else:
                t2 += l
        T2.append(t2)
    for t2 in T2:
        print(t2)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# === The Minion Game | punteggio 40.0 | submission 483772681 ===
def minion_game(string):
    S = 0
    K = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            K += len(string) - i
        else:
            S += len(string) - i
    if S > K:
        print(f"Stuart {S}")
    elif S < K:
        print(f"Kevin {K}")
    else:
        print("Draw")
     

if __name__ == '__main__':
    s = input()
    minion_game(s)

# === Capitalize! | punteggio 20.0 | submission 483771630 ===
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    i = 0
    s2 = ""
    while i < len(s):
        if i == 0 or s[i-1] == " ":
            s2 += s[i].upper()
        else:
            s2 += s[i]
        i += 1
    return s2
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# === Alphabet Rangoli | punteggio 20.0 | submission 483764778 ===
def print_rangoli(size):
    w = size * 4 - 3
    output = ""
    for n in range(-(size-1), size):
        n2 = abs(n)
        indexes = list(range(size-1, n2, -1)) + list(range(n2, size))
        output += "-".join(chr(ord("a") + i) for i in indexes).center(w, "-")+"\n"
    print(output)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# === String Formatting | punteggio 10.0 | submission 483762415 ===
def print_formatted(number):
    space = len(bin(number)[2:]) + 1
    for n in range(1, number+1):
        print(str(n).rjust(space-1)+oct(n)[2:].rjust(space)+
              hex(n)[2:].upper().rjust(space)+bin(n)[2:].rjust(space))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# === Designer Door Mat | punteggio 10.0 | submission 483761624 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N, M = map(int, input().split())
    #TOP PART
    for i in range(0, N-2, 2):
        print((".|."*(i+1)).center(M, "-"))
    #CENTER
    print("WELCOME".center(M, "-"))
    #BOTTOM PART
    for i in range(N-2, 0, -2):
        print((".|."*(i)).center(M, "-"))














# === Text Wrap | punteggio 10.0 | submission 483759855 ===
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# === Text Alignment | punteggio 10.0 | submission 483759200 ===
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# === String Validators | punteggio 10.0 | submission 483758023 ===
if __name__ == '__main__':
    s = input()
    l = [0, 0, 0, 0, 0]
    for c in s:
        if c.isalnum():
            l[0] = 1
        if c.isalpha():
            l[1] = 1
        if c.isdigit():
            l[2] = 1
        if c.islower():
            l[3] = 1
        if c.isupper():
            l[4] = 1
    for n in l:
        if n == 1:
            print("True")
        else:
            print("False")

# === Find a string | punteggio 10.0 | submission 483757350 ===
def count_substring(string, sub_string):
    sublen = len(sub_string)
    count = 0
    i = 0
    while i <= len(string):
        if string[i:i+sublen] == sub_string:
            count += 1
            i += sublen - 1
        else:
            i += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# === Mutations | punteggio 10.0 | submission 483755675 ===
def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# === What's Your Name? | punteggio 10.0 | submission 483755469 ===
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first+' '+last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# === String Split and Join | punteggio 10.0 | submission 483755142 ===


def split_and_join(line):
    line = line.split()
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# === sWAP cASE | punteggio 10.0 | submission 483754843 ===
def swap_case(s):
    s2 = ""
    for l in s:
        if l.islower():
            s2 += l.upper()
        else:
            s2 += l.lower()
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# === Tuples | punteggio 10.0 | submission 483720314 ===
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))

# === Lists | punteggio 10.0 | submission 483719094 ===
if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command, *args = input().split()
        if command == "print":
            print(l)
        else:
            args = list(map(int, args))
            getattr(l, command)(*args)

# === Finding the percentage | punteggio 10.0 | submission 483717838 ===
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    values = student_marks[query_name]
    print(f"{sum(values)/len(values):.2f}")

# === Collections.namedtuple() | punteggio 20.0 | submission 483717730 ===
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    Spreadsheet = namedtuple('Spreadsheet', input().split())
    students = []
    for _ in range(n):
        student = Spreadsheet(*input().split())
        students.append(student)
    print(f"{sum(int(students[i].MARKS) for i in range(n))/n:.2f}")

# === Nested Lists | punteggio 10.0 | submission 483698827 ===
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = set()
    for element in records:
        scores.add(element[1])
    grade = sorted(scores)[1]
    output = []
    for element in records:
        if element[1] == grade:
            output.append(element[0])
    output = sorted(output)
    for name in output:
        print(name)

# === Find the Runner-Up Score! | punteggio 10.0 | submission 483697653 ===
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = max(arr)
    rnrup = -100
    for i in arr:
        if i == first:
            continue
        if i > rnrup:
            rnrup = i
    print(rnrup)

# === List Comprehensions | punteggio 10.0 | submission 483696611 ===
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(l)

# === Print Function | punteggio 20.0 | submission 483695200 ===
if __name__ == '__main__':
    n = int(input())
    res = ""
    for i in range(1, n+1):
        res += f"{i}"
    print(res)

# === Write a function | punteggio 10.0 | submission 483694868 ===
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        if year % 100 == 0 and year % 400 != 0:
            return False
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# === Loops | punteggio 10.0 | submission 483694416 ===
if __name__ == '__main__':
    n = int(input())
    for i in range(n): print(i**2)

# === Python: Division | punteggio 10.0 | submission 483694175 ===
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a // b}\n{a / b}")

# === Arithmetic Operators | punteggio 10.0 | submission 483694091 ===
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a + b}\n{a - b}\n{a * b}")

# === Python If-Else | punteggio 10.0 | submission 483693869 ===
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

# === Say "Hello, World!" With Python | punteggio 5.0 | submission 483693349 ===
if __name__ == '__main__':
    print("Hello, World!")





