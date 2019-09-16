#Eliot Brown
#CS 1134

#1
import DoublyLinkedList #can only import if it is in the same folder

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList() #how to add that imported file, name of file.name of class

    def __len__(self):
        return len(self.data) #this goes to __len__ method in DoublyLinkedList

    def is_empty(self):
        return len(self) == 0

    def push(self, elem):
        self.data.add_last(elem)

    def pop(self):
        self.data.delete_last()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.last_node()


AStack = LinkedStack()
AStack.push(5)
AStack.push(9)
AStack.push(8)
AStack.pop()
#print(AStack.top)
#print(AStack.data)

#2a
import ArrayStack

class ArrayLeakyStack:
    def __init__(self, max_num_of_elems):
        self.data =[None]*max_num_of_elems
        self.num_of_elems = 0
        self.max_num_of_elems = max_num_of_elems
        self.front_ind = None  #back_ind is actually front

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return self.num_of_elems == 0

    def push(self, elem):

        if self.is_empty():
            self.data[0] = elem
            self.num_of_elems = 1
            self.front_ind = 0


        elif self.num_of_elems == self.max_num_of_elems:
            self.data[self.front_ind] = elem
            self.front_ind = (self.front_ind + 1) % (self.num_of_elems)

        else:
            self.data[self.num_of_elems] = elem
            self.num_of_elems += 1
            self.front_ind += 1


    def pop(self):

        if self.is_empty():
            raise Exception("Array is empty")

        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.num_of_elems -= 1
        return val


    def top(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.data[self.front_ind]

AArray = ArrayLeakyStack(3)
AArray.is_empty()
AArray.push(5)
AArray.push(7)
AArray.push(9)
#print(AArray.data)
AArray.push(11)
AArray.pop()
#print(AArray.data)




#2b
#import DoublyLinkedList()

class LinkedLeadkyStack:
    def __init__(self, max_num_of_elems):
        self.data = DoublyLinkedList.DoublyLinkedList()
        self.max_num_of_elems = max_num_of_elems

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, elem):
        if len(self) == self.max_num_of_elems:
            self.data.delete_first()
            self.data.add_last(elem)
        else:
            self.data.add_last(elem)

    def pop(self):
        self.data.delete_last()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.last_node()

BStack = LinkedLeadkyStack(2)
BStack.push(5)
BStack.push(9)
BStack.push(8)
BStack.push(7)
#print(BStack.top())
#print(BStack.data)



#3
import ArrayQueue

class QStack:
    def __init__(self):
        self.data_queue = ArrayQueue.ArrayQueue()
        self.num_elem = 0 #just used as a check for pop method

    def __len__(self):
        return self.data_queue.num_of_elems

    def is_empty(self):
        return self.data_queue.num_of_elems == 0

    def push(self, elem): #run time = O(n)
        self.data_queue.enqueue(elem)
        self.num_elem += 1


    def pop(self): #run time = O(n) Omega(n)

        for num in range(len(self.data_queue)-1):
            self.data_queue.enqueue(self.data_queue.dequeue())
        self.data_queue.dequeue()
        self.num_elem -= 1


    def top(self): #run time = O(n) Omega(n)
        for __ in range(len(self.data_queue)-1):
            self.data_queue.enqueue(self.data_queue.dequeue()) #two individual operations #if one resizes O(n) then the other will be O(1)
        val = self.data_queue.dequeue()
        self.data_queue.enqueue(val)

        return val


BQueue = QStack()
BQueue.push(5)
BQueue.push(9)
BQueue.push(8)
BQueue.push(7)
#print(BQueue.data_queue.data)
#print(BQueue.top())
#print(BQueue.num_elem)
#print(BQueue.is_empty())
BQueue.pop() #should pop 5
#print(BQueue.num_elem)
#print(BQueue.top())
#print(BQueue.data_queue.data)