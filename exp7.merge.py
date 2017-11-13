def mergesort(numbers):
    # check for the empty list or the list with single element
    if not numbers or len(numbers) == 1:
        return numbers
    # recursive splitting (Divide)
    else:
        mid = len(numbers)//2
        left = mergesort(numbers[:mid])
        right = mergesort(numbers[mid:])
        return merge(left, right)

