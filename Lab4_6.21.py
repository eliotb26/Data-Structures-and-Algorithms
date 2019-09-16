#Eliot Brown
#ecb465
#CS 1134

#3
'''
    a) run time is Theta(log(n))
    
    b) run time would be Theta(n^2)

'''
#4
'sum_lst1'

'sum_list1, low= 0 high= 7'
'sum_list1, low= 1 high= 7'
'sum_list1, low= 2 high= 7'
'sum_list1, low= 3 high= 7'
'sum_list1, low= 4 high= 7'
'sum_list1, low= 5 high= 7'
'sum_list1, low= 6 high= 7'
'sum_list1, low= 7 high= 7'
'returns' #36


'sum_lst2'

'''
sum_list2 low=0, high=7
sum_list2 low=0, high=3
sum_list2 low=0, high=1
sum_list2 low=0, high=0
sum_list2 low=1, high=1
sum_list2 low=2, high=3
sum_list2 low=2, high=2
sum_list2 low=3, high=3
sum_list2 low=4, high=7
sum_list2 low=4, high=5
sum_list2 low=4, high=4
sum_list2 low=5, high=5
sum_list2 low=6, high=7
sum_list2 low=6, high=6
sum_list2 low=7, high=7
36
'''

'''The asymptotic running time of sum_lst1 is O(n) and the run time 
of sum_list2 is O(log(n). This shows that the second function will
be more efficient and faster.'''
#should be sum_lst1 O(n) and sum_lst2 O(n)


#5
''' 
Run time Theta(n**2)
'''
#   b)
import random
def random_str(n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    strin = ''
    for i in range(1, n+1):
        curr = random.choice(letters)
        strin += curr
    return ' '.join(strin)

print(random_str(10))

#6
def powers(base, n):
    for i in range(1, n+1):
        val = base ** i
        yield val

for val in powers(2, 10):
    print(val, end=' ')

#7
def is_palindrome(input_str, low, high):
    if low == high:
        return True
    else:
        if input_str[low] == input_str[high]:
            return is_palindrome(input_str, low+1, high -1)
        else:
            return False


input_str = 'racecar'
length = len(input_str) -1
print(is_palindrome(input_str, 0, length))


#8
def partition(lst):
    upper = len(lst)-1
    low = 1
    while upper != low:
        if lst[upper] < lst[0] and lst[low] > lst[0]:
            lst[upper] , lst[low] = lst[low], lst[upper]
            upper -= 1
            low += 1
        elif lst[low] < lst[0]:
            low += 1
        elif lst[upper] > lst[0]:
            upper -= 1
    lst[upper-1], lst[0] = lst[0], lst[upper-1]
    return lst


print(partition([42,17,81,77,68,22,55,10,90]))


