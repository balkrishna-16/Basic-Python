import math
print("Hellow world! ")
print("Mero naam Balkrishna Chaudhary ho")
print("Welcome to the Python ")
print(math.cos(3.65))
print("Calculation")
# -----------------------------------------------------
a=5
b=7
print(a+b)
print(type(a))
c= 7.8
print(type(c))
d = "I am IT student"
print(type(d))
print (d)
# ---------------------------------------------------------

str1 = "this is my first python string"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.format())
print(str1.swapcase())
print(str1.find("this"))
# ------------------------------------------------------------

items =["Bkc",1,2,3]
print(items)
print(type(items))
print(type(items))
items[1] = "Anshu"
items[2] = "Raju"
items[3] = "Nawaraj"
print(items)
# --------------------------------------------------------------

tup1 = (1,2,3)
print(type(tup1))
print[0] =2
print(tru1)
# --------------------------------------------------------------

dict1 = {}
print(type(dict1))
print(dict1)

dict1["Dhoni"]= 100
dict1["sachin"]= 200
print(dict1)
print(dict1.get("Dhoni"))
print(dict1.items())
print(dict1.keys())

# ---------------------------------------------------------------

list1 =[1,2,3,4,4,1,3]
print(list1)
s1 = set(list1)
print(s1)
# ----------------------------------------------------------------

var = int(input())
print(var)
if (var>4):
   print("Variable is greater")
elif(var>=2):
   print("Variable is two")
else:
   print("Variable is not greater")

for i in range(0, 101):
   print(i)
# --------------------------------------------------------------------

i= 0
while(i<100):
   i =i+1
   print(i)
# --------------------------------------------------------------------

def average(num1,num2):
   avr = (num1 + num2)/2
   return avr
print(average(3,6))
# ---------------------------------------------------------------------

index =3
try:
   print(index)
except Exception as e:
   print(e)
# ------------------------------------------------------------------------

f= open("1.txt", "w")
f.write("Never Loss Hope You Never Know What Tomarrow You Might Bring")
f.close()
f= open("1.txt","r")
content = f.read()
f.close()
print(content)
    
