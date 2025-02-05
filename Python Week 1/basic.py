print("Hello")
print("Hello World")

# -> comment

# python interpreter is written in C language
# every line executed in python interpreter is
#   1 statement 
#   2 expression

"Tanaya"
"""Tanaya"""

100 + 200
_+ 200 # _ is the previous answer

a = "a"
type(a)

# four bacis data types in python
# 1 string
# 2 integer
# 3 float
# 4 complex

# these four are similar to the C interpreter therefore these are considered as the basic

# primitives are inbuild variables that doesnt depend on anything that means those are logics of interpreter 

isinstance("a",int)
isinstance("b", str)

a = 255
print(id(a))

a = 200
print(id(a))

a = 4864121894184121333
print(a+1)


# python are platform independent inspiration from linux
# interpreter are platform dependent

print(1)

print(1, 2, 3, "jatin", 3.4, 1 + 5j, sep=",")

print("Hello")
print("World!")

print("Hello", end=":")
print("World!")

# print has accept can take infinite numberof arguments and prints with space
# print after every execution new line character is added

print("a")
print("b")
print("c")

print("a", end=" ")
print("b", end=" ")
print("c")

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep="-")


a = input()
123456
print(a)
print(type(a))


#python delimits only on the / characters

# C++ supports type casting

int a = 65
char b = (char)a:

bin(65)

# typer coercion is shown by python

a = 15
str(a)
'15'

int('1234')

float('1.5')

a = 65
isinstance(a, object)
a= 'A'
isinstance(a, object)


sum(1,2)
# mul(2, sum(y,5)

print(5+5) #addition
print(10-6) #subraction
print(10/5) #division
print(10*5) #multiplication
print(12//5) #floor division
print(10%3) # mod
print(2**3) # to the power

isinstance(10.0,int)
isinstance(10.0,float)

print("jatin"+"kaytal")
print("abc"*5)

#comparision operations

print(1 == 2)
print(1!=2)
print(1 < 2)
print(2 > 3)
print("ab" < "z") # lexicographic comparision
print("a"<"A")
print("A"<"a")

# logical operators

print(True and False)
print(True or False)
print(True and 1)
print(1 and 0)
print(1 and 5)

isinstance(True, int)

type(True)

bool(1)

# Short Circuiting

# True or b = True
# False or b = b
# True and b = b
# False and b = False

# a or b = a (if a is truthy)
# a or b = b(if a is falsy)
# a and b = b(if a is truthy)
# a and b = a (if a is falsy)

# "jatin" and 6
# " " or 6

1.6 or ''
"" or 2.5

bool([])

bool([1,2,3])

"" and 0
112 and ""


# 1 indent  = 2 spaces, 4 spaces ,tab , 9 spaces user defined

a = True
if True:
    print("A")

a = False

if a:
    print("the value is true")
print("end")

a = False
if a:
    print("this value is true")
elif a == 5:
    print("this value is 5")
else:
    print("this value is false")

# if x<0:
#     sign=-1
# if x == 0:
#     sign=0
# if x>0:
#     sign = 1

# x = int(-inf, inf)
# G -> x 

# a= x < 0
# b = x == 0
# c = x > 0

# a int b = b int c = a int c = phi
# a u b u c != 0 then else statement
# conditions are mutually exclusive

# q = can profile A access profile B

# a = isFriend
# b = isBlocked
# c = isAdmin
# d = isMarkZuckerberg

# a b c d q
# 0 0 0 0 0   
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 1
# 0 1 0 0 0
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 1
# 1 0 0 0 1
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 0
# 1 1 0 1 1
# 1 1 1 0 0
# 1 1 1 1 1

if ___:
    print("has access")
else:
    print("access denied")


# while loop
a = 1 
while a<10:
    print(a)
    a += 1

# if we dont know how many iterations takes place then while loop
# temple run

# when we know how many iterations takes palce then for loop

while battery.notDead():
    pass

# for loop

# works in the concept of sequences

a = 1
a.__str__

name = 'jakin'

name.__iter__


for c in name:
    print(c)

print(type(name))
print('****')
for c in name:
    print(c)
    print(type(c))

# we cant iterate over integers complex numbers floats

for i in range(5):
    print(i)

# for i in 1:
#     print(i)
for i in range(5):
i.__str__

for i in range(5):
    print(i)
    if i == 3:
        break

for i in range(5):
    print(i)
    del i

a = 1
print(a)
del a 
print(a)

for i in [0,1,2,3,4]:
    print(i)
    i = 100
    print(i)


if True:
    # I dont know what to do
    pass
print("Rest of the code")

for i in range(5):
    print(i)
else:
    print("something")

for i in range(5):
    print(i)
    if i == 3:
        break
    print(i)
else:
    print("something")


n = 5 #[0,n)

for i in range(n):
    for j in range(n):
        print(i, end=' ')
    #     print(i)
    # print()
    # print("\n")

for i in range(n):
    for j in range(n):
        print(n-j, end=' ')
    print()


for i in range(n):
    for j in range(n):
        print(j+1, end=' ')
    print()


for i in range(n):
    for j in range(n):
        print(i+1, end=' ')
    print()



for i in range(n):
    for j in range(n):
        print(n-i, end=' ')
    print()

n=7
for i in range(n):
    for j in range(n):
        print(max(i+1, j+1, n-1, n-j), end=' ')
    print()


n=5
for i in range(n):
    for j in range(n):
        i, j
        print((i,j), end=' ')
    print()

n=7
for i in range(n):
    for j in range(n):
        print(i, end=' ')
    print()

n=7
for i in range(n):
    for j in range(n):
        print(j, end=' ')
    print()

n=7
for i in range(n):
    for j in range(n):
        print(max(i,j), end=' ')
    print()

n=7
for i in range(n):
    for j in range(n):
        print(n-i-1, end=' ')
    print()


max(7,8,20,6)
# gives the max value

n=7
for i in range(n):
    for j in range(n):
        print((n-j-1,n-i-1), end=' ')
    print()

n=5
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1),max(n-j,n-i), end=' ')
    print()

max(1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17)

sum(1,2,3,4,5,6,7,8,9)
