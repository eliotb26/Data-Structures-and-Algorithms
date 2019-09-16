#Eliot Brown    #split into different files
#HW 2
#Q1:

import random
import time

def max_subsequence_sum1(lst): #O(n^3)
    max_sum = 0
    start_seq = None
    end_seq = None
    for curr_start in range(len(lst)):
        for curr_end in range(curr_start, len(lst)):
            curr_sum = 0
            for i in range(curr_start, curr_end+1):
                curr_sum += lst[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start_seq = curr_start
                end_seq = curr_end
    return max_sum, start_seq, end_seq


def max_subsequence_sum2(lst): #O(n^2)
    max_sum = 0
    start_seq = None
    end_seq = None
    for curr_start in range(len(lst)):
        curr_sum = 0
        for curr_end in range(curr_start, len(lst)):
            curr_sum += lst[curr_end]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start_seq = curr_start
                end_seq = curr_end
    return max_sum, start_seq, end_seq

def max_subsequence_sum3(lst): #O(n)
    max_sum = 0
    start_seq = None
    end_seq = None

    curr_start = 0
    curr_sum = 0
    for curr_end in range(len(lst)):
        curr_sum += lst[curr_end]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start_seq = curr_start
            end_seq = curr_end
        elif curr_sum < 0:
            curr_start = curr_end + 1
            curr_sum = 0
    return max_sum, start_seq, end_seq

class Timer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()



#runtime = my_timer.elapsed()
#max_subsequence_sum2(my_list2)

# my_timer = Timer()
# my_list1 = [random.randint(-10000,10000) for num in range(128)]
# my_timer.reset()
# max_sum, start, end = max_subsequence_sum1(my_list1)
# runtime1 = my_timer.elapsed()
# #print(runtime1)
#     #1 runtime (n= 2^7) = 0.02932572364807129
#     #  runtime (n= 2^8) = 0.3401193618774414
#     #  runtime (n= 2^9) = 2.251329183578491
#     #  runtime (n= 2^10) = 14.930267095565796
#     #  runtime (n= 2^11) =202.39069294929504
#     #  runtime (n= 2^12) = would not finish (to large/to much time)
# my_timer.reset()


# my_timer = Timer()
# my_list2 = [random.randint(-10000,10000) for num in range(1024)]
# my_timer.reset()
# max_sum, start, end = max_subsequence_sum2(my_list2)
# runtime2 = my_timer.elapsed()
# #print(runtime2)
#     #  runtime (n= 2^7) = 0.0009992122650146484
#     #  runtime (n= 2^8) = 0.009651899337768555
#     #  runtime (n= 2^9) = 0.014476776123046875
#     #  runtime (n= 2^10) = 0.10808992385864258
#     #  runtime (n= 2^11) =0.29874181747436523
#     #  runtime (n= 2^12) = 1.0890791416168213
# my_timer.reset()


my_timer = Timer()
my_list3 = [random.randint(-10000,10000) for num in range(2**7*100)]
my_timer.reset()
max_sum, start, end = max_subsequence_sum3(my_list3)
runtime3 = my_timer.elapsed()
#0.000039925575print(runtime3)
    #  runtime (n= 2^7) = 0.0
    #  runtime (n= 2^8) =0.0
    #  runtime (n= 2^9) = 0.0
    #  runtime (n= 2^10) = 0.0010004043579101562
    #  runtime (n= 2^11) = 0.0005109310150146484
    #  runtime (n= 2^12) = 0.0010328292846679688
#my_timer.reset()

#2

def flatten_nested_list(lst, low, high):
    total = []
    low = 0
    while low != len(lst):
        if type(lst[low]) == type([]):
            total.extend(flatten_nested_list(lst[low],0, len(lst[low])-1))
        else:
            total.append(lst[low])
        low += 1
    return total
print(flatten_nested_list([1, [2, 3], 4, [5, [6, [7, [8]]],[9], 10]], 0,3))



#3

def permutation(lst, low, high):
    if low == high:
        return [lst]
    else:
        permutation_list = []
        for ind in range(len(lst)):
            first_elem = lst[ind] #first elem
            rest = lst[:ind] + lst[ind+1:] #all elements up to and after
            for elem in permutation(rest, low+1, high):
                permutation_list.append([first_elem]+elem)
        return permutation_list

#print(permutation([1,2,3,4], 0, 2))


#4
import ArrayStack

class MaxStack:
    #cant use max function
    #push a tuple
    def __init__(self):
        self.data = ArrayStack.ArrayStack()
        self.max_num = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, elem):
        if len(self.data) == 0:
            self.max_num = elem
        if elem > self.max_num:
            val = (elem, self.max_num)
            self.max_num = elem
        else:
            val = (elem, self.max_num)
        self.data.push(val)

    def top(self): #last in first out
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if self.top() == self.max_num:
            self.max_num = self.data.top()[1]
        return self.data.pop() #does not print correctly

    def max(self): #tuple which will point to next max value
        return self.max_num

'''
max_s = MaxStack()
print(max_s.data.data)
print(len(max_s))
print(max_s.is_empty())
max_s.push(1)
max_s.push(2)
print(max_s.data.data)
print(max_s.top())
print(max_s.pop())
print(max_s.data.data)
print(max_s.max())
'''


#5
import ArrayStack

class Queue: #make using two stacks
    def __init__(self):
        self.stack1 = ArrayStack.ArrayStack()
        self.stack2 = ArrayStack.ArrayStack()
        self.num_of_elem = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_elem

    def is_empty(self):
        return self.num_of_elem == 0

    def enqueue(self, elem): #worst case when resizes O(n)


        if self.is_empty():
            self.front_ind = 0
            self.num_of_elem += 1
            self.stack1.push(elem)
            self.back_ind = 1

        else:
            back_ind = (self.front_ind + self.num_of_elem) % len(self.stack1)
            self.stack1.push(elem)
            self.num_of_elem += 1
            self.back_ind += 1


    def dequeue(self): #worst case when resizes O(n)
        if self.is_empty():
            raise Exception("Queue is empty")

        else:
            for val in range(self.num_of_elem):
                self.stack2.push(self.stack1.top())
                self.stack1.pop()
            val_dequeued = self.stack2.top()
            self.stack2.pop()
            self.num_of_elem -= 1

            for val2 in range(self.num_of_elem):
                self.stack1.push(self.stack2.top())
                self.stack2.pop()
            self.front_ind = (self.front_ind + 1) % len(self.stack1) #remakes front index, not needed if dont want complete queue structure
            if self.is_empty():
                self.front_ind = None


            return val_dequeued


    def first(self):

        if self.is_empty():
            raise Exception("Queue is empty")

        return self.stack1.data[0]

'''
my_queue = Queue()
print(len(my_queue))
print(my_queue.is_empty())
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
print(my_queue.stack1.data)
my_queue.dequeue()
print(my_queue.stack1.data)
print(my_queue.first())
'''


#6

import ArrayStack

def eval_postfix_boolean_exp(boolean_exp_str):
    #make a binary tree or can make a stack from class 7.1_7.3
    types = '<>&|'
    args_stack = ArrayStack.ArrayStack()
    lst = boolean_exp_str.split()
    for val in range(len(lst)):
        if lst[val] not in types:
            args_stack.push(lst[val])
        else:
            right_val = args_stack.data.pop()
            left_val = args_stack.data.pop()
            if lst[val] == '<':
                evaluate = left_val < right_val
            elif lst[val] == '>':
                evaluate = left_val > right_val
            elif lst[val] == '&':
                evaluate = left_val and right_val
            elif lst[val] == '|':
                if left_val == True or right_val == True:
                    evaluate = True
            args_stack.push(evaluate)
    boolean = args_stack.top()
    
    

    return boolean


expression = "1 2 < 6 3 < &"
expression2 = "1 2 < 6 3 < |"
expression3 = "5 2 <"
expression4 = "5 2 < 4 6 > |"

#print(eval_postfix_boolean_exp(expression))
#print(eval_postfix_boolean_exp(expression2))
#print(eval_postfix_boolean_exp((expression4)))

