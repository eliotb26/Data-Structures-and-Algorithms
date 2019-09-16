#Eliot Brown
#Homework 3

#1
import DoublyLinkedList

class LinkedQueue:

    def __init__(self):
        self.data = DoublyLinkedList.DoublyLinkedList()
        self.front_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return self.num_of_elems == 0

    def enqueue(self, elem):
        self.data.add_last(elem)
        self.num_of_elems += 1

    def dequeue(self): #make so not including trailer or header !!!!!!!!!!!!!!!!
        if self.data.is_empty():
            raise Exception("Queue is empty")
        else:
            res = self.data.first_node()
            self.data.delete_first()
            self.num_of_elems -= 1
            return res

    def first(self):
        if self.data.is_empty():
            raise Exception("Queue is empty")
        return self.data.first_node()


#2
import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.num_str = num_str
        self.data = DoublyLinkedList.DoublyLinkedList()
        for num in num_str:
            self.data.add_last(int(num))

    def __add__(self, other):
        num1 = self.data.last_node()
        num2 = other.data.last_node()
        result = Integer("0")
        result.data.delete_first()
        carry = 0
        while num1 is not self.data.header and num2 is not other.data.header:
            if num1.data + num2.data + carry < 10:
                result.data.add_first(num1.data + num2.data + carry)
                carry = 0
            else:
                result.data.add_first((num1.data + num2.data + carry)%10)
                carry = 1
            num1 = num1.prev
            num2 = num2.prev
        while num1 is not self.data.header:
            result.data.add_first(num1.data)
            num1 = num1.prev
        while num2 is not other.data.header:
            result.data.add_first(num2.data)
            num2 = num2.prev
        if carry == 1:
            result.data.add_first(1)
        return result
    def __repr__(self):
        res_str = ""
        for num in self.data:
            res_str += str(num)
        return res_str


#3

#takes two (sorted) doubly linked lists
#create and return a new sorted dbl object
def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    new = DoublyLinkedList.DoublyLinkedList()
    return merge_sublists(srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node(),new)

def merge_sublists(node1, node2, new):
# recursively linear time O(n1 + n2)

    if node1.next.data is None and node2.next.data is None:
        if node1.data < node2.data:
            new.add_last(node1.data)
            new.add_last(node2.data)
        else:
            new.add_last(node2.data)
            new.add_last(node1.data)
        return new

    elif node1.next.data is None:
        new.add_last(node2.data)
        return merge_sublists(node1, node2.next, new)
    elif node2.next.data is None:
        new.add_last(node1.data)
        return merge_sublists(node1.next, node2, new)
    elif node1.data < node2.data:
        new.add_last(node1.data)
        return merge_sublists(node1.next, node2, new)
    elif node1.data > node2.data:
        new.add_last(node2.data)
        return merge_sublists(node1, node2.next, new)
    return new


link_lst1 = DoublyLinkedList.DoublyLinkedList()
for i in range(0,10,2):
    link_lst1.add_last(i)

link_lst2 = DoublyLinkedList.DoublyLinkedList()
for i in range(1,10,2):
    link_lst2.add_last(i)
#print(link_lst1, link_lst2)
#print(merge_linked_lists(link_lst1, link_lst2))


#4
import LinkedBinaryTree

def min_max(bin_tree):
    #returns min and max value, as a tuple
    return subtree_min_max(bin_tree.root)

def subtree_min_max(subtree_root):
    if subtree_root is None:
        return (float('inf'), -float('inf'))
    else:
        l_result = subtree_min_max(subtree_root.left)
        r_result = subtree_min_max(subtree_root.right)
        l_min = min(l_result[0],subtree_root.data,r_result[0])
        l_max = max(l_result[1], subtree_root.data, r_result[1])
        return (l_min, l_max)


left_right_right = LinkedBinaryTree.LinkedBinaryTree.Node(4)
left_right_left = LinkedBinaryTree.LinkedBinaryTree.Node(7)
left_right = LinkedBinaryTree.LinkedBinaryTree.Node(9, left_right_left, left_right_right)
left_child1 = LinkedBinaryTree.LinkedBinaryTree.Node(8, None, left_right)

right_right_right = LinkedBinaryTree.LinkedBinaryTree.Node(5)
right_right = LinkedBinaryTree.LinkedBinaryTree.Node(6, None, right_right_right)
right_left = LinkedBinaryTree.LinkedBinaryTree.Node(1)
right_child1 = LinkedBinaryTree.LinkedBinaryTree.Node(2, right_left)

root_node1 = LinkedBinaryTree.LinkedBinaryTree.Node(3, left_child1, right_child1)

bin_tree = LinkedBinaryTree.LinkedBinaryTree(root_node1)
#print(min_max(bin_tree))

#5
import LinkedBinaryTree
import ArrayStack


def iterative_inorders(bin_tree):
    #run linear time
    if bin_tree.is_empty():
        raise Exception("This tree is empty sir")
    stack = ArrayStack.ArrayStack()
    curr_node = bin_tree.root
    while True:
        if curr_node is not None:
            stack.push(curr_node)
            curr_node = curr_node.left
        elif len(stack) != 0:
            curr_node = stack.pop()
            yield curr_node.data
            curr_node = curr_node.right
        elif len(stack) == 0:
            break


left_right_right = LinkedBinaryTree.LinkedBinaryTree.Node(4)
left_right_left = LinkedBinaryTree.LinkedBinaryTree.Node(7)
left_right = LinkedBinaryTree.LinkedBinaryTree.Node(9, left_right_left, left_right_right)
left_child1 = LinkedBinaryTree.LinkedBinaryTree.Node(8, None, left_right)

right_right_right = LinkedBinaryTree.LinkedBinaryTree.Node(5)
right_right = LinkedBinaryTree.LinkedBinaryTree.Node(6, None, right_right_right)
right_left = LinkedBinaryTree.LinkedBinaryTree.Node(1)
right_child1 = LinkedBinaryTree.LinkedBinaryTree.Node(2, right_left, right_right)

root_node1 = LinkedBinaryTree.LinkedBinaryTree.Node(3, left_child1, right_child1)

bin_tree = LinkedBinaryTree.LinkedBinaryTree(root_node1)

# for val in bin_tree.inorder():
#     print(val, end = " ")
# print()
# for val in iterative_inorders(bin_tree):
#     print(val, end=' ')
# print()

#6
#a)

def prefix_expression(expr_tree):
    if expr_tree is None:
        return " "
    else:
        item = ''
        for elem in expr_tree.preorder():
            item += str(elem) + " "
        item = item.strip(" ")
        return item

#b)

def postfix_expression(expr_tree):
    postfix= ''
    for elem in expr_tree.postorder():
        postfix += str(elem) + " "
    postfix = postfix.strip(" ")
    return postfix

#c)

def create_exp_tree(prefix_exp_tree):
    prefix_exp_tree_lst = prefix_exp_tree.split(" ")
    print(prefix_exp_tree_lst)
    i = 0
    fin_tree = LinkedBinaryTree.LinkedBinaryTree()
    parent = 0
    curr = None
    operators = "+-*/"
    while i != (len(prefix_exp_tree_lst)):
        if i == 0:
            fin_tree.root = LinkedBinaryTree.LinkedBinaryTree.Node(prefix_exp_tree_lst[0])
            curr = fin_tree.root
            i += 1
        elif curr.left is None:
            if prefix_exp_tree_lst[i] not in operators:
                curr.left = LinkedBinaryTree.LinkedBinaryTree.Node(int(prefix_exp_tree_lst[i]))
            else:
                curr.left = LinkedBinaryTree.LinkedBinaryTree.Node(prefix_exp_tree_lst[i])
                curr.left.parent = curr
                curr = curr.left
            i += 1
        elif curr.right is None:
            if prefix_exp_tree_lst[i] not in operators:
                curr.right = LinkedBinaryTree.LinkedBinaryTree.Node(int(prefix_exp_tree_lst[i]))
            else:
                curr.right = LinkedBinaryTree.LinkedBinaryTree.Node(prefix_exp_tree_lst[i])
                curr.right.parent = curr
                curr = curr.right
            i += 1
        elif curr.right is not None and curr.left is not None:
            curr = curr.parent
            if curr == fin_tree.root:
                parent += 1
            if parent > 1:
                break
    return fin_tree
