#Whiteboard Question: '''
#Write a function that reverses characters in (possibly nested) parentheses in the input string.
#Input strings will always be well-formed with matching ()s.
#Example
#For inputString = "(bar)", the output should be
#solution(inputString) = "rab";
#For inputString = "foo(bar)baz", the output should be
#solution(inputString) = "foorabbaz";
#For inputString = "foo(bar)baz(blim)", the output should be
#solution(inputString) = "foorabbazmilb";
#For inputString = "foo(bar(baz))blim", the output should be
#solution(inputString) = "foobazrabblim".
#Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".'''
# UPER
# Understand, Plan/Prepare, Execute, and Repeat/Refactor

#Understand
# We need to create a function that reverses characters
# Ensure that strings are will formed with matching ()s

# Plan
# Iterate through the string
# Iteration will be done using the length
# We need a conditional statement and needs to check if there is either a beginning or ending parentheses
# If it's a beginning parentheses, we make a starting index, and if it's an ending parenthese, we create an ending index

#Execute
# def means to define function_name
def solution(inputstring):
    for index in range(len(inputstring)): # range position is present to access each unique index 
        if inputstring[index] == '(':
            start = index
        if inputstring[index] == ')':
            end = index
            return solution(inputstring[:start] + inputstring[start + 1:end][::-1] + inputstring[end + 1:]) 
    return inputstring


def litres(time):
# so for every 1 hour of cycling, there's 0.5 litres of water being consumed
    if time < 1:
            return time *0.5 ==0
    else:
        return (time *0.5)//1