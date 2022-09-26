print("If you want to log data enter 1 or to retrive data enter 2 :")
request = int(input())

print("Whose data you want to update Harry, Rohan or Hammed")
user_name = input()
user_name = user_name.lower()

print("If you want to update exercise details enter 1 or to update food details enter 2")
details = int(input())
# print(type(request), type(details), request, details)

def getDate():
    import datetime
    return datetime.datetime.now()

def logData(name, word,info):
    date = getDate()
    #print(date)
    f = open(name+"_"+word+".txt", "a")
    f.write("["+str(date)+"] : "+ info + "\n")
    print("Data updated")
    f.close()

def retriveData(name, word):
    f = open(name + "_" + word + ".txt", "rt")
    print(f.read())
    f.close()

if request == 1:

    if details == 1:
        info= input("Enter info that you want to store :")
        logData(user_name,"exercise",info)
    elif details == 2:
        info= input("Enter info that you want to store :")
        logData(user_name,"food",info)
    else:
        print("Enter either 1 or 2")

elif request == 2:

    if details == 1:
        retriveData(user_name, "exercise")
    elif details == 2:
        retriveData(user_name, "food")
    else:
        print("Enter either 1 or 2======1")

else:
    print("Enter either 1 or 2")

