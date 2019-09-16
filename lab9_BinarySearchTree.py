#Eliot Brown
#Lab 9

#1


#2
import BinarySearchTreeMap

def are_bst_keys_same(bst1, bst2):
    lst1 = []
    lst2 = []
    for key in bst1:
        lst1.append(key)
    for key in bst2:
        lst2.append(key)
    if len(lst1) != len(lst2):
        return False
    lst1.sort()
    lst2.sort()
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

tree1 = BinarySearchTreeMap.BinarySearchTreeMap()
tree2 = BinarySearchTreeMap.BinarySearchTreeMap()

tree1[5] = 4
tree1[1] = 10
tree1[10] = 15

tree2[15] = 12
tree2[10] = 17
tree2[1] = 1
tree2[5] = 5
# print(tree1)
# print(tree2)

m = are_bst_keys_same(tree1, tree2)
#print(m)

#3
import LinkedBinaryTree

def is_bst(binary_tree):
    # if binary_tree is None:
    #     rootvalue = None
    # else:
    #     rootvalue = binary_tree.root
    return is_bst_helper(binary_tree.root)[0]
def is_bst_helper(subtree_root):
    if subtree_root is None or (subtree_root.right is None and subtree_root.left is None):
        return (True, None, None)
    elif subtree_root.num_children() ==1:
        if subtree_root.left != None:
            (lbool, lmin, lmax) = is_bst_helper(subtree_root.left)
            return (lbool and (lmax<subtree_root.left), lmin, subtree_root)
        else:
            (rbool,rmin, rmax) = is_bst_helper(subtree_root.right)
            return (rbool and (rmin>subtree_root.right), subtree_root,rmax)
    else:
        (llbool, lmin, lmax) = is_bst_helper(subtree_root.left)
        (rbool, rmin, rmax) = is_bst_helper(subtree_root.right)




    #     if subtree_root is None:
    #         return (True, rootvalue,rootvalue)
    #     parent = subtree_root.parent.data
    #     left_bool, left_max, left_min = is_bst_helper(subtree_root.left)
    #     right_bool, right_max, right_min = is_bst_helper(subtree_root.right)
    #
    #     if left_min < parent < left_max and right_min < parent < right_max:
    #         if left_max < parent < right_min: #compare both trees
    #             return (True, right_max.data, left_min.data)
    #     # if right_min < parent < right_max:
    #     #     if left_max
    #     else:
    #         return (False, right_max.data, left_min.data)
    # return is_bst_helper(binary_tree.root)[0]

lbt = LinkedBinaryTree.LinkedBinaryTree()
left_child1 = lbt.Node(4)
right_left = lbt.Node(8)
right_child1 = lbt.Node(5, right_left)
root_node1 = lbt.Node(2, left_child1, right_child1)
print(is_bst(lbt))
tree1 = None
print(is_bst(tree1))
# tree1 = LinkedBinaryTree.LinkedBinaryTree(root_node1)
# print(is_bst(tree1))

#4

def lca_bst(bst, node1, node2): #O(h) where h is the height

    res = True
    root = bst.root
    while res is True:
        if root.item.key > max(node1.item.key, node2.item.key):
            root = root.left
        elif root.item.key < min(node1.item.key, node2.item.key):
            root = root.right
        else:
            res = False

    return root.item.key


tree1 = BinarySearchTreeMap.BinarySearchTreeMap()


lst = [20,10,28,8,15,22,50,25]
for i in lst:
    tree1.insert(i)

node1 = tree1.find(10)
node2 = tree1.find(10)

print(lca_bst(tree1, node1, node2))


#in class version

def lca_bst(bst, node1, node2):
    #basically when the curr_node has node1 and node two on the right and left, not both on one side
    curr_node = bst.root
    key1, key2 = node1.item.key, node2.item.key
    while curr_node is not None:
        if curr_node.data < key1 and curr_node.data < key2:
            curr_node = curr_node.right
        elif curr_node.data > key2 and curr_node.data > key2:
            curr_node = curr_node.left
        else:
            return curr_node