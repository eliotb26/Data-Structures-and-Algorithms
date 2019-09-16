#Eliot Brown
#Lab 5

#Problem 1

def binary_search(lst, val, low, high):
    if low == high:
        return low
    else:
        mid = (low + high) // 2
        if lst[mid] < val:
            return binary_search(lst, val, mid+1, high)
        elif lst[mid] > val:
            return binary_search(lst, val, low, mid)
        elif lst[mid] == val:
            return low

#print(binary_search([1,2,3,4,5,6], 6, 0, 5))
#print(binary_search([1,2,3,4,5,6,7,8], 7, 0, 7))

#2

def nested_list_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        total = 0
        for elem in lst:
            try:
                total += elem
            except TypeError:
                val = nested_list_sum(elem)
                total += val
        return total
    
    '''
    total = 0
    for elem in lst: 
        if type(elem) == type([]):
            total += nested_list_sum(elem)
        else:
            total += [elem]
    return total'''

#print(nested_list_sum([1, [2, [3], [4, 5]], [6, 7]]))


#3.1
def selection_sort(lst): #O(n**2)
    for i in range(len(lst)):
        smallest_index = i
        for j in range(i, len(lst)):
            if lst[j] <= lst[smallest_index]:
                smallest_index = j
        lst[i], lst[smallest_index] = lst[smallest_index], lst[i]
    return lst

#print(selection_sort([1,4,5,8,44,0,2]))

#3.2
def find_min(lst, low, high):
    min_ind = low
    for i in range(low, high):
        if lst[i] < lst[min_ind]:
            min_ind = i
    return min_ind

def selection_sort_recursive(lst, low, high):
    if low >= high:
        return
    else:
        min_ind = find_min(lst, low, high)
        lst[low], lst[min_ind] = lst[min_ind], lst[low]
        selection_sort_recursive(lst, low+1, high)

lst = [1,5,7,4,6,8]
selection_sort_recursive(lst,0,5)
print(lst)

#4

def partition(lst, low, upper):
    ind = low
    pivot = lst[low]
    low += 1
    while upper >= low:
        if lst[upper] < pivot and lst[low] > pivot:
            lst[upper], lst[low] = lst[low], lst[upper]
            upper -= 1
            low += 1
        while lst[low] < pivot:
            low += 1
        while lst[upper] > pivot:
            upper -= 1

    lst[upper], lst[ind] = lst[ind], lst[upper]
    return upper


def quicksort(lst, start, end):
    if start >= end:
        return
    else:
        part = partition(lst, start, end)
        quicksort(lst, start, part -1)
        quicksort(lst, part+1, end)

lst = [42, 17, 81, 77, 68, 22, 55, 10, 90]
#print(lst)
#print(partition(lst, 0,8))
#quicksort(lst, 0, 8)
#print(lst)