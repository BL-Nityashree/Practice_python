# products = ["book", "pen", "pencil", "eraser", 56, 98]
# products.insert(1,45)
# products[3] = 'test'
# print(products[::])
#
# tup = (57, 35, 57, 85 )
# # tup[1]=10
# print(tup)
"""
d1 = {"mutable" : "liable to change", "immutable" : "unchanging over time or unable to be changed",
      "set" : "collection of well defined objects" }
print(d1)
print("Enter a word")
word= input()

print("The meaning of the word you have entered is :", d1.get(word) )


print("Enter your Age")
age= int(input())

if age > 18 and age < 80:
      print("You are eligible to drive")
elif age == 18:
      print("Cannot decide your eligibility, need to see you physically")
else:
      print("You are not eligible to drive")
"""

"""
d1 = {"mutable" : "liable to change", "immutable" : "unchanging over time or unable to be changed",
      "set" : "collection of well defined objects" }
print(d1)
print("Enter a word")
word= input()

print("The meaning of the word you have entered is :", d1[word] )
"""

"""
list1= ["Nitya", 6, 7, "Hema", 9, 4]
list2= [["nitya", 2], ["hema", 3]]
dict1= dict(list2)
print(dict1)
for data in dict1.items() :
    print(data)
for item in list1:

    if str(item).isnumeric() and item > 6:
        print(item, "it is a num")
    else:
        print(item,"not a num")
"""
num = 0

while (True):
    num = int(input("Enter a number : "))
    print(num)
    if num <= 100:
        continue
    else:
        print("Congrats! You have entered num greater than 100")
        break





