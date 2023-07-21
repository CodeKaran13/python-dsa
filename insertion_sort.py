def insertion_sort(list):
    """
    Insertion sort moves greater numbers to the right and not swap them
    Takes an array of integer
    Takes O(n) in best case scenario
    Takes O(n^2) in worst case scenario
    Args:
        list (int): integer array
    """
    if len(list) <= 1:
        return

    for i in range(1, len(list)):
        current = list[i]
        j = i - 1
        while j >= 0 and current < list[j]:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = current


array = [97, 56, 74, 43, 32, 23, 76]
insertion_sort(array)

print(array)
