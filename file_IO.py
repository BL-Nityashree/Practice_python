with open("test.txt") as f:
    print(f.readlines())

f = open("test.txt", "rt")
print(f.readline())

f.close()