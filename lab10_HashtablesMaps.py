#Eliot Brown
#lab 10

#1
''' did in class'''


#2

def list_intersection(lst1, lst2):
    #worst case run time: _O(nlogn + mlogm)!!!!!!!!!!!!!!!!!!!
    inter_lst = []
    new_dict = {}
    for item in lst1:
        new_dict[item] = None
    for val in lst2:
        if val in new_dict:
            inter_lst.append(val)
    return inter_lst
print(list_intersection([5, 6, 1, 10], [6,8, 1, 9, 5, 3, 8]))
''' worst case run time is Theta (n**2) '''


import ChainingHashMap
#in class practice but with a hash map instead of a dictionary
def list_intersection(lst1, lst2):
    elems_in_lst1_map = ChainingHashMap.ChainingHashMap()
    elems_in_lst2_map = ChainingHashMap.ChainingHashMap()
    result_lst = []
    for elem in lst1:
        elems_in_lst1_map[elem] = True
    for elem in lst2:
        elems_in_lst2_map[elem] = True

    for elem in elems_in_lst1_map:
        try:
            if elems_in_lst1_map[elem] == True:
                result_lst.append(elem)
        except:
            pass

    return result_lst

#3

def mode_of_list(lst):
    #put into dict and then count values for the highest
    new_dict = {}
    for val in lst:
        if val not in new_dict:
            new_dict[val] = 1
        else:
            new_dict[val] += 1
    maxx = 0
    mode = None
    for vals in new_dict:
        if new_dict[vals] > maxx:
            maxx = new_dict[vals]
            mode = vals
    return mode
print(mode_of_list([1,3,2,2,2,1,2,1]))

''' Average run time is O(n) 
worst runtime is O(n**2) 
improvement was made when using a dictionary instead of a list
Alternate average run time is Theta(n) 
'''
#4

def two_sum(lst, target):
    #takes an unsorted lst and returns tuples with two nums to sum to target
    two_sum_lst = []
    new_dict = {}
    for i in range(len(lst)):
        new_dict[lst[i]] = i

        val = target - lst[i]
        if val in new_dict:
            ind = new_dict[val]
            return (ind, i)
print(two_sum([-5, 2, 8, -3, 7, 1], -1))

#5

def is_anagram(str1, str2):
    #returns bool
    new_dict = {}
    new_dict2 = {}
    for let in str1:
        if let in new_dict:
            new_dict[let] += 1
        else:
            new_dict[let] = 1
    for item in str2:
        if item in new_dict2:
            new_dict2[item] += 1
        else:
            new_dict2[item] = 1
    for items in new_dict:
        if items not in new_dict2:
            return False
        elif new_dict[items] != new_dict2[items]:
            return False
    for items in new_dict2:
        if items not in new_dict:
            return False

    return True
print(is_anagram('enraed', 'anered'))