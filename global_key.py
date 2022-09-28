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
m=50
def Harry():
    k=20
    def Rohan():
        global x
        x=55
        print("inside rohan",x,m,k)
    Rohan()
    print("Inside harry",x,m,k)

# print("outside harry",x)
Harry()
print("outside harry",x,m)
