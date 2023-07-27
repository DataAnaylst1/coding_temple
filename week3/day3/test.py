# test = "hello world"

# test.sort()
# list1 = [1,2,3,4,5,6,7,8,9,0]
# phone_number = " "
# for numbers in list1():
#     phone_number = "'(' +"

def fib(n):
    if( n <=1 ):
        return n
    else:
        return (fib( n-1 ) + fib( n-2 ))

n = int(input("Enter number of terms: "))
print("Fib sequence: ")
for i in range(n):
    print(fib(i))
# so let's say 5 was the term
# if 5 is less than or equal to 1, return 5
# else
# 5-1 + 5-2
# 4 + 3