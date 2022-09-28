# l = 10
#
# def function1():
#     m= 5
#     global l
#     l+=15
#     print(l,m)
#
# function1()
# print(l)

def Harry():
    x=20
    def Rohan():
        global x
        x=55
        print("inside rohan",x)
    Rohan()
    print("Inside harry",x)

# print("outside harry",x)
Harry()
print("outside harry",x)
