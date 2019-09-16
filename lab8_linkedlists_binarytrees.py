#Eliot Brown
#Lab 8

#1
'''
preorder = A, B, D, G, C, E, F, H

inorder = B, G, D, A, E, C, H, F

postorder = G, D, B, E, H, F, C, A


height = 3

depth of node D = 2

'''

#2
import DoublyLinkedList

def right_circular_shift(lnk_lst):
    #should not create and return a new linked list, should mutate,
    new_first = lnk_lst.last_node()
    new_last = new_first.prev #originally this is second last one that will be last one
    second_first = lnk_lst.first_node()

    # point (origianlly) last one to header
    lnk_lst.header.next = new_first
    new_first.prev = lnk_lst.header

    new_first.next = second_first
    second_first.prev = new_first

    new_last.next = lnk_lst.trailer
    lnk_lst.trailer.prev = new_last





# dl = DoublyLinkedList.DoublyLinkedList()
# dl.add_first(5)
# dl.add_first(6)
# dl.add_first(7)
# print(dl)
# right_circular_shift(dl)
# print(dl)



#3
import LinkedBinaryTree

def count_val(root, value): #root is type LinkedBinaryTree.Node
#way in review
    if root is None:
        return 0
    else:

        left_count = count_val(root.left, value) #num of times value appears in left subtree
        right_count = count_val(root.right, value) #num of times value appears in right subtree
        total = left_count + right_count
        if root.data == value:
            total += 1
        return total


    # if root is None:
    #     return 0
    # else:
    #     repeats = 0
    #     left_count = count_val(root.left, value)
    #     right_count = count_val(root.right, value)
    #
    #     # repeats += left_count + right_count
    #     if left_count == value:
    #         repeats += 1
    #     if right_count == value:
    #         repeats += 1
    #     # if root.data == value:
    #     #     repeats += 1
    #     return repeats
    count = 0
    def subtree_inorder(root):
        if root is None:
            return
        else:
            yield from subtree_inorder(root.left)
            yield root.data
            yield from subtree_inorder(root.right)

    generator_to_iterate = subtree_inorder(root)
    for elem in generator_to_iterate:
        if elem == value:
            count += 1
    return count
        # def subtree_preorder(subtree_root):
        #     if subtree_root is None:
        #         return
        #     else:
        #         yield subtree_root.data
        #         yield from subtree_preorder(subtree_root.left)
        #         yield from subtree_preorder(subtree_root.right)
        # generator=subtree_preorder(root)
        # count = 0
        # for elem in generator:
        #     if elem==value:
        #         count+=1
        # return count


#4

def invert_binary_tree(bin_tree):
    # in class method
#way in review
    def invert_helper(subtree_root):
        if subtree_root is None:
            return None
        return LinkedBinaryTree.Node(subtree_root.data, invert_helper(subtree_root.right), invert_helper(subtree_root.left))


    return LinkedBinaryTree.LinkedBinaryTree(invert_helper(bin_tree.root))
''''''
    # new_BT = LinkedBinaryTree.LinkedBinaryTree()
    # def helper(bin_tree, new_BT):
    #     if bin_tree.left is None and bin_tree.right is None:
    #         new_BT.data = bin_tree
    #         return new_BT
    #     elif (bin_tree.left is None) and (not bin_tree.right is None):
    #         invert_binary_tree(bin_tree.right, new_BT.right)
    #         new_BT.left = bin_tree.right
    #
    #     elif (bin_tree.right is None) and (not bin_tree.left is None):
    #         invert_binary_tree(bin_tree.left, new_BT.right)
    #         new_BT.right = bin_tree.left
    #     else:
    #         invert_binary_tree(bin_tree.left, new_BT.left)
    #         invert_binary_tree(bin_tree.right,new_BT.right)
    #         new_BT.right = bin_tree.left
    #         new_BT.left = bin_tree.right
    #
    # old, new = helper(bin_tree, new_BT)
    # return new



    #other way
    # listn = []
    # generator = LinkedBinaryTree.breadth_first()
    # for node in generator:
    #     listn.append(node)
    # for node in listn:
    #     if node.right is not None or node.left is not None:
    #         node.right, node.left = node.left, node.right
    #     elif node.right is not None and node.left is None:
    #         node.left = node.right
    #         node.right = None
    #     elif node.right is None and node.left is not None:
    #         node.right = node.left
    #         node.left = None
    #
    # newtree = LinkedBinaryTree(listn[0])
    # return newtree




#5

def subtree_children_dist(self, subtree_root):  # THIS IS FOR LAB 8 Q5
    def helper(subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root
            yield from helper(subtree_root.left)
            yield from helper(subtree_root.right)

    a = helper(subtree_root)
    list1 = [0, 0, 0]
    for subtree_root in a:
        if subtree_root.left is None and subtree_root.right is None:
            list1[0] += 1
        elif subtree_root.left is None and subtree_root.right is not None:
            list1[1] += 1
        elif subtree_root.left is not None and subtree_root.right is None:
            list1[1] += 1
        else:
            list1[2] += 1

    return list1