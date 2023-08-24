# You are given a list of integers. Write a function to find the two numbers that appear the
# most frequently in the list. If multiple pairs have the same frequency, return the pair with the smallest sum.
# For example, given the list [1, 2, 2, 3, 3, 4, 4], the function should return the pair [2, 3]
# because both numbers appear twice, and their sum is smaller than the sums of other pairs with the same frequency.
# Challenge: Cannot use the sorted function.

# Understand 
# list [1, 2, 2, 3, 3, 4, 4]
# We are trying to return two numbers that appear the most frequent, but if there are more than two sets of pairs of numbers,
# Return the two of the lesser

#Plan
# We are dealing with a list, so we can iterate over for each element
# I can create an empty list to return the unique values
# A for loop that will iterate through the list
# I need to alert Python to identify the integers that are more than one value
# I could potentially use set to bring out the unique identifiers but if something has only one value, 
# It will return that as well. 
def most_freq(list_of_nums):
    freq = {}
    answer = []
    for num in list_of_nums:
        freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        for num, freq in freq.items():
            if freq == max_freq:
                answer.append(num)
        x = answer.pop(0)
        y = answer.pop(0)
        return [x,y]
    
most_freq([1,2,2,3,3,4,4])
    