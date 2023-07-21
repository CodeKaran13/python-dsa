def bubble_sort(list):
    """
    Bubble sort swaps smaller number from j to j - 1 location
    Takes O(n) in best case scenario
    Takes O(n^2) in worst case scenario
    Args:
        list (int): integer array
    """
    if len(list) <= 1:
        return

    """
    Optimizing the sort
    Not necessary to iterate if already sorted
    """

    """
    Optimizing inner loop 
    no need to check last number in array after every iteration hence len(List) - i
    In every iteration greatest number is placed at the end of the array 
    """

    for i in range(0, len(list)):
        isSorted = True
        for j in range(1, len(list) - i):
            if list[j] < list[j - 1]:
                swap(list, j, j - 1)
                isSorted = False

        if isSorted:
            return


def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


numbers = [97, 56, 74, 43, 32, 23, 76]
bubble_sort(numbers)

print(numbers)
