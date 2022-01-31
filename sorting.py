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
    n = len(numbers)  # n is a variable containing the number of elements in 'numbers'
                      # In Python, we use the len function to get the number of elements
                      # in a list

    # Here we use a 'for-loop' to check the numbers in all of the positions of the list
    # range(n) below returns a sequence of number from 0 up to n-1:
    # So, 'for i in range(n)' basically means
    # "for each number 'i' in the sequence [0, 1, 2, ..., n-1]"
    # 'i' in here is used for accessing the numbers in the list (also known as an index or position).
    # In Python, we access the elements of a list by using the syntax of the following form:
    # list_name[index]
    # and the first element is located at index 0, second element is at index 1,
    # and so on, up to the last element at index n-1
    # (this is the way it works in Python and many other programming languages).
    for i in range(n):
        cur_num = numbers[i]  # cur_num represents the number that we're currently checking

        min_num = cur_num     # min_num represents the minimum number in the portion of the list from index i up to n-1.
                              # in this case, it is by default set to cur_num.
                              # This may or may not change later in the comparison step.

        min_index = i         # This is similar to min_num, but it contains the index of the minimum number
                              # in the portion of the list from index i up to n-1.

        # Find index of minimum element in the 'remaining' portion of the list
        # (the portion of the list starting from the position that is 1 index
        # next to the current number up to the last number)

        # Like before, we are using a for loop, but this time we are using it
        # to search for the minimum number in the portion of the list from index
        # i+1 (the position that is 1 index to the right of our current number at index 'i', up to n-1)
        for j in range(i+1, n):  # here j is used to denote the index of this portion of the list
            if numbers[j] < min_num:  # if the number at index j is smaller than min_num
                                      # (which by default contains the number at index i)
                min_num = numbers[j]  # we set min_num to be the number at index j
                min_index = j         # and set the min_index to be j
        # After this loop runs, you'll end up with min_num containing the minimum number in
        # the portion of the list STARTING FROM index i up to n-1
        # and min_index to be the index of this number

        # decide if we want to swap min_num with cur_num
        # if min_num >= cur_num, we do not swap
        # otherwise we swap
        if min_num < cur_num:
            numbers[i] = min_num  # set numbers[i] to min_num
            numbers[min_index] = cur_num  # set numbers[min_index] to cur_num


# Run the script using the code below
if __name__ == "__main__":
    # an unsorted list with all unique numbers
    nums = [3, 1, 2, 5, 4, 8, 6, 7, 9]
    nums_copy = [3, 1, 2, 5, 4, 8, 6, 7, 9]
    print("Before Sorting: {}".format(nums))
    selection_sort(nums)
    print("After Sorting:  {}".format(nums))
    print(nums == sorted(nums_copy))
    print()


    # an unsorted list with duplicate elements (two 3s)
    nums =      [3, 1, 2, 5, 4, 8, 3, 6, 7, 9]
    nums_copy = [3, 1, 2, 5, 4, 8, 3, 6, 7, 9]
    print("Before Sorting: {}".format(nums))
    selection_sort(nums)
    print("After Sorting:  {}".format(nums))
    print(nums == sorted(nums_copy))
    print()

    # an unsorted list containing a negative number
    nums =      [3, 1, 2, 5, 4, 8, 6, 7, 9, 1234, -111]
    nums_copy = [3, 1, 2, 5, 4, 8, 6, 7, 9, 1234, -111]
    print("Before Sorting: {}".format(nums))
    selection_sort(nums)
    print("After Sorting:  {}".format(nums))
    print(nums == sorted(nums_copy))
    print()

    # an list containing multiple copies of the same number
    nums = [3, 3, 3, 3, 3, 3, 3, 3]
    nums_copy = [3, 3, 3, 3, 3, 3, 3, 3]
    print("Before Sorting: {}".format(nums))
    selection_sort(nums)
    print("After Sorting:  {}".format(nums))
    print(nums == sorted(nums_copy))
    print()

    # a sorted list
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums_copy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Before Sorting: {}".format(nums))
    selection_sort(nums)
    print("After Sorting:  {}".format(nums))
    print(nums == sorted(nums_copy))
    print()


# NOTE: I usually write selection sort in a simpler way but I find the one
#       above easier to explain. I also usually decompose the function into
#       smaller functions that each only perform one specific task.