"""
@author:     Alexander J. Hugo
@student_id: 31058795
"""

"""
In this Python script, I've written a function that sorts
a given list of number in ascending order.

The function is based on the Selection Sort algorithm.
The algorithm starts by having you check all the numbers in the list, 
starting from the first/leftmost number up to the last rightmost number.

For each number you check, you'll compare it with the smallest number
in the remaining part of the list (the portion of the list starting from
the number that is 1 position to the right of the current number, up to 
the last number). 

If the smallest number of the remaining part of the list is indeed smaller
than the current number that you're checking, you swap their positions.
Otherwise there is no swapping, and the current number stays in its position.

We'll then do this for all numbers in the list, and the list will eventually
be sorted :)

We know that the whole list will eventually be sorted, as everytime we check
a number in the list and decide if we want to swap it with the smallest number 
in the 'remaining' portion of the list, the number in the position we're checking
is already in its final position. 

The reason that the number is already in its final
position is because of the fact that everytime we check a number in a given position
in a list, we have to SEARCH for the SMALLEST number in the 'remaining' portion of the 
list. 

To demonstrate this, let's say that we're currently checking the number in the 
FIRST position of the list. Like before, we need to scan the part of the list starting
from the number in the second position up to the number in the last position, for
the smallest number of this portion.
We then compare, is the first number smaller than the minimum number of the 'remaining'
portion and deeccide if we want to swap them or not, as explained before. So, after 
this operation, we know that the number in the first position contains the smallest number
of the list. This operation then is performed for every position of the list, and to give
an example again, if we did this to the number in the second position of the list, the operation
will then cause the numbers in the first and second position to be the 2-smallest numbers of the
whole list, and this number in the second position is also greater than the number in the first
position.

Basically, after every iteration of our operation, the first i-numbers (in this case
'i' denotes the number of iterations of the operation that we've performed so far) 
is already sorted, and the numbers in this portion is smaller than the number in the
'remaining' portion that we haven't checked and performed the operation on.
This is also known as the Loop Invariant, which will be further discussed in
FIT1045/FIT1008/FIT2004.
"""

def selection_sort(numbers):
    """
    This function sorts a given list of number in ascending order.
    It is based on the Selection Sort algorithm.
    :param numbers: a list of number
    """
    n = len(numbers)   # the number of elements in 'numbers'

    # iterate over every of element of 'numbers'
    #   we iterate over the elements by using the index
    #   in this case, the loop starts from index 0 (the first element) up to
    #   index n-1 (the last element)
    for i in range(n):
        cur_num = numbers[i]  # the current number we're 'processing'
        min_num = cur_num     # the current minimum number in
        min_index = i

        # find index of minimum element in the 'unsorted' part of the list
        # at the 1st iteration of the outer loop, the whole list is still treated as unsorted
        for j in range(i+1, n):
            if numbers[j] < min_num:
                min_num = numbers[j]
                min_index = j

        # swap
        if min_num < cur_num:
            numbers[i] = min_num
            numbers[min_index] = cur_num



if __name__ == "__main__":
    # all same elem
    nums = [3, 1, 2, 5, 4, 8, 6, 7, 9]
    nums_copy = [3, 1, 2, 5, 4, 8, 6, 7, 9]
    print(nums)
    selection_sort(nums)
    print(nums)
    print(nums == sorted(nums_copy))
    print()


    # duplicates
    nums =      [3, 1, 2, 5, 4, 8, 3, 6, 7, 9]
    nums_copy = [3, 1, 2, 5, 4, 8, 3, 6, 7, 9]
    print(nums)
    selection_sort(nums)
    print(nums)
    print(nums == sorted(nums_copy))
    print()

    nums =      [3, 1, 2, 5, 4, 8, 6, 7, 9, 1234, -111]
    nums_copy = [3, 1, 2, 5, 4, 8, 6, 7, 9, 1234, -111]
    print(nums)
    selection_sort(nums)
    print(nums)
    print(nums == sorted(nums_copy))
    print()
