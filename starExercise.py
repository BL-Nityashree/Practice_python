rows = int(input("Enter the no of rows : "))
status = bool(int(input("Enter either true or false : ")))
print(rows, status)
if status==True:
    print("true")
    for i in range(0,rows):
        for j in range(0, i + 1):
            # printing stars
           #
            print("* ",end=" ")

            # ending line after each row
        print("\r")
else:
    for i in range(rows,0,-1):
        for j in range(i, 0, -1):
            # printing stars
            #print(i,j)
            print("* ", end=" ")

            # ending line after each row
        print("\r")