#Eliot Brown
#CS 1134

#1
class ArrayDeque: #double ended queue
    Initial_capacity = 8

    def __init__(self):
        self.data = [None] * ArrayDeque.Initial_capacity
        self.num_of_elems = 0
        self.front_ind = None
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        return self.num_of_elems == 0
    def first(self):
        if self.num_of_elems == 0:
            raise Exception("Deque is empty")
        return self.data[self.front_ind]
    def last(self):
        if self.num_of_elems == 0:
            raise Exception("Deque is empty")
        return self.data[self.num_of_elems - 1]
    '''Returns (without removing) the element at the back of the Deque
    or raise an Exception if the Deque is empty'''
    def enqueue_first(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2* self.len(self.data))
        if self.is_empty():
            self.front_ind = 0
            self.data[0] = elem
            self.num_of_elems += 1
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.data[self.front_ind] = elem
            self.num_of_elems += 1

    '''Adds elem to the front of the Deque'''
    def enqueue_last(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2* self.len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.num_of_elems += 1

    '''Adds elem to the back of the Deque'''
    def dequeue_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None

        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return elem

    '''Remove and return the element at the front of the Deque
    or raise an Exception if the Deque is empty'''
    def dequeue_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        elem = self.data[back_ind]
        self.num_of_elems -= 1
        self.back_ind = None
        if self.is_empty():
            self.back_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return elem
    '''Remove and return the element at the back of the Deque
    or raise an Exception if the Deque is empty'''
    def resize(self,new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

q=ArrayDeque()
len(q)
q.is_empty()
print(q.is_empty())
q.enqueue_first(5)
q.enqueue_first(4)
q.enqueue_last(7)
q.enqueue_last(1)
q.dequeue_first()
q.dequeue_last()
print(q.first())
print(q.last())




#2
def balanced_expression(str_input):
    stack = []
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    for i in str_input:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            ind = close_list.index(i)
            if (len(stack)>0) and (open_list[ind]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
#print(balanced_expression("{(})"))

#3
def is_matched_html(html_str):
    stack = []
    open_list = ["<"]
    close_list = ["</"]
    for i in get_tags(html_str):
        print(len(stack))
        if i[0] in open_list and i[1] != '/':
            stack.append(i)
        elif i[0:2] in close_list:
            if len(stack) > 0 and i[2:] == stack[len(stack)-1][1:]:
                stack.pop()

    if len(stack) == 0:
        return "Balanced"
    else:
        return"Unbalanced"


def get_tags(html_str): #yeilds html tags
    start = html_str.find('<')
    end = html_str.find('>',start)
    while end != -1:
        yield html_str[start:end+1]
        if start == -1:
            break
        start = html_str.find('<',end+1)
        end = html_str.find('>', start)
    yield html_str[start:]


html_str = '<html><body><h1>My First Heading</h1> <p> My first paragraph.</p></body></html>'
#for i in get_tags(html_str):
    #print(i)

#print(is_matched_html(html_str))
