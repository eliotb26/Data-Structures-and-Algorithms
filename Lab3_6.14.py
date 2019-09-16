#Eliot Brown
#Lab 3

#2.1
def first1(lst):
    len_1 = len(lst)//2
    val = False
    while val == False:
        if lst[len_1] == 0:
            len_1 += len_1 // 2
        else:
            val = True
        return len_1

#print(first1([0,0,0,0,1,1]))

#print(first1([0,0,0,0,0,0,0,0,1,1,1]))

#log run time is you split in half until you
#find the answer

#linear run time is a loop and that amount
#basically can seperate for/while loops

#nested loops would make the run time
#n^#of loops

#pop affects run time if it is not the last item of lst

#2.2
def e_approximation(n):
    i = 0
    sum = 0
    factorial = 1
    while i <= n:
        if i == 0:
            sum +=1
        else:
            factorial *= i
            val = 1 / factorial
            sum += val
        i += 1
    return sum
#print(e_approximation(50))
#print(e_approximation(10))

def two_sum(sorted_lst, target):
    i = 0
    j = len(sorted_lst)-1
    while sorted_lst[i] + sorted_lst[j] != target:
        if i == (len(sorted_lst)-1) or j == 0:
            return None
        elif sorted_lst[i] + sorted_lst[j] < target:
            i += 1
        elif sorted_lst[i] + sorted_lst[j] > target:
            j -= 1
    return (i,j)
#print(two_sum([-3,-2,0,5,17],2))
#print(two_sum([-1,1,3,4], 0))

#2.4
def split_neg_pos(lst):
    i = len(lst) - 1
    j = 0
    while j < i:
        if lst[j] >= 0 and lst[i] <= 0:
            lst[j],lst[i] = lst[i], lst[j]
            j += 1
            i -= 1
        elif lst[j] >= 0 and lst[i] >= 0:
            i -= 1
        else:
            j += 1
    return lst

#print(split_neg_pos([-7, 5, -3, 4, 2]))
#print(split_neg_pos([-7, 1,-2,7, -3, 4, 2]))

#2.5
def move_zeros(lst):
    i = len(lst) - 1
    j = 0
    while j < i:
        if lst[j] == 0 and lst[i] != 0:
            lst[j],lst[i] = lst[i], lst[j]
            j += 1
            i -= 1
        elif lst[j] == 0 and lst[i] == 0:
            i -= 1
        else:
            j += 1
    return lst
#print(move_zeros([1,0,2,0,0,3,4]))
#print(move_zeros([1,0,0,0,4,0,0]))

#2.6
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_num = find_min(lst[1:])
        lst_min = lst[0]
        if min_num < lst_min:
            lst_min = min_num
        return lst_min

#print(find_min([5, -1, 9, 6,0]))
#print(find_min([5,3,10,25,-40,9]))
