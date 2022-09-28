#Find factorial of a number using iteration

def fact_iterative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact

def fact_recursive(n):
    if n==1:
        return 1
    else:
        print(n )
        return n * fact_recursive(n-1)

number = int(input("Enter a number :"))
print("Factorial by iterative method: ", fact_iterative(number))
print("Factorial by recursive method: ", fact_recursive(number))





